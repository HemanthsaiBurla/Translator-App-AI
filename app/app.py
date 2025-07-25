import os
from flask import Flask, render_template, request, session, redirect, url_for
from dotenv import load_dotenv
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = "your_secret_key" 

# Initialize LangChain with Groq API
groq_api_key = os.getenv("GROQ_API_KEY")
chat_model = ChatOpenAI(
    model_name="llama3-8b-8192",
    openai_api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

def translate_text(source_lang, target_lang, text, mode="simple"):
    if mode == "detailed":
        prompt = (
            f"Translate the following from {source_lang} to {target_lang} without any markdown, bullet points, or headings. "
            + (f"Use Simplified Chinese characters only.\n" if target_lang.lower() == "chinese" else "")
            + f"1. Word-level translation.\n"
              f"2. Meaning in one or two lines.\n"
              f"3. Usage or related words (in 1 line).\n\n"
              f'Text: "{text}"'
        )
    else:
        prompt = (
            f'Translate "{text}" from {source_lang} to {target_lang} in a simple, direct way without any note. '
            + ("Use Simplified Chinese characters only." if target_lang.lower() == "chinese" else "")
        )

    response = chat_model.invoke([HumanMessage(content=prompt)])
    return response.content

@app.route("/")
def home():
    return redirect(url_for("translator"))  # Redirect homepage to translator

@app.route("/translator", methods=["GET", "POST"])
def translator():
    if "history" not in session:
        session["history"] = []

    translation = ""
    detailed_translation = ""
    source_lang = "English"
    target_lang = "Telugu"
    text = ""

    if request.method == "POST":
        # Clear history if button clicked
        if "clear" in request.form:
            session["history"] = []
            return redirect(url_for("translator"))

        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]
        text = request.form["text"]
        mode = request.form.get("mode", "simple")

        result = translate_text(source_lang, target_lang, text, mode)

        if mode == "detailed":
            detailed_translation = result
        else:
            translation = result

        # Insert new translation at the beginning (most recent first)
        history = session.get("history", [])
        history.insert(0, (text, result))
        session["history"] = history[:10]  # Keep only last 10

    return render_template("translator.html",
                           translation=translation,
                           detailed_translation=detailed_translation,
                           source_lang=source_lang,
                           target_lang=target_lang,
                           text=text,
                           history=session.get("history", []))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
