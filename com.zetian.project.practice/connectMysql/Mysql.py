# 开发人员：泽天

# 开发时间：2024/3/21 14:31

# 项目定义：
# 导入pymysql模块
import pymysql

# 定义连接参数
host = 'rm-3ns77a88hm732bsftqo.mysql.rds.aliyuncs.com'
port = 3306
user = 'bok'
password = 'ahsdqweasd!^5'
database = 'bok_health'
charset = 'utf8mb4'

connection = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             password=password,
                             db=database,
                             charset=charset)

cursor = connection.cursor()
sql = "select * from user_info where id = 1"
try:
    cursor.execute(sql)

    columns = [i[0] for i in cursor.description]
    results = cursor.fetchall()

    for row in results:
        print("{")
        for i, value in enumerate(row):
            print(f"  '{columns[i]}': {value},")
        print("}")

except pymysql.MySQLError as e:
    print(f"执行SQL时发生错误: {e}")

cursor.close()
connection.close()
