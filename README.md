# 🤖 Smart Text Summarizer API

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)
![Cloud](https://img.shields.io/badge/Deployed-Render-purple.svg)

An AI-powered REST API that summarizes long texts using Facebook's **BART-large-CNN** model from HuggingFace Transformers. Built with FastAPI and deployed on cloud.

---

## 🚀 Live Demo
> API Base URL: `https://smart-text-summarizer.onrender.com`

---

## 📌 Features
- Summarizes long articles, research papers, and documents
- Returns word count comparison (original vs summary)
- Clean REST API with auto-generated docs
- Deployed on cloud (free tier)

---

## 🛠️ Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Core language |
| FastAPI | REST API framework |
| HuggingFace Transformers | BART summarization model |
| Render | Cloud deployment |

---

## 📂 Project Structure
```
smart-text-summarizer/
│
├── app.py              # FastAPI application
├── model.py            # HuggingFace model wrapper
├── requirements.txt    # Dependencies
├── render.yaml         # Cloud deployment config
└── README.md           # Project documentation
```

---

## ⚙️ API Endpoints

### `GET /`
Returns API status.

### `POST /summarize`
Summarizes the input text.

**Request Body:**
```json
{
  "text": "Your long text here...",
  "max_length": 130,
  "min_length": 30
}
```

**Response:**
```json
{
  "original_text": "Your long text here...",
  "summary": "AI generated summary...",
  "original_word_count": 200,
  "summary_word_count": 45
}
```

---

## 🧠 How It Works
1. User sends a POST request with long text
2. BART model processes and understands the text
3. API returns a concise AI-generated summary

---

## 👨‍💻 Author
Made for academic GA/TA applications — demonstrating AI + Cloud skills.
