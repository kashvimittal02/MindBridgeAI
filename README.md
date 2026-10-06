# 🧠 MindBridge AI

MindBridge AI is a Retrieval-Augmented Generation (RAG) chatbot designed to provide mental health information from a custom knowledge base. The chatbot combines Google's Gemini API with ChromaDB vector search to retrieve relevant information from uploaded PDF documents before generating a response.

---

## ✨ Features

- 🤖 Gemini 2.5 Flash powered chatbot
- 💬 Conversation memory
- 📄 PDF document ingestion
- ✂️ Recursive text chunking
- 🔍 Semantic search using embeddings
- 🗂️ ChromaDB vector database
- 📚 Retrieval-Augmented Generation (RAG)
- 🧩 Modular object-oriented architecture

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- ChromaDB
- PyMuPDF
- LangChain Text Splitters
- python-dotenv

---

## 📂 Project Structure

```
MindBridgeAI/
│
├── app.py
├── chatbot.py
├── config.py
├── memory.py
├── prompts.py
├── requirements.txt
│
├── documents/
│   └── MindBridge_Test_Document.pdf
│
├── RAG/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vectordb.py
│   ├── retriever.py
│   └── prompt_builder.py
│
└── .gitignore
```

---

## ⚙️ How It Works

1. Load a PDF document.
2. Extract text using PyMuPDF.
3. Split the text into overlapping chunks.
4. Generate embeddings for each chunk using Gemini Embeddings.
5. Store the embeddings in ChromaDB.
6. Embed the user's question.
7. Retrieve the most relevant chunks from the vector database.
8. Combine:
   - System Prompt
   - Conversation History
   - Retrieved Context
   - User Question
9. Send the final prompt to Gemini.
10. Return the generated response and update conversation memory.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/MindBridgeAI.git
cd MindBridgeAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Running the Project

Start the chatbot:

```bash
python app.py
```

---

## 💡 Example Questions

```
What is mental health?

How can stress be reduced?

What are the symptoms of anxiety?

When should someone seek professional help?
```

---

