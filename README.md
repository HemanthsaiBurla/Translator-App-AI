# Translator-App-AI
# 🌐 Multi-Language Translator App (English ↔ Telugu ↔ Hindi + More)

This is a **simple and clean web-based translation tool** built using **Python (Flask)**. It supports **text translation** through **LangChain**, powered by **Groq API** and **OpenAI API**.

Users can **instantly translate** text between **multiple languages** including **English**, **Telugu**, **Hindi**, and up to **10 other languages**

> 💡 Offers both **Instant Translation** for quick results and **Detailed Translation** to get word meanings, usage, and synonyms.


---

## 🔥 Features

- 🎯 **Direct Translation** (No login or registration)  
- 🔁 **Language Selection** (English ↔ Telugu ↔ Hindi + Upto-10)  
- 🧠 **Simple & Detailed Modes** (Word meanings, usage)  
- 🧾 **Translation History** (Last 10 searches stored)  
- 🌐 Powered by **LangChain + Groq API**  
- 💡 Clean UI with HTML + CSS (local only)  
- 🖼️ Project screenshots for easy understanding  

---

## 🗂️ File Structure

```bash
TRANSLATOR-APP-AI/
│
├── app/
│   ├── flask_session/                # Flask session data
│   ├── Project_Images/              # App screenshots (for README/docs)
│   ├── static/                      # Static files (CSS, JS if any)
│   ├── templates/
│   │   └── translator.html          # Main UI HTML template
│   └── app.py                       # Main Flask app
│
├── .env                             # Environment variables
├── requirements.txt                 # Project dependencies
├── load_api_key.ipynb               # API key test/setup (optional)
├── .gitignore                       # Files to ignore in Git
└── README.md                        # This file
```

---

## ✅ Prerequisites

Make sure you have the following installed:

- Python 3.8+  
- pip (Python package manager)  
- A valid **Groq API Key**

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/HemanthsaiBurla/Translator-App-AI.git
cd translator-app-ai
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root folder and add:

```env
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_flask_secret_key
```

---

## ▶️ Run the App

```bash
python app/app.py
```

Now open your browser and go to:

```
http://127.0.0.1:5000/translator
```

---

## ✨ Usage

- Choose source language and target language  
- Enter text you want to translate  
- Select **Simple** or **Detailed** mode  
- Hit **Translate**  
- Scroll to view previous translations (history saved in session)

---

## 🧠 Translation Modes

- **Simple Mode**: Clean, direct translation  
- **Detailed Mode**: Word-level meaning, usage, and synonyms  

---

## 🖼️ UI Screenshots

Screenshots are located in `translator_images/`

### Home Screen  
![Home Screen](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_HomeScreen_Tran.png)

### Detailed Translation  
![Detailed Translation](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_detail_translation.png)

### Language Switch  
![Language Switch](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Lan_switch.png)

### Copied Translation  
![Copied Translation](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Sharing_Copied_Text.png)

### Translation History  
![Translation History](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Tran_History.png)

### English-Hindi Example  
![En-Hi Translation](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Detail_tran_En-Hi.png)

### Different Language Pair  
![Different Language Pair](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_with_diff_lan.png)


---

## 📦 Technologies Used

- **Python + Flask** – Backend web framework  
- **LangChain + Groq API** – AI-powered translation  
- **HTML/CSS (Jinja2)** – Frontend templates  
- **Flask Session** – Translation history storage  

---

## 🛡️ Security Notes

- API keys are stored in `.env` and ignored by Git  
- `SECRET_KEY` is required for Flask session encryption  

---

## 📃 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Want to improve this translator or extend to more languages/features?  
Feel free to **fork** the repo and submit a **pull request**!

---

## 👨‍💻 Developed By

**Hemanth Sai Burla**  
🌐 Portfolio: [Portfolio](https://hemanthsaiburla.netlify.app)  
💻 GitHub:    [HemanthsaiBurla](https://github.com/HemanthsaiBurla)  
🌐 LinkedIn:  [HemanthSai Burla](https://www.linkedin.com/in/hemanthsaiburla/)  
📬 Email:     hemanthsaiburla@gmail.com  

---

# Contributing
 
 Feel free to submit issues or pull requests to improve this project.
 
 Made with ❤️ by [HemanthSai Burla](https://www.linkedin.com/in/hemanthsaiburla/)
