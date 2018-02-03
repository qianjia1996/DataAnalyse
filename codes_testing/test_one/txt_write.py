#---txt写操作---#
'''
txt_filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/python_baidu.txt'
# 打开文件
file_obj = open(txt_filename, 'w', encoding='utf-8')

# 写入全部内容
file_obj.write("《Python数据分析》")

print(file_obj)    #只能写

file_obj.close()
'''
'''
txt_filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/python_baidu.txt'

# 打开文件
file_obj = open(txt_filename, 'w', encoding='utf-8')

# 推导式写入字符串列表
lines = ['这是第%i行\n' %n for n in range(100)]
'''
lines = []
for n in range(100):
    line = '这是第%i行\n' %n
    lines.append(line)
'''
file_obj.writelines(lines)

file_obj.close()
'''

#---with语句---#
#包括了异常处理，自动调用文件关闭操作
#适用于对资源进行访问
txt_filename = './files/test_write.txt'
with open(txt_filename, 'r', encoding='utf-8') as f_obj:
    print(f_obj.read())