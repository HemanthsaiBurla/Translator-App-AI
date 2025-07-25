# Translator-App-AI
# 🌐 Multi-Language Translator App (English ↔ Telugu ↔ Hindi + More)

This is a **simple and clean web-based translation tool** built using **Python (Flask)**. It supports **text translation** through **LangChain**, powered by **Groq API** and **OpenAI API**.

Users can **instantly translate** text between **multiple languages** including **English**, **Telugu**, **Hindi**, and up to **10 other languages**

> 💡 Offers both **Instant Translation** for quick results and **Detailed Translation** to get word meanings, usage, and synonyms.

## 🌐 Live Demo
**🔗 Live URL:** `https://translator-app-ai.onrender.com/translator`  
or  
**🔗 Live Translator** [Click Here](https://translator-app-ai.onrender.com/translator)

---

## 🔥 Features

- 🎯 **Direct Translation** (No login or registration)  
- 🔁 **Language Selection** (English ↔ Telugu ↔ Hindi + Up to 10 languages)  
- 🧠 **Simple & Detailed Modes** (Word meanings, usage, synonyms)  
- 🧾 **Translation History** (Last 10 searches stored)  
- 🌐 Powered by **LangChain + Groq API**  
- 💡 Clean UI with HTML + CSS  
- 🚀 **Deployed on Render.com** (Always accessible)
- 💡 **Added additional buttons like copy, share, cleary history and clear input**
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
├── .env                             # Environment variables (local)
├── requirements.txt                 # Project dependencies
├── runtime.txt                      # Python version for Render
├── load_api_key.ipynb               # API key test/setup (optional)
├── .gitignore                       # Files to ignore in Git
└── README.md                        # This file
```

---

## ✅ Prerequisites

- Python 3.8+  
- pip (Python package manager)  
- A valid **Groq API Key** ([Get it here](https://console.groq.com))
- **Render.com account** (for deployment)

---

## 🚀 Local Development Setup

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

### 5. Run the App Locally

```bash
python app/app.py
```

Now open your browser(chrome or any) and go to:
```
http://127.0.0.1:5000/translator
```

---

## 🌐 Deploy to Render.com

### Step 1: Prepare for Deployment

Create `requirements.txt` with these dependencies:
```txt
Flask==2.3.3
python-dotenv==1.0.0
langchain==0.0.340
groq==0.4.1
openai==1.3.0
gunicorn==21.2.0
Werkzeug==2.3.7
```

Create `runtime.txt` (optional):
```txt
python-3.11.0
```

### Step 2: Deploy on Render.com

1. **Sign up** at [Render.com](https://render.com)
2. **Connect GitHub** → Select your repository
3. **Configure settings:**
   ```bash
   Name: translator-app-ai
   Region: Oregon (US West) or Singapore (for India)
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python app/app.py or gunicorn --bind 0.0.0.0:$PORT app.app:app
   ```

### Step 3: Add Environment Variables

In Render Dashboard → Your Service → Environment:
```env
GROQ_API_KEY=your_groq_api_key_here
#### Optional:
SECRET_KEY=your_flask_secret_key_here
FLASK_ENV=production
```

### Step 4: Deploy & Access

- Click **"Create Web Service"**
- Wait for deployment (5-10 minutes)
- Access your app at: `https://translator-app-ai.onrender.com/translator`

---

## ⚡ Keep Your App Active (Important!)

### 🚨 **Free Tier Limitation:**
- App **sleeps after 15 minutes** of inactivity
- Takes **30+ seconds** to wake up

### 💡 **Solutions:**

#### Option 1: Upgrade to Starter Plan ($7/month)
- ✅ Always-on service (recommended)
- ✅ No sleep, no cold starts
- ✅ Better performance

#### Option 2: Use Free Monitoring Tools

**UptimeRobot (Recommended)**
1. Sign up at [UptimeRobot.com](https://followupthen.com)
2. Add your Render URL
3. Set check interval: **5 hours or 15 days**
4. Free plan: 50 monitors

**Cron-job.org**
1. Visit [Cron-job.org](https://cron-job.org)
2. Create job to ping every **10 minutes or any**
3. URL: `https://translator-app-ai.onrender.com/translator`

---

## ✨ Usage

1. **Choose Languages**: Select source and target languages
2. **Enter Text**: Type or paste text to translate
3. **Select Mode**: 
   - **Simple**: Quick, direct translation
   - **Detailed**: Word meanings, usage, synonyms
4. **Translate**: Click translate button
5. **View History**: Scroll down to see previous translations
---

## 🖼️ UI Screenshots

Screenshots are located in `translator_images/`

### Home Screen  
![Home Screen](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_HomeScreen_Tran.png)

### Detailed Translation  
![Detailed Translation](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_detail_translation.png)

### Language Switch  
![Language Switch](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Lan_switch.png)

### Translation History  
![Translation History](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Tran_History.png)

### English-Hindi Example  
![En-Hi Translation](https://github.com/HemanthsaiBurla/Translator-App-AI/blob/main/translator_images/T_Detail_tran_En-Hi.png)

---

## 📦 Technologies Used

- **Python + Flask** – Backend web framework  
- **LangChain + Groq API** – AI-powered translation  
- **HTML/CSS** – Frontend templates  
- **Flask Session** – Translation history storage
- **Render.com** – Cloud deployment platform
- **Gunicorn** – WSGI HTTP Server

---

## 🛠️ Troubleshooting

### Common Issues:

**App won't start on Render:**
```python
# Ensure app.py has:
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

**Environment variables not working:**
```python
# Add to app.py:
import os
from dotenv import load_dotenv

load_dotenv()  # For local development
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

**App sleeping too often:**
- Set up UptimeRobot monitoring
- Consider upgrading to Starter plan

---

## 🛡️ Security Notes

- API keys are stored in `.env` and ignored by Git  
- `SECRET_KEY` is required for Flask session encryption
- Environment variables are secure on Render.com
- HTTPS enabled by default on Render

---

## 💰 Cost Information

### Free Tier:
- ✅ 744 hours/month (≈31 days)
- ❌ Sleeps after 15 minutes
- ❌ Cold start delays

### Starter Plan ($7/month):
- ✅ Always-on service
- ✅ No sleep/cold starts
- ✅ Custom domains
- ✅ Better performance

---

## 📝 Quick Setup Checklist

**Local Development:**
- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Install dependencies(requirements.txt*)
- [ ] Set up `.env` file
- [ ] Get Groq API key
- [ ] Run `python app/app.py`

**Deployment:**
- [ ] Push code to GitHub
- [ ] Create Render account
- [ ] Connect GitHub repository
- [ ] Configure build settings
- [ ] Add environment variables
- [ ] Deploy and test
- [ ] Set up uptime monitoring (optional)

---

## 🤝 Contributing

Want to improve this translator or add more features?  
Feel free to **fork** the repo and submit a **pull request**!

**Ideas for contribution:**
- Add more languages
- Improve UI/UX
- Add voice translation
- Implement caching
- Mobile app version

---

## 📃 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Developed By

**Hemanth Sai Burla**  
🌐 **Portfolio:** [hemanthsaiburla.netlify.app](https://hemanthsaiburla.netlify.app)  
💻 **GitHub:** [HemanthsaiBurla](https://github.com/HemanthsaiBurla)  
🌐 **LinkedIn:** [HemanthSai Burla](https://www.linkedin.com/in/hemanthsaiburla/)  
📬 **Email:** hemanthsaiburla@gmail.com

---

## 🆘 Support

Having issues? Here's how to get help:

1. **Check the troubleshooting section** above  
2. **Create an issue** on GitHub  
3. **Contact me** via email or LinkedIn  
4. **Check Render documentation** at [docs.render.com](https://docs.render.com)

---

## ⭐ Show Your Support

If this project helped you:
- ⭐ **Star the repository**
- 🍴 **Fork for your projects**  
- 📢 **Share with friends**
- 🐛 **Report bugs or suggest features**

---

*Made with ❤️ by [HemanthSai Burla](https://www.linkedin.com/in/hemanthsaiburla/) | Deployed with 🚀 on Render.com*

**Last Updated:** July 2025
