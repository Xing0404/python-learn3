
from pymysql import Connection

# 获取到MySQL数据库的链接对象
conn = Connection(
    host='localhost',              # 主机口（或IP地址）
    port=3306,                     # 端口，默认3306
    user='root',                   # 账户名
    password='123456'              # 密码
)

# 打印MySQL数据库软件信息(版本)
# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()         # 获取游标对象
# 选择数据库
conn.select_db("test")
# 执行sql  execute
cursor.execute("create table test_pymysql(id int);")       # 直接在括号内写sql语句，并且在当前语句中可以不写分号;

# 执行查询性SQL
cursor = conn.cursor()
conn.select_db("world")
cursor.execute("select * from student;")
# 获取查询结果 fetchall
result: tuple = cursor.fetchall()
for r in result:
    print(r)

# 关闭链接
conn.close()

'''
如果想在python中执行数据更改相关的操作（如数据插入等），需要通过commit方法去提交确认更改才能生效
即在执行sql语句下面加上: conn.commit()

如果不想手动commit确认，可以在构建链接对象的时候，设置自动commit的属性
如：
conn = Connection(
    host='localhost',              # 主机口（或IP地址）
    port=3306,                     # 端口，默认3306
    user='root',                   # 账户名
    password='123456',             # 密码
    autocommit=True                 # 设置自动提交
)
'''