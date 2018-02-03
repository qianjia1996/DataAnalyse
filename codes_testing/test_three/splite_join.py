'''
数据库多表连接：
查询记录时将多个表中的记录连接join并返回结果
join方式：
    交叉连接 cross join
    内连接   inner join
    外连接   outer join
'''
import sqlite3

db_path = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/test_join.sqlite'

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# 建 depaetment 表，并插入数据
cur.execute("DROP TABLE IF EXISTS department")
cur.execute("CREATE TABLE department(\
                id INT PRIMARY KEY NOT NULL, \
                dept CHAR(50) NOT NULL, \
                emp_id INT NOT NULL)")
depts = (
        (1, 'IT Builing', 1),
        (2, 'Engineerin', 2),
        (3, 'Finance', 7)
)
cur.executemany("INSERT INTO department VALUES(?, ?, ?)", depts)

# 建 company 表，并插入数据
cur.execute("DROP TABLE IF EXISTS company")
cur.execute("CREATE TABLE company(\
                    id INT PRIMARY KEY NOT NULL, \
                    name CHAR(50) NOT NULL, \
                    age INT NOT NULL, \
                    address CHAR(50) NOT NULL,\
                    salary DOUBLE NOT NULL)")
companies = (
        (1, 'Paul', 32, 'California', 20000.0),
        (2, 'Allen', 25, 'Texas', 15000.0),
        (3, 'Teddy', 23, 'Norway', 20000.0),
        (4, 'Mark', 25, 'Rich-Mond', 65000.0),
        (5, 'David', 27, 'Texas', 85000.0),
        (6, 'Kim', 22, 'South-Hall', 45000.0),
        (7, 'James', 24, 'Houston', 10000.0)
)
cur.executemany("INSERT INTO company VALUES (?, ?, ?, ?, ?)", companies)

conn.commit()

#cross join交叉连接
cur.execute("SELECT emp_id, name, dept FROM company CROSS JOIN department;")
rows = cur.fetchall()
for row in rows:
    print(row)
#行 row  列 column