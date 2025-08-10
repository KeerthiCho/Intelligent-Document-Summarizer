# Intelligent-Document-Summarizer
AI-powered summarization tool that condenses text from local files or web URLs using state-of-the-art NLP models. Built with Python, Hugging Face Transformers, and Newspaper3k, supporting adjustable summary lengths for quick content understanding.
Alright — here’s your **complete README.md** with everything (description, usage, requirements, .gitignore note, and license info) so you can just copy–paste into PyCharm and commit.

---

````markdown
# 📝 Intelligent Document Summarizer

An **AI-powered summarization tool** that condenses text from **local files** or **web URLs** using state-of-the-art NLP models.  
Built with **Python**, **Hugging Face Transformers**, and **Newspaper3k**, supporting adjustable summary lengths for quick content understanding.

---

## 🚀 Features
- 📂 Summarizes text from `.txt` files or web URLs
- 📏 Adjustable summary length: short, medium, long
- 🤖 Uses **BART-large-CNN** model from Hugging Face
- 🌐 Supports most major news and article sites
- ⚡ Lightweight & fast

---

## 📦 Installation
```bash
git clone https://github.com/<your-username>/intelligent-document-summarizer.git
cd intelligent-document-summarizer
python -m venv .venv
# Activate virtual environment:
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
````

---

## 🛠 Usage

**Summarize from a local file:**

```bash
python main.py file data/sample_text.txt --length medium
```

**Summarize from a URL:**

```bash
python main.py url "https://www.bbc.com/news/science-environment-56837908" --length short
```

---

## 📂 Project Structure

```
intelligent-document-summarizer/
├── data/
│   └── sample_text.txt
├── src/
│   └── summarizer/
│       ├── utils.py
│       └── summarize.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🧠 Model

Uses the [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) model for abstractive summarization,
which generates summaries that are both **concise** and **coherent**.

---

## 📜 Requirements

See `requirements.txt` for the complete list:

```txt
transformers==4.44.0
torch>=2.0.0
newspaper3k==0.2.8
lxml==5.2.1
lxml_html_clean==0.2.0
requests==2.32.3
```

---

## 🛡 .gitignore

The `.gitignore` file ensures unnecessary files (virtual environments, cache, IDE configs) are not pushed to GitHub.

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Environment
.env
.venv/
env/
venv/

# PyCharm
.idea/

# OS
.DS_Store
Thumbs.db

# Cache
.cache/
```

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it.
See the [LICENSE](LICENSE) file for details.

---

## 🏷 GitHub Tags

```
python, nlp, ai, machine-learning, text-summarization, huggingface, transformers, newspaper3k
```
```
