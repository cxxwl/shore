import pymysql

host = "localhost"
user = "root"
password = "root"
database = "bank"

def update(sql,param):
    con = pymysql.connect(host="localhost", user="root", password="root", database="bank")
    cursor = con.cursor()  # 创建控制台
    cursor.execute(sql, param)  # 执行sql
    con.commit()  # 提交真实数据到数据库里
    cursor.close()
    con.close()

def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host="localhost", user="root", password="root", database="bank")
    cursor = con.cursor()  # 创建控制台
    cursor.execute(sql, param)  # 执行sql
    # 提取数据
    if mode == "all":
        return cursor.fetchall()
    if mode == "many":
        return cursor.fetchmany(size)
    if mode == "one":
        return cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()








