import pandas as pd
from github_api import fetch_repo_info

repos = [
    ("mosquitorich", "python-crawler-learn"),
    ("pandas-dev", "pandas"),
    ("tensorflow", "tensorflow")
]

data_list = []
for owner, repo in repos:
    print(f"正在获取 {owner}/{repo} ...")
    info = fetch_repo_info(owner, repo)
    if info:
        data_list.append({
            "name": info["name"],
            "stars": info["stargazers_count"],
            "forks": info["forks_count"],
            "open_issues": info["open_issues_count"],
            "language": info["language"]
        })
    else:
        print(f"获取失败: {owner}/{repo}")

if not data_list:
    print("没有获取到任何数据，请检查网络或 GitHub API 限制。")
else:
    df = pd.DataFrame(data_list)
    print("\n=== 仓库数据对比 ===")
    print(df.to_string(index=False))
    
    print("\n=== 统计信息 ===")
    print(f"星标数最多: {df.loc[df['stars'].idxmax(), 'name']} ({df['stars'].max()} stars)")
    print(f"星标数最少: {df.loc[df['stars'].idxmin(), 'name']} ({df['stars'].min()} stars)")
    print(f"平均星标数: {df['stars'].mean():.0f}")
    print(f"总复刻数: {df['forks'].sum()}")
    print(f"总开放 issues: {df['open_issues'].sum()}")
