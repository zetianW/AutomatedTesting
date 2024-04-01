# 开发人员：泽天

# 开发时间：2024/1/30 18:12

# 项目定义：
import datetime

now = datetime.datetime.now()
target_time = now.replace(2024, 1, 29, 14, 3, 0, 0)
time_difference = (target_time - now).total_seconds()/3600
print(time_difference)
