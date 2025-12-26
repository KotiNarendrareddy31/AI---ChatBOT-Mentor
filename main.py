import streamlit as st
import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from fpdf import FPDF  # Updated: Use modern fpdf2 instead of outdated fpdf
from dotenv import load_dotenv

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="MentorMate AI",
    page_icon="🎓",
    layout="centered"
)

# ---------------- LOAD ENV ----------------
load_dotenv()
HF_TOKEN = os.getenv("hf1")  # Key name in .env

if not HF_TOKEN:
    st.error("❌ HuggingFace API key not found. Please create a file named '.env' with: hf1=your_hf_token")
    st.stop()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #0f172a, #020617);
    }

    .main {
        background-color: transparent;
    }

    h1, h2, h3 {
        color: #f8fafc;
        text-align: center;
    }

    p, label, span {
        color: #e5e7eb;
    }

    .mentor-badge {
        background: linear-gradient(90deg, #6366f1, #22c55e);
        padding: 8px 16px;
        border-radius: 999px;
        display: inline-block;
        color: white;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .stButton > button {
        background: linear-gradient(90deg, #6366f1, #22c55e);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 18px;
        font-weight: 600;
    }

    .stButton > button:hover {
        opacity: 0.9;
        transform: scale(1.02);
    }

    .download-box {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }

    .chat-title {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        color: #e5e7eb;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------
default_param = {
    "module": None,
    "chat_history": [],
    "greeted": False,
    "chat_over": False
}

for key, val in default_param.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ---------------- RESET FUNCTION ----------------
def reset_bot():
    for key, val in default_param.items():
        st.session_state[key] = val
    st.rerun()

# ---------------- HOME PAGE ----------------
if not st.session_state.module:
    st.markdown("<h1>🎓 MentorMate AI</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center;'>Your personalized AI learning mentor</p>",
        unsafe_allow_html=True
    )

    st.markdown("### 📘 Choose Your Learning Path")

    modules = [
        "🐍 Python",
        "🗄️ SQL",
        "📊 Power BI",
        "📈 Exploratory Data Analysis (EDA)",
        "🤖 Machine Learning",
        "🧠 Deep Learning",
        "✨ Gen AI",
        "🕸️ Agentic AI"
    ]

    selected_module = st.selectbox(
        "Select Module",
        modules,
        label_visibility="collapsed"
    )

    if st.button("🚀 Start Mentoring"):
        st.session_state.module = selected_module
        st.session_state.chat_history = []
        st.session_state.greeted = False
        st.session_state.chat_over = False
        st.rerun()

# ---------------- CHAT PAGE ----------------
else:
    module = st.session_state.module

    st.markdown(
        f"""
        <div class="chat-title">🎯 {module} Mentor</div>
        <div style="text-align:center;">
            <span class="mentor-badge">AI Mentor Active</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Initial Greeting
    if not st.session_state.greeted:
        greeting = (
            f"👋 Welcome to **{module} Mentor**!\n\n"
            f"I’m your dedicated AI mentor. Ask me anything related to **{module}**."
        )
        st.session_state.chat_history.append(("Mentor", greeting))
        st.session_state.greeted = True

    # Display Chat History
    for role, msg in st.session_state.chat_history:
        with st.chat_message("assistant" if role == "Mentor" else "user"):
            st.markdown(msg)

    # Chat Input
    if not st.session_state.chat_over:
        user_input = st.chat_input("💬 Ask your question (type 'exit' to end)")

        if user_input:
            with st.chat_message("user"):
                st.markdown(user_input)

            st.session_state.chat_history.append(("Student", user_input))

            if user_input.lower().strip() == "exit":
                farewell = "👋 **Session ended.** You can now download your conversation."
                st.session_state.chat_history.append(("Mentor", farewell))
                st.session_state.chat_over = True
                st.rerun()

            with st.chat_message("assistant"):
                with st.spinner("🤔 Mentor is thinking..."):
                    # Updated model: Latest high-performance 70B (released Dec 6, 2024) – gated but excellent
                    # Accept the license on HF page first: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
                    llm_endpoint = HuggingFaceEndpoint(
                        repo_id="meta-llama/Llama-3.3-70B-Instruct",
                        task="text-generation",
                        temperature=0.6,
                        max_new_tokens=1024,  # Increased for longer responses
                        repetition_penalty=1.1,
                    )

                    llm = ChatHuggingFace(llm=llm_endpoint)

                    prompt = ChatPromptTemplate.from_messages([
                        SystemMessagePromptTemplate.from_template(f"""
                        You are a professional AI mentor specializing in {module}.
                        Rules:
                        1. Answer ONLY {module} related questions.
                        2. If unrelated, reply exactly:
                        "Sorry, I don’t know about this question. Please ask something related to {module}."
                        3. Be clear, structured, concise, and friendly.
                        4. Use markdown for code/examples when relevant.
                        """),
                        HumanMessagePromptTemplate.from_template("{query}")
                    ])

                    response = llm.invoke(
                        prompt.format_messages(query=user_input)
                    ).content

                    st.markdown(response)

            st.session_state.chat_history.append(("Mentor", response))

    # ---------------- DOWNLOAD SECTION ----------------
    if st.session_state.chat_over:
        st.markdown(
            """
            <div class="download-box">
            <h3>📥 Download Your Conversation</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        chat_text = "\n\n".join(f"**{r}:** {m}" for r, m in st.session_state.chat_history)

        st.download_button(
            "📄 Download as TXT",
            chat_text,
            file_name=f"{module.replace(' ', '_')}_Mentor_Chat.txt",
            mime="text/plain"
        )

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Helvetica", size=12)  # Better default font
        for line in chat_text.split("\n"):
            pdf.multi_cell(0, 8, line.encode('latin-1', 'replace').decode('latin-1'))

        pdf_bytes = pdf.output(dest="S")

        st.download_button(
            "📑 Download as PDF",
            pdf_bytes,
            file_name=f"{module.replace(' ', '_')}_Mentor_Chat.pdf",
            mime="application/pdf"
        )

        if st.button("🔙 Back to Home"):
            reset_bot()