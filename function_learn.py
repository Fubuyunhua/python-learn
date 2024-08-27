# # def my_function(x, y):
# #     print(f"{x} + {y} = {x+y}")
# #
# #
# # my_function(2, 5)
#
# def my_function2(x, y):
#     result = 1
#     for i in range(y):
#         result *= x
#     return result
#
#
# x_i = int(input("请输入x："))
# y_i = int(input("please input y:"))
# print(f"{x_i} ^ {y_i} = {my_function2(x_i, y_i)}")
# 函数的多返回值
def my_function(time=10, dis=1000, ruler='m'):
    volit = dis / time
    print(f"当前速度：{volit} {ruler}/s")


print("输入50和600得：")
my_function(50, 60)


def angel_compute(yaw=0, pit=0, rol=0):
    return yaw, pit, rol


x, y, z = angel_compute(30, 60, 90)
print("姿态角的参数：%s,%s,%s" % (x, y, z))


def angel_compute2(yaw=0, pit=1, rol=2):
    return yaw, pit, rol


x, y, z = angel_compute2(110, rol=60, pit=30)
print(f"ans:%s %s %s" % (x, y, z))
