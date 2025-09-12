import pandas as pd
import os
# 数据导入
# 使用绝对路径
# fpath_excel = r"D:\知行合一\数据分析\python\data\test.xlsx"
# fpath_csv = r"D:\知行合一\数据分析\python\data\Fitness_Tracker_Data.csv"

# 使用相对路径
# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 设置当前工作目录为脚本所在的目录
os.chdir(script_dir)

fpath_excel = r"data\test.xlsx"
fpath_csv = r"data\Fitness_Tracker_Data.csv"

# 读取 Excel 文件
pdata_excel = pd.read_excel(fpath_excel)
print("Excel 文件内容：")
print(pdata_excel)

# 读取 CSV 文件
pdata_csv = pd.read_csv(fpath_csv, encoding='gbk')
print("\nCSV 文件内容：")
print(pdata_csv)

# 数据保存
# 保存为 CSV 文件
df = pd.DataFrame({'Name': ['Al', 'B', 'C'], 'Age': [25, 30, 35]})
df.to_csv('output.csv', index=False, encoding='utf-8') # index=False表示不带行索引
# 保存为 Excel 文件
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

# 保存为 JSON 文件
df.to_json('output.json', orient='records', indent=4)

# 保存为 HTML 文件
df.to_html('output.html', index=False)

# 