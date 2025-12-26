
# 🎓 AI Chat Bot Mentor (MentorMate AI)

**MentorMate AI** is an interactive **AI-powered learning mentor** built with **Streamlit**, **LangChain**, and **Hugging Face LLMs**.
It provides **module-specific mentoring** in areas like Python, SQL, Machine Learning, Deep Learning, GenAI, and more.

Users can chat with a dedicated AI mentor, receive structured explanations, and **download their learning conversations as TXT or PDF**.

---

## ✨ Features

* 🤖 AI-powered personal learning mentor
* 📘 Module-specific mentoring:

  * 🐍 Python
  * 🗄️ SQL
  * 📊 Power BI
  * 📈 Exploratory Data Analysis (EDA)
  * 🤖 Machine Learning
  * 🧠 Deep Learning
  * ✨ Generative AI
  * 🕸️ Agentic AI
* 🧠 Smart prompt control (answers only module-related questions)
* 💬 Chat-style interactive UI
* 📄 Download conversation as **TXT**
* 📑 Export full chat as **PDF**
* 🎨 Modern dark-themed UI with custom CSS
* 🔐 Secure API key handling via `.env`

---

## 🛠️ Tech Stack

* **Frontend / UI:** Streamlit
* **LLM:** Meta LLaMA 3.3 (70B Instruct)
* **AI Framework:** LangChain
* **LLM Provider:** Hugging Face Inference API
* **Language:** Python
* **Utilities:** PDF export, environment management

---

## 📂 Project Structure

```
AI-ChatBot-Mentor/
│
├── main.py          # Main Streamlit application
├── req.txt          # Python dependencies
├── .env             # Hugging Face API token (ignored by git)
└── README.md        # Project documentation
```

---

## 🔑 Prerequisites

* Python **3.9+**
* Hugging Face account
* Hugging Face API token
* Internet connection

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-chatbot-mentor.git
cd ai-chatbot-mentor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv AI
```

Activate it:

**Windows (PowerShell)**

```powershell
AI\Scripts\Activate.ps1
```

**Windows (CMD)**

```bash
AI\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r req.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
hf1=your_huggingface_api_token_here
```

⚠️ **Never commit `.env` to GitHub**

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

The app will open automatically in your browser.

---

## 🧠 How It Works

1. User selects a learning module
2. AI mentor is initialized for that module
3. User asks questions via chat
4. AI responds using **LLaMA 3.3 70B**
5. Conversation is stored in session
6. User can download chat as TXT or PDF

---

## 🔐 Security & Privacy

* API key loaded securely from `.env`
* No chat data is stored permanently
* Session-based interaction only

---

## 🚀 Future Enhancements

* 🧪 Quiz mode & assessments
* 🧭 Learning roadmap generation
* 🧑‍🏫 Difficulty-level selection (Beginner → Advanced)
* 🎙️ Voice-based mentor
* ☁️ Cloud deployment (Streamlit Cloud / Hugging Face Spaces)

---



## 🤝 Contributing

Contributions are welcome!
Fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Narendra Reddy Kotireddy**
🎓 B.Tech CSE (2023)
🎯 Aspiring AI/ML Engineer
🔗 [LinkedIn](https://www.linkedin.com/in/kotireddy-narendra-reddy-5105301a6)


