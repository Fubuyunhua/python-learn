from pymysql import Connection
# 获取到MySQL
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='cw20003845',
    autocommit=True
)


# print(conn.get_server_info())
# 执行非查询性质的SQL
cursor = conn.cursor() # 获取游标对象
# 选择数据库
conn.select_db("world")
# 执行sql
cursor.execute("INSERT INTO student (id, name, age) VALUES ('9', '王冬雷', 24);")
# 通过commit进行确认
# conn.commit()
cursor.execute("select * from student")  # 光标的功能决定了它的意义，只有查询的光标才能实现数据读取
result = cursor.fetchall()
print(result)
conn.close()
