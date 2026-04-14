import datetime

def get_advice(job, years):
    if job in ["柜员", "客户经理"]:
        if years < 3:
            return "建议考取AFP/CFP，往财富管理深耕"
        else:
            return "可转型信贷审批或风控，你的客户经验是优势"
    elif job in ["信贷审批", "风险主管"]:
        if years < 5:
            return "建议补充数据分析技能，向数字化风控发展"
        else:
            return "可以考虑做金融科技咨询或企业内训"
    else:
        return "输入岗位：柜员、客户经理、信贷审批、风险主管"

# 查看历史
show = input("是否查看历史建议？(y/n): ")
if show.lower() == 'y':
    try:
        with open("history.txt", "r") as f:
            print("\n=== 历史记录 ===\n" + f.read())
    except FileNotFoundError:
        print("暂无历史记录。")

# 获取新建议
job = input("\n请输入岗位: ")
years_input = input("请输入年限: ")
try:
    years = int(years_input)
except ValueError:
    print("年限必须为数字，已设为0")
    years = 0

advice = get_advice(job, years)
print("\n建议:", advice)

# 保存到文件
with open("history.txt", "a") as f:
    today = datetime.date.today()
    f.write(f"{today} | 岗位:{job} 年限:{years} | 建议:{advice}\n")

print("已保存到历史记录。")
