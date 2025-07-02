# Gemma2-Application-GenAI

Sure! Here's a complete and clean `README.md` file for your project that explains what it does, how it works locally with a lightweight model (Gemma), and how to set it up:

---

````markdown
# 🧠 LangChain Chatbot using Gemma 2B (Ollama + Streamlit)

A lightweight, local-first **Generative AI chatbot** powered by [Google’s Gemma 2B model](https://ai.google.dev/gemma), built using **LangChain**, **Ollama**, and **Streamlit**.

> ⚡️ Perfect for developers with limited computing resources – no OpenAI key or cloud GPU required!

---

## 🚀 Features

✅ Ask any question through a simple **Streamlit UI**  
✅ Get AI responses generated **locally** via the **Gemma 2B** model  
✅ Powered by **LangChain** for prompt orchestration  
✅ Works even on low-end systems (8–16 GB RAM)  
✅ Runs entirely offline after setup

---

## 🧠 About Gemma 2B

[Gemma](https://ai.google.dev/gemma) is a family of open, lightweight models released by Google.

We use the **Gemma 2B** model because:
- It's optimized for **CPU and low-end GPU** environments.
- It’s efficient and fast for real-time queries.
- It can be run locally using **Ollama** with just one command.

---

## 🧰 Tech Stack

| Tool         | Purpose                        |
|--------------|--------------------------------|
| 🦜 LangChain  | Prompt management & chaining   |
| 🧠 Gemma 2B   | Lightweight LLM (via Ollama)   |
| 📦 Ollama     | Local model inference engine   |
| 🌐 Streamlit  | Frontend for chat interface    |
| 🐍 Python     | Core language (3.9+)           |

---

## 🖥️ Prerequisites

Make sure you have:

- **Python 3.9+** installed
- **Ollama** installed → [https://ollama.com](https://ollama.com)
- The **Gemma 2B model** pulled locally:

```bash
ollama pull gemma:2b


---

## ⚙️ Installation & Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/KartikNimhan/Gemma2-Application-GenAI-.git
   cd Gemma2-Application-GenAI-
   ```

2. **Create Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama (in another terminal)**:

   ```bash
   ollama serve
   ollama run gemma:2b
   ```

5. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Environment Variables

Create a `.env` file with the following (if using LangSmith tracking):

```env
OPENAI_API_KEY=your_dummy_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=GemmaChat
```

> ℹ️ You don’t need a real OpenAI key unless you're integrating OpenAI-based models. Ollama runs locally.

---

## ✅ Features

* 💬 Ask any question and get AI-generated answers
* 🧱 Modular LangChain architecture
* ⚡ Fast and local: No cloud APIs required
* 🖼️ Clean Streamlit UI for interaction

---

## 📷 Screenshot

![App Screenshot](https://user-images.githubusercontent.com/placeholder/app_screenshot.png)

---

## 🧪 Example Questions

* What is Generative AI?
* How does LangChain work?
* Who is Alan Turing?

---

## 🛠️ Future Improvements

* Add PDF/document ingestion
* Add retrieval-based QA with vector store
* Add model selector (Gemma, LLaMA, Mistral, etc.)

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Kartik Nimhan**
ML & GenAI Enthusiast | [GitHub](https://github.com/KartikNimhan)

---

```

```
