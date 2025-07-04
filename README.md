# GitHub AI Recommender Agent with Google Gemini + ADK

This project demonstrates how to build an intelligent AI agent that recommends trending GitHub repositories based on user input — using **Google Gemini** for embeddings and planning, and **Google ADK** for memory and tool management.

## 🔍 Use Case

The agent takes a natural language prompt like:

> "I'm looking for trending AI projects on computer vision"

It then:
1. Fetches trending GitHub repositories (using a public API)
2. Embeds their descriptions using Google Gemini
3. Stores them in a local in-memory vector DB
4. Uses a Gemini-powered planner + ADK to respond with the best matches

---

## 🛠️ Stack

| Component | Purpose |
|----------|---------|
| Google Gemini API | Embeddings + Planning |
| Google ADK         | Agent, Planner, Memory, Toolset |
| GitHub Trending API | Repository source |
| Python              | Implementation language |

---

## 📁 Project Structure

```
github-gemini-agent/
├── agent.py              # Main agent logic
├── github_fetcher.py     # Fetches trending GitHub repos
├── vector_store.py       # Local vector embedding + search
├── config.py             # Loads Gemini API key
├── .env.example          # Env variable template
├── requirements.txt      # Dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/github-gemini-agent.git
cd github-gemini-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_api_key
```

---

## 🚀 Run the Agent

```bash
python agent.py
```

Example prompt:

```
What are the best reinforcement learning projects on GitHub?
```

Sample output:

```
OpenAI Baselines: https://github.com/openai/baselines
Facebook ELF: https://github.com/facebookresearch/ELF
Ray RLlib: https://github.com/ray-project/ray
```

---

## 🧠 How It Works

- Uses Gemini's `embedding-001` model to embed repo descriptions
- Uses ADK's `GeminiPlanner` to interpret your query
- Matches your intent to embedded repo metadata using cosine similarity
- Recommends top 3 matching GitHub repos via ADK tools

---

## 📌 Requirements

- Python ≥ 3.9
- Google Gemini API access
- Internet access to fetch trending repositories

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙋‍♀️ Author

**Puspanjali Sarma**

Connect on [LinkedIn](https://www.linkedin.com/in/puspanjali-sarma/) | Twitter | Medium

---

## ⭐️ If you find this useful...

Give the project a ⭐️ on GitHub and share it with your community!
