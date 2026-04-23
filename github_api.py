import  requests
import json
def fetch_repo_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()
        return reponse.json()
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def save_to_json(data,filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"已保存到 {filename}")

if __name__ == "__main__":
    info =fetch_repo_info("mosquitorich", "python-crawler-learn")
    if info:
        print(f"仓库名称: {info['name']}")
        print(f"描述: {info['description']}")
        print(f"星标数: {info['stargazers_count']}")
        save_to_json(info, "repo_info.json")