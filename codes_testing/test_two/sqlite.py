'''
Python数据库
SQLite:
关系型数据库管理系统
嵌入式数据库
SQLite不是C/S的数据库引擎
集成在用户程序中
连接数据库：
    conn = sqlite3.connect(db_name)
获取游标：
    conn.cursor()
    一段私有的SQL工作区
CRUD操作：
    cursor.execute()
fetchone()
fetchall()
conn.commit()
关闭连接 conn.close
'''
import sqlite3

db_path = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/test.sqlite'

conn = sqlite3.connect(db_path)
cur = conn.cursor()
conn.text_factory = str  # 处理中文

cur.execute('SELECT SQLITE_VERSION()')

print('SQLite版本：', str(cur.fetchone()[0]))
#逐条插入数据
cur.execute("DROP TABLE IF EXISTS book")
cur.execute("CREATE TABLE book(id INT, name TEXT, price DOUBLE)")
cur.execute("INSERT INTO book VALUES(1,'肖秀荣考研书系列:肖秀荣(2017)考研政治命题人终极预测4套卷',14.40)")
cur.execute("INSERT INTO book VALUES(2,'法医秦明作品集:幸存者+清道夫+尸语者+无声的证词+第十一根手指(套装共5册) (两种封面随机发货)',100.00)")
cur.execute("INSERT INTO book VALUES(3,'活着本来单纯:丰子恺散文漫画精品集(收藏本)',30.90)")
cur.execute("INSERT INTO book VALUES(4,'自在独行:贾平凹的独行世界',26.80)")
cur.execute("INSERT INTO book VALUES(5,'当你的才华还撑不起你的梦想时',23.00)")
cur.execute("INSERT INTO book VALUES(6,'巨人的陨落(套装共3册)',84.90)")
cur.execute("INSERT INTO book VALUES(7,'孤独深处(收录雨果奖获奖作品《北京折叠》)',21.90)")
cur.execute("INSERT INTO book VALUES(8,'世界知名企业员工指定培训教材:所谓情商高,就是会说话',22.00)")

#批量插入数据
books = (
    (9, '人间草木', 30.00),
    (10,'你的善良必须有点锋芒', 20.50),
    (11, '这么慢,那么美', 24.80),
    (12, '考拉小巫的英语学习日记:写给为梦想而奋斗的人(全新修订版)', 23.90)
)
cur.executemany("INSERT INTO book VALUES(?, ?, ?)", books)

#提交数据
conn.commit()

#查找数据
cur.execute('SELECT * FROM book')
rows = cur.fetchall()

# 通过索引号访问
for row in rows:
    print('序号: {}, 书名: {}, 价格: {}'.format(row[0], row[1], row[2]))

conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute('SELECT * FROM book')
rows = cur.fetchall()

# 通过列名访问
for row in rows:
    print('序号: {}, 书名: {}, 价格: {}'.format(row['id'], row['name'], row['price']))

#关闭
conn.close()

#其它数据库连接



