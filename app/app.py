import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flask_session import Session
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Flask session configuration
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your_secret_key")
Session(app)

# MySQL Configuration
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "translator_app"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Initialize LangChain with Groq API
groq_api_key = os.getenv("GROQ_API_KEY")
chat_model = ChatOpenAI(model_name="llama3-8b-8192", openai_api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")

# LangChain Prompt
translation_prompt = PromptTemplate(
    input_variables=["text"],
    template="Translate this English text to Telugu: {text}"
)

def translate_text(text):
    """Translates English text to Telugu using LangChain and Groq API."""
    query = translation_prompt.format(text=text)
    response = chat_model.invoke([HumanMessage(content=query)])
    return response.content

@app.route("/")
def home():
    """Redirects to the login page or translator if logged in."""
    if "user_id" in session:
        return redirect(url_for("translator"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Handles user registration."""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", 
                        (username, email, hashed_password))
            mysql.connection.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("login"))
        except:
            flash("Username or Email already exists.", "danger")
        finally:
            cur.close()

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles user login."""
    if "user_id" in session:
        return redirect(url_for("translator"))  # Redirect if already logged in

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("translator"))  # Redirect to translator after login
        else:
            flash("Invalid email or password", "danger")

    return render_template("login.html")

@app.route("/translator", methods=["GET", "POST"])
def translator():
    """Displays the translator interface and handles translations."""
    if "user_id" not in session:
        flash("Please log in to access the translator.", "warning")
        return redirect(url_for("login"))

    translation = ""
    if request.method == "POST":
        text = request.form["text"]
        translation = translate_text(text)

    return render_template("translator.html", translation=translation)

@app.route("/logout")
def logout():
    """Logs out the user and clears the session."""
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
