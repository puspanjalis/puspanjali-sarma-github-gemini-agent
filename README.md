# 🤖 GitHub Recommender AI Agent using Google Gemini + ADK

Build an intelligent AI agent that recommends trending GitHub projects tailored to your interests using Google's Gemini API and Agent Development Kit (ADK).

> This project demonstrates hands-on use of Google's LLM stack, vector embeddings, agentic planning, and external tool chaining — part of my Google Developer Expert (GDE) application in AI/ML.

---

## 🌟 Features

- 💬 Accepts natural language queries like:  
  *“Show me trending projects in reinforcement learning”*

- 🔍 Fetches GitHub trending repositories

- 🧠 Embeds repo descriptions using **Gemini Embeddings**

- 📊 Stores embeddings in a lightweight **in-memory vector DB**

- 🎯 Returns intelligent, ranked recommendations using cosine similarity

---

## 📦 Tech Stack

| Component           | Description                                |
|--------------------|--------------------------------------------|
| Google Gemini API  | LLM and embedding generation               |
| Google ADK         | Agent planner, memory, and tool interface  |
| GitHub REST API    | Trending repository data                   |
| Numpy              | Embedding similarity scoring               |
| Python             | Orchestration and logic                    |

---

## 🚀 Quick Start

### Clone the Repo

```bash
git clone https://github.com/puspanjali-sarma/github-gemini-agent.git
cd github-gemini-agent
```
---

### Roadmap
 - Add user profiles for personalized history
 - Deploy as Streamlit web UI
 - Integrate GitHub GraphQL API
 - Store feedback to improve relevance over time

### Related Blog
Build a GitHub Recommender AI Agent Using Google Gemini and ADK

## 🤝 Contributions
Pull requests welcome! Please open an issue to discuss improvements or bugs. Drop a message [here](https://www.linkedin.com/in/puspanjalisarma/)
  


