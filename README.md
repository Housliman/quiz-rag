# 📄 PDF Quiz Generator (RAG-Powered)

An AI-powered web application that transforms any PDF document into an interactive multiple-choice quiz. Built with Python, Streamlit, and the latest Llama 3 models via Groq.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-f55036?style=for-the-badge)

## 🚀 Key Features
- **Smart PDF Processing:** Automatically extracts and chunks text using LangChain's `RecursiveCharacterTextSplitter`.
- **Local Embeddings:** Uses `sentence-transformers/all-MiniLM-L6-v2` (running on CPU) for fast, private, and free vector embeddings.
- **High-Performance RAG:** Leverages **FAISS** for efficient similarity search to provide the LLM with relevant context.
- **Advanced LLM:** Powered by **Llama 3.3 70B Versatile** on Groq for high-quality question generation.
- **Interactive UI:** A polished Streamlit interface for uploading PDFs, taking quizzes, and reviewing detailed explanations.

## 🛠️ Tech Stack
- **UI:** [Streamlit](https://streamlit.io/)
- **Orchestration:** [LangChain](https://www.langchain.com/)
- **Vector DB:** [FAISS](https://github.com/facebookresearch/faiss)
- **Model Provider:** [Groq Cloud](https://console.groq.com/)
- **Embedding Model:** `all-MiniLM-L6-v2` (HuggingFace)

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- A Groq API Key ([Get one here](https://console.groq.com/keys))

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/quiz-rag.git
cd quiz-rag
```

### 3. Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 🎮 How to Use
1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. **Upload** your PDF in the sidebar.
3. **Select** the number of questions (5 to 15).
4. Click **"Generate Quiz"**.
5. **Answer** the questions and click "Submit" to see your score and detailed explanations for every answer.

## 📁 Project Structure
- `app.py`: Streamlit UI and state management.
- `rag.py`: PDF processing, embedding logic, and vector search.
- `quiz.py`: Groq API integration and quiz data parsing.
- `prompts.py`: Custom-engineered prompt for structured JSON generation.
- `requirements.txt`: Python dependencies.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
