'''
#---txt文件操作---#
txt_filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/python_baidu.txt'

#---打开文件------#
file_obj = open(txt_filename, 'r', encoding='utf-8')

#---读取整个文件内容
all_content = file_obj.read()

# 关闭文件
file_obj.close()

print(all_content)
'''
txt_filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/python_baidu.txt'

# 打开文件
file_obj = open(txt_filename, 'r', encoding='utf-8')

# 逐行读取
line1 = file_obj.readline()
print(line1)

# 继续读下一行
line2 = file_obj.readline()
print(line2)

#列表

lines = file_obj.readlines()

#for line in lines:
#    print(line)

for i, line in enumerate(lines):   #循环次数
    print ('{}: {}'.format(i, line))

# 关闭文件
file_obj.close()