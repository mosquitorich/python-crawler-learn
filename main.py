from github_api import fetch_repo_info

owner = "mosquitorich"
repo = "python-crawler-learn"
data = fetch_repo_info(owner, repo)
if data:
    print(f"⭐ {data['stargazers_count']} stars")
    print(f"✍️ {data['description']}")