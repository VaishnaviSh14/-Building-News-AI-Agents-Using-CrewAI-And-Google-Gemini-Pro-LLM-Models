# 📰 AI News Agents with CrewAI & Google Gemini Pro

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)
![CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange)
![LLM](https://img.shields.io/badge/Model-Google%20Gemini%20Pro%201.5-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-blueviolet)

> 🚀 **Automated News Research & Writing** using multi-agent AI, CrewAI framework, and Google Gemini LLM.

---

## 📌 Overview
This project builds an **AI-powered News Research & Writing System** using **CrewAI** and **Google Gemini Pro (1.5 Flash)** LLM models.  
It features two autonomous agents – a **Senior Researcher** and a **Writer** – who collaborate to research trending topics, analyze insights, and generate well-structured news blog posts.  
The system uses **Serper API** for real-time web search and outputs a **ready-to-publish blog post**.

---

## 🏗️ Project Structure
```bash
📂 News-AI-Agents
 ├── agents.py            # Defines Researcher & Writer agents
 ├── crew.py              # Creates Crew & orchestrates workflow
 ├── tasks.py             # Defines tasks for research & writing
 ├── tools.py             # Initializes Serper API search tool
 ├── .env                 # Stores API keys (Google & Serper)
 └── news_blog_post.txt   # Output blog file (generated)
```

⚙️ Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/news-ai-agents.git

cd news-ai-agents

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file in the root directory and add:

GOOGLE_API_KEY=your_google_api_key

SERPER_API_KEY=your_serper_api_key

4️⃣ Run the Project

python crew.py

✅ Output: A news_blog_post.txt file will be generated with a ready-to-publish blog post.

| Tool / Library        | Purpose                    |
| --------------------- | -------------------------- |
| **Python 3.10+**      | Programming Language       |
| **CrewAI**            | Multi-Agent Orchestration  |
| **Google Gemini Pro** | LLM for research & writing |
| **Serper API**        | Real-time Web Search       |
| **dotenv**            | Secure API Key Management  |


## 📊 Example Output
## Sample Blog Post Generated

Title: The AI Revolution in Healthcare: Generative AI Takes Center Stage

Artificial intelligence (AI) is rapidly transforming the healthcare landscape, and the latest wave of innovation is driven by generative AI.
This powerful technology is poised to revolutionize drug discovery, personalize medicine, and enhance patient care in unprecedented ways.

Highlights:

⚡ Accelerated Drug Discovery – Rapidly generates and evaluates drug candidates

🧬 Personalized Medicine – Tailors treatment to individual patient profiles

🩺 Improved Diagnostics – Detects subtle patterns early in medical imaging

🔍 Ethical Considerations – Data bias, privacy, transparency & regulation


## 📸 Output Screenshots
<img width="1513" height="891" alt="image" src="https://github.com/user-attachments/assets/e4df2bc5-5f1d-4d4b-b5b9-b17301558d8a" /> <img width="1392" height="892" alt="image" src="https://github.com/user-attachments/assets/becc3fd5-f6fc-466b-9dab-acc8dcc7532e" />

🌟 Don't forget to ⭐ this repo if you like it!
