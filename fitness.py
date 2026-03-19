from datetime import datetime

# 先读取并显示 diary.txt 的历史内容（最近10条）
print("="*50)
print("📋 历史打卡记录（最近10条）：")
print("="*50)

try:
    with open("diary.txt", "r") as file:
        lines = file.readlines()
        if lines:
            # 只显示最后10条
            for line in lines[-10:]:
                print(line.rstrip())
        else:
            print("（暂无记录）")
except FileNotFoundError:
    print("（暂无记录）")

print("="*50)
print()

# 让用户输入今天的任务
task = input("请输入今天完成的任务：")

# 获取当前时间
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 创建要保存的内容
entry = f"[{current_time}] {task}\n"

# 把内容追加保存到 diary.txt
with open("diary.txt", "a") as file:
    file.write(
        entry)

print("✓ 已保存！")