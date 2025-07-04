import requests

def get_trending_repos():
    res = requests.get("https://ghapi.huchen.dev/repositories")
    res.raise_for_status()
    return [{"name": r["name"], "desc": r.get("description", ""), "url": r["url"]} for r in res.json()]
