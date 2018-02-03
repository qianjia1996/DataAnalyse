import pandas as pd
filename = '/Users/volare/Desktop/数据分析/第二章/codes/examples/output.txt'

df = pd.read_csv(filename, encoding='utf-8')
df.to_csv(filename, index=None,encoding='utf-8')
print(df)