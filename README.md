# 🧠 LangChain Chatbot using Gemma 2B (Ollama + Streamlit)

A lightweight, local-first **Generative AI chatbot** powered by [Google’s Gemma 2B model](https://ai.google.dev/gemma), built using **LangChain**, **Ollama**, and **Streamlit**.

> ⚡ Perfect for developers with limited computing resources – no OpenAI key or cloud GPU required!

---

## 🚀 Features

- ✅ Ask any question through a clean **Streamlit UI**
- ✅ Get AI-generated responses **locally** using the **Gemma 2B** model
- ✅ Powered by **LangChain** for prompt orchestration and chaining
- ✅ Designed to work on **low-end systems** (8–16 GB RAM)
- ✅ **No cloud dependency** – runs completely offline after setup

---

## 🧠 About Gemma 2B

[Gemma](https://ai.google.dev/gemma) is a family of open-source, lightweight models developed by Google.  
This app uses the **Gemma 2B** variant, which:

- Is optimized for CPUs and small GPUs
- Runs efficiently on local machines
- Offers fast and meaningful responses for everyday questions
- Can be hosted with **[Ollama](https://ollama.com/)** locally

---

## 🧰 Tech Stack

| Tool         | Description                       |
|--------------|------------------------------------|
| 🦜 LangChain  | Prompt handling and chaining       |
| 🧠 Gemma 2B   | Lightweight LLM (via Ollama)       |
| 📦 Ollama     | Local model runner for Gemma       |
| 🌐 Streamlit  | Frontend interface for interaction |
| 🐍 Python     | Core programming language          |

---
````markdown

 🖥️ Prerequisites

- Python 3.9+
- [Ollama installed](https://ollama.com)
- Pull the Gemma 2B model:

```bash
ollama pull gemma:2b
````

---

## ⚙️ Installation & Setup

1. **Clone this repository**:

```bash
git clone https://github.com/KartikNimhan/Gemma2-Application-GenAI-.git
cd Gemma2-Application-GenAI-
```

2. **Create a virtual environment** (recommended):

```bash
python -m venv venv
```

Activate it:

```bash
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Start Ollama in a new terminal**:

```bash
ollama serve
ollama run gemma:2b
```

5. **Run the Streamlit app**:

```bash
streamlit run app.py
```

---

## 🌐 Environment Variables

Create a `.env` file in your project directory with:

```env
OPENAI_API_KEY=dummy_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=GemmaChat
```

> 💡 `OPENAI_API_KEY` is just a dummy value – it's not used when running locally with Ollama.

---

## 🧪 Sample Questions

Try asking:

* What is Generative AI?
* How does LangChain work?
* Who was Alan Turing?

---

## 📸 Screenshot

![Image](https://github.com/user-attachments/assets/39be4d73-3a89-429e-a372-9bad12db9fa8)

---

## 🔮 Future Enhancements

* 📄 Add document ingestion (PDF, TXT)
* 🔍 Implement vector-based retrieval (RAG)
* 🤖 Add model selector (Gemma, Mistral, LLaMA, etc.)
* 🧠 Add conversation memory

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙋‍♂️ Author

**Kartik Nimhan**
Machine Learning & GenAI Enthusiast
[GitHub Profile](https://github.com/KartikNimhan)

````

