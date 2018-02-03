#comma-separated values
'''
以纯文本形式存贮的表哥数据，以逗号作为分隔符
通常第一行为列名
文件操作：
   np.loadtxt()
   pandas
读操作：
   df_obj = pd.read_csv()
   返回dataframe类型的数据

写操作：
   df_obj.to_csv()
'''

import pandas as pd

filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/gender_country.csv'
print(type(filename))
df = pd.read_csv(filename, encoding='utf-16')

print(type(df))    #dataframe数据类型
print(df.head())   #额外增加索引号  第一行为行名

country_se = df[u"国家"]    #u  unicode
print(type(country_se))    #series数据
print(country_se.head())

'''
pandas基于numpy构建
索引在左，数值在右。索引是pandas自动创建的
数据结构：
    series 类似于一维数据的对象
    dataframe 表格型数据结构 每列可以不同数据类型
'''