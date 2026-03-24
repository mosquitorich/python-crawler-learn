# 银行职业档案（无客户信息）
name = "靳雯"
total_years = 10

positions = ["柜员", "客户经理", "信贷审批专员", "风险主管"]
years_in_position = [2, 3, 3, 2]

job_duties = {
    "柜员": ["现金收付", "账户开户", "基础业务咨询"],
    "客户经理": ["客户关系维护", "理财产品销售", "贷款需求挖掘"],
    "信贷审批专员": ["企业财务分析", "风险评估", "撰写审批报告"],
    "风险主管": ["团队管理", "制定风控政策", "监控不良贷款"]
}

skills = ["财务分析", "风险建模", "客户沟通", "团队管理", "Python基础"]

print("姓名:", name)
print("银行工龄:", total_years)
print("\n岗位历程:")
for i in range(len(positions)):
    print(f"{positions[i]}：{years_in_position[i]}年")

print("\n各岗位工作内容:")
for job, duties in job_duties.items():
    print(f"【{job}】")
    for duty in duties:
        print(f"  - {duty}")

print("\n核心技能:")
for skill in skills:
    print(f"  • {skill}")

print(f"\n总年限（检查）: {sum(years_in_position)}年")
