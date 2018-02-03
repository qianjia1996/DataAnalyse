'''
JSON(javaScript Object Natation)
轻量级的数据交换格式
语法格式：
    数据是健值对
    由逗号分隔
    {}保存对象 {key1:val1,}
    []保存数组 [val1,val2]
读操作：
    json.load(file_obj)
    返回值 dict类型
类型转换 json -> csv
编码操作：
    json.dumps()
'''


import json

filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/files/global_temperature.json'
with open(filename, 'r') as f_obj:
    json_data = json.load(f_obj)

# 返回值是dict类型
#print(type(json_data))
#print(json_data)

#print(json_data.keys())

#JSON转CSV
print(json_data['data'].values())

#转换keys
year_str_lst = json_data['data'].keys()
year_lst = [int(year_str) for year_str in year_str_lst]
#print(year_lst)

#转换value
temp_str_lst = json_data['data'].values()
temp_lst = [float(temp_str) for temp_str in temp_str_lst]
#print(temp_lst)

#保存csv
import pandas as pd

# 构建 dataframe
year_se = pd.Series(year_lst, name = 'year')
temp_se = pd.Series(temp_lst, name = 'temperature')
result_df = pd.concat([year_se, temp_se], axis = 1)   #axis = 1 轴的方向 0按纵

print(result_df.head())

# 保存csv
result_df.to_csv('./files/json_to_csv.csv', index = None)  #index = None 不要索引