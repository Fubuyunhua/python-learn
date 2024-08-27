import numpy as np
import pandas as pd
import pymysql
# ser1 = pd.Series(data=[120, 380, 250, 360], index=['一季度', '二季度', '三季度', '四季度'])
# print(ser1)
# ser2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
# print(ser2)
# print(f'两个系列和：\n{ser1 + ser2}')
# print(ser1[2])
# print(ser1.describe())
# print(ser2.dtype)                    # 数据类型
# print(ser2.hasnans)                  # 有没有空值
# print(ser2.index)                    # 索引
# print(ser2.values)                   # 值
# print(ser2.is_monotonic_increasing)  # 是否单调递增
# print(ser2.is_unique)                # 是否每个值都独一无二
# import matplotlib.pyplot as plt
#
# ser9 = pd.Series({'Q1': 400, 'Q2': 520, 'Q3': 180, 'Q4': 380})
# # 通过plot方法的kind指定图表类型为柱状图
# ser9.plot(kind='bar')
# # 定制纵轴的取值范围
# plt.ylim(0, 600)
# # 定制横轴刻度（旋转到0度）
# plt.xticks(rotation=0)
# # 为柱子增加数据标签
# for i in range(ser9.size):
#     plt.text(i, ser9[i] + 5, ser9[i], ha='center')
# plt.show()
# # plot方法的kind参数指定了图表类型为饼图
# # autopct会自动计算并显示百分比
# # pctdistance用来控制百分比到圆心的距离
# ser9.plot(kind='pie', autopct='%.1f%%', pctdistance=0.65)
# plt.show()
scores = np.random.randint(60, 101, (5, 3))
courses = ['语文', '数学', '英语']
stu_ids = np.arange(1001, 1006)
df1 = pd.DataFrame(data=scores, columns=courses, index=stu_ids)
print(df1)
scores1 = {'语文': [62, 72, 93, 88, 93],
           '数学': [95, 65, 86, 66, 87],
           '英语': [66, 75, 82, 69, 82]}
index1 = np.arange(1001, 1006)
df2 = pd.DataFrame(data=scores1, index=index1)
print(df2)
df3 = pd.DataFrame()
try:
    df3 = pd.read_csv('data/2023年北京积分落户数据.csv', index_col='id')
except ValueError:
    print('出现 ValueError')
finally:
    print(df3)

# 创建一个MySQL数据库的连接对象
conn = pymysql.connect(
    host='101.42.16.8', port=3306,
    user='guest', password='Guest.618',
    database='hrs', charset='utf8mb4'
)
# 通过SQL从数据库二维表读取数据创建DataFrame
df5 = pd.read_sql('select * from tb_emp', conn, index_col='eno')
print(df5)
