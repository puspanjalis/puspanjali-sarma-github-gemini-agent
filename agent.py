from adk.agent import Agent
from adk.planner import GeminiPlanner
from adk.memory import SimpleMemory
from adk.tools import Tool, Toolset

from github_fetcher import get_trending_repos
from vector_store import LocalVectorDB
from config import GEMINI_API_KEY

# Embed trending repos
db = LocalVectorDB()
repos = get_trending_repos()
for repo in repos:
    db.add(repo["name"], repo["desc"], repo["url"])

# Define a custom tool
class GitHubRecommendTool(Tool):
    name = "github_recommender"
    description = "Recommend AI projects from GitHub"

    def invoke(self, query: str) -> str:
        results = db.search(query)
        return "\n".join([f"{name}: {url}" for name, url in results])

# Assemble agent
planner = GeminiPlanner(api_key=GEMINI_API_KEY)
memory = SimpleMemory()
toolset = Toolset([GitHubRecommendTool()])

agent = Agent(name="github-expert", planner=planner, memory=memory, toolset=toolset)

def main():
    q = input("What kind of AI project are you looking for? ")
    print(agent.run(q))

if __name__ == "__main__":
    main()
