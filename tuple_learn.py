# tuple_name = (1, "hello", "cai wei")
# my_tuple = ("test",)
# print(f"这个是什么呢？{type(my_tuple)}")
#
#
# # 进行切片，从1-4步长为1
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = my_list[1:4]
# print(f"对{my_list}进行切片的结果：{result}")
# # 对[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]进行切片的结果：[1, 2, 3]
#
# my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# ans = my_tuple[1:4]
# print(f"对{my_tuple}进行切片的结果：{ans}")
#
# # 对tuple进行切片，从下标零开始，步长为一，直至结束
# ans2 = my_tuple[:]
# print(f"对{my_tuple}进行切片的结果：{ans2}")
#
# # 对[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]进行切片的结果：[1, 2, 3]
# # 对(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)进行切片的结果：(1, 2, 3)
# # 对(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)进行切片的结果：(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# # 对整个字符串按步长为2及逆行切片
# my_str = "help yourself,gold help you too"
# ans3 = my_str[::2]
# print(f"{my_str}切片后 -> {ans3}")
# 集合定义
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育"}
my_set_empty = {}
print(f"my_set:{my_set}, my_set_empty:{my_set_empty}")

# 添加新元素
my_set.add("python")
print(f"my_set:{my_set}")

# 移除元素
my_set.remove("黑马程序员")
print(f"yi chu jie guo:{my_set}")

# 随机取出一个
ans = my_set.pop()
print(f"{ans}")

# 清空集合
ans = my_set.clear()
print(f"status:{ans}")


# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
# set3 = set1.difference(set2)
# print(f"set3:{set3}")
#
# # 在集合1内删除和集合2中相同的元素
# set1.difference_update(set2)
# print(f"set1:{set1}")

# 合并两个集合
set3 = set1.union(set2)
print(f"set3:{set3}")
set4 = set()
print(f"set4:{set4}")

