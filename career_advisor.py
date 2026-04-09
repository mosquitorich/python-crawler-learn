# 职业转型建议器（无客户信息）
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

print("=== 职业转型小助手 ===")
job = input("请输入你当前岗位（柜员/客户经理/信贷审批/风险主管）: ")
years = int(input("请输入在该岗位的工作年限: "))
advice = get_advice(job, years)
print("\n建议:", advice)
