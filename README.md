# English-to-Telugu Translator Web App
This is a Flask-based web application that allows users to translate English text into Telugu. The app includes user authentication (registration and login) with MySQL as the database.

## Features
User Registration & Login

Secure Password Storage (Flask-Bcrypt)

Session Management (Flask-Session)

Text Translation using LangChain and Groq API

MySQL Database Integration

## File Structure
```python
translator-app/
│── app.py                 # Main Flask application
│── requirements.txt       # Python dependencies
│── .env                   # Environment variables (API keys, DB credentials)
│── templates/             # HTML files
│   │── login.html
│   │── register.html
│   │── translator.html
│── static/                # CSS, JS, Images
│   │── style.css
│── README.md              # Project documentation
```

## Prerequisites

Make sure you have the following installed:

Python 3.8+

MySQL

Pip

# Installation & Setup

## 1. Clone the Repository
```python
git clone https://github.com/Saimoguloju/English-to-Telugu-Translator.git
cd English-to-Telugu-Translator
```
 

## 2. Create and Activate a Virtual Environment
```python
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

## 3. Install Dependencies
```python
pip install -r requirements.txt
```

## 4. Set Up Environment Variables

Create a .env file in the project root and add the following:
```python
SECRET_KEY=your_secret_key
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=translator_app
GROQ_API_KEY=your_groq_api_key
```

## 5. Set Up MySQL Database

Open MySQL and create a database:
```python
CREATE DATABASE translator_app;
USE translator_app;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```

## 6. Run the Flask App
```python
python app.py
```
Open your browser and go to http://127.0.0.1:5000/

# Usage

Register a new user.

Log in with your credentials.

Enter English text and get the Telugu translation.

# API & Technologies Used

Flask (Web framework)

Flask-Bcrypt (Password hashing)

Flask-Session (Session management)

Flask-MySQLdb (MySQL database connection)

LangChain & Groq API (Text translation)

Bootstrap/CSS (Frontend styling)

# Images
## Register Page
![image alt](https://github.com/Saimoguloju/English-to-Telugu-Translator/blob/main/Images/Register.png)

## Login Page
![image alt](https://github.com/Saimoguloju/English-to-Telugu-Translator/blob/main/Images/Login.png)

## Database
![image alt](https://github.com/Saimoguloju/English-to-Telugu-Translator/blob/main/Images/Database.png)

## Translator
![image alt](https://github.com/Saimoguloju/English-to-Telugu-Translator/blob/main/Images/Translator.png)

# License

This project is licensed under the MIT License.

# Contributing

Feel free to submit issues or pull requests to improve this project.

Made with ❤️ by [Moguloju Sai](https://linktr.ee/Moguloju_Sai)
