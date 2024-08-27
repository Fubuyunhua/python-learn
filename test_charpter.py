# 练习题，求1-100的和
# num = int(input('计算1-n的和，\n请输入n的值:'))
# i = 1
# result = 0
# while i <= num:
#     result += i
#     i += 1
# print(f"计算结果为：{result}")
#
# # 方法2
# result = 0;
# for i in range(1, num+1):
#     result += i
#
# print("计算结果为：%3d" % result)
# print("计算结果为:", str(result))


# 猜数字
# import random
# num = random.randint(1, 100)
# count = 0
# gess_num = int(input("请输入猜测的数字："))
# while gess_num != num:
#     count += 1
#     if gess_num > num:
#         print("输入的猜测数值大于随机数")
#     else:
#         print("输入的猜测数值小于随机数")
#     gess_num = int(input("请输入猜测的数字："))
#
# print(f"一共猜测{count+1}次")


# while嵌套循环打印9*9乘法表
# i = 1
# j = 1
# while i <= 9:
#     while j <= i:
#         print(f"{j} * {i} = {i*j}", end="  ")
#         j += 1
#     print()
#     i += 1
#     j = 1
#
#
# for i in range(1, 10):
#     for k in range(1, i+1):
#         print("%2d *%2d=%d" %(i, k, i*k), end="  ")
#     print()
# 发工资
# import random
# money = 20
# for hums in range(1, 21):
#     salary = random.randint(1, 20)
#     if salary > money:
#         print("没钱了，结束")
#         break
#     else:
#         print(f"发给{hums}号{salary}万元")
#         money -= salary
# import string


# def covid_test(temp: float = 36.5):
#     if temp == 36.5:
#         print("is ok")
#     elif temp < 36.5:
#         print('too cold')
#     else:
#         print("too hot")
#
#
# input_temp = float(input("please input your tempture"))
# covid_test(input_temp)
#
#
# def add_function(x: int, y: int):
#     """
#     函数的作用是对两个整数求和
#     :param x:输入的整形变量
#     :param y: 输入的整形变量
#     :return:
#     """
#     return x + y
#
#
# def read_str(my_str: str):
#     my_list = list()
#     for x in my_str:
#         my_list.append(x)
#     return my_list
#
#
# my_list0 = input("please input a and b")
#
#
# print(my_list0,type(my_list0))
#
#
# def str2input_num(in_str: str):
#     count_num = 0
#     my_list = list()
#     for x in in_str:
#         if x != ' ':
#             my_list.append(int(x))
#             count_num += 1
#         else:
#             break
#     print(count_num)
#     x1 = 0
#     for i in my_list:
#         x1 *= 10
#         x1 += i
#         print(i)
#     y1 = 0
#     for x in in_str[count_num+1:]:
#         if x != ' ':
#             my_list.append(int(x))
#         else:
#             break
#     for i in my_list[count_num:]:
#        y1 *= 10
#        y1 += i
#     return x1, y1
#
#
# x0, y0 = str2input_num(my_list0)
#
# print(f"answer:{add_function(x0, y0)}")
