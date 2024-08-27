# name_list = ["cai wei", "zhang shu cheng", "xie jia wei", "qian chun hui", "ji jun jie", "han run yu"]
# print(name_list)
# print(type(name_list))
# print(name_list[2])
# print(name_list[-6][-1])
# for str_name in name_list:
#     print(str_name)
#
#
# for i in range(-1,-7,-1):
#     print(name_list[i])

my_list = ["cai wei", "zhang shu cheng", "xie jia wei"]
# 查询某一元素的下标
index = my_list.index("zhang shu cheng")
print(f"该元素在列表中的下标为：{index}")
# 查找不存在的下标
# index = my_list.index("hello")
# print(f"该元素在列表中的下标为：{index}")
# 出现报错
my_list[2] = "zhou nian peng"
print(my_list)
my_list.append("qian chun hui")
print(my_list)
my_list.extend(["wang dong lei", "wang ji yan"])
print(my_list)
del my_list[3]
print(my_list)
my_list.remove("wang ji yan")
print(my_list)
count_element = my_list.count("cai wei")
print(f"number of cai wei:{count_element}")


