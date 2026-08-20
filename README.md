# 🤖 AI Study Agent

An intelligent **Agentic AI Study Assistant** built with **Google Gemini** and **Streamlit**. The system helps students learn more effectively by answering questions, solving mathematical problems, searching study material, and generating practice quizzes.

---

## 🚀 Features

- 🤖 **AI Study Assistant**
  - Ask questions and receive intelligent explanations.
  - Powered by Google Gemini.

- 🧮 **Smart Calculator**
  - Solve mathematical and numerical problems.

- 📚 **Knowledge Search**
  - Search and retrieve information from study material.

- 📝 **Quiz Generator**
  - Generate practice MCQs for exam preparation.

- 💬 **Interactive Chat Interface**
  - Conversational AI interface built with Streamlit.

- 🎨 **Modern UI**
  - Dark glassmorphism interface.
  - Custom background image.
  - Responsive sidebar and feature cards.

- 🔐 **Environment-based API Configuration**
  - API credentials are stored in `.env`.
  - Sensitive credentials are excluded from GitHub.

---

## 🧠 System Architecture

```text
                    ┌─────────────────────┐
                    │       Student       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │    Chat Interface   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   AI Study Agent    │
                    │    Agent Logic      │
                    └──────────┬──────────┘
                               │
                  ┌────────────┼────────────┐
                  │            │            │
                  ▼            ▼            ▼
             Calculator   Knowledge      Quiz
                            Search       Generator
                  │            │            │
                  └────────────┼────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Gemini LLM       │
                    │  Google Generative  │
                    │        AI           │
                    └─────────────────────┘
