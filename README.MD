# 🧠 Smart AI Research Assistant

An intelligent GenAI-powered web app that helps users understand, summarize, and test their knowledge on research papers. Just upload a PDF or TXT file, and let the assistant summarize the content, answer your questions, and challenge you with logic-based questions — all powered by Gemini Flash.

---

## 🚀 Features

- 📤 Upload **PDF** or **TXT** files
- 📝 Get a **150-word AI-generated summary**
- ❓ **Ask Anything** about the document — with contextual answers + source snippets
- 🧩 **Challenge Me Mode** — auto-generated logic-based questions with feedback
- 💬 **Memory-aware Q&A** — ask follow-up questions with chat context
- 📌 View supporting **document snippets**
- 🧠 View and clear previous Q&A history
- 💻 Clean, responsive **Streamlit UI** with spinners and sectioned layout
- 🔐 API integration with **Gemini Flash (Google)** using `.env` key

---

## 📂 Project Structure

```bash
genai-assistant/
├── app/
│   └── main.py                 # Streamlit UI
├── backend/
│   ├── document_parser.py      # PDF/TXT reader
│   ├── qa_engine.py            # Ask Anything logic
│   └── question_generator.py   # Challenge evaluation
├── models/
│   └── gemini_wrapper.py       # Gemini API integration
├── .streamlit/
│   └── config.toml             # Custom UI theme
├── .env                        # API key (not committed)
├── requirements.txt            # Dependencies
└── README.md                   # You're here

⚙️ Setup Instructions
✅ Step 1: Clone the Repo
git clone https://github.com/yourusername/genai-assistant.git
cd genai-assistant

✅ Step 2: Create Virtual Environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

✅ Step 3: Install Dependencies
pip install -r requirements.txt

✅ Step 4: Add .env File
Create a .env file in the root:
GEMINI_API_KEY=your_actual_gemini_api_key_here

✅ Step 5: Run the App
streamlit run app/main.py
