import requests, json
from pathlib import Path


class FetchRepos:
    @staticmethod
    def fetch_repos(self):
        user = "octocat"
        url = f"https://api.github.com/users/{user}/repos"
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        repos = r.json()
        return [{"name": x["name"], "stars": x["stargazers_count"]} for x in repos]


if __name__ == "__main__":
    fetcher = FetchRepos()
    data = fetcher.fetch_repos()
    Path("data").mkdir(exist_ok=True)
    Path("data/repos.json").write_text(json.dumps(data, indent=2))
    print(f"Saved {len(data)} repos.")
