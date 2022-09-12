import pymysql
# 连接数据库
db = pymysql.connect(host="192.168.175.5",
                     port = 3306,
                     user="zentao",
                     password="123456",
                     database="stu",
                     charset="utf8")
# name = input("name:")
# age = input("age:")
# score = input("score:")
data = [('zhang',11,55),('li',10,56),('wang',10,57)]
# 生成游标
cur = db.cursor()
try:
    # sql = "insert into class_1 values(9,'alex',10,'m',83)"
    sql = "insert into class_1 (name,age,score) values(%s,%s,%s)"
    # cur.execute(sql,[name,age,score])
    cur.executemany(sql,data)
    # sql = "update class_1 set score = 88.5 where  id = 7"
    # cur.execute(sql)
    # sql = 'delete from class_1 where id = 6'
    # cur.execute(sql)
    db.commit()   # 将操作提交
except Exception as e:
    db.rollback()  # 将数据回滚
# 关闭游标和数据库
cur.close()
db.close()