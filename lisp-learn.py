# def average(x, y):
#     return (x + y) / 2.0
# 
# 
# def square_guess(g, x):
#     guess = average(g, x / g)
#     return guess
# 
# 
# def Squart_x(inputValue, guess):
#     if inputValue < 0:
#         print('error')
#         return -1
#     elif abs(guess - inputValue / guess) < 0.001:
#         return guess
#     else:
#         return Squart_x(inputValue, square_guess(guess, inputValue))
# 
# 
# list_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for x in list_test:
#     print(f'{x}的平方根为{Squart_x(x, 1)}', end='\t')
#     print('%2d的三位精度平方根为%6.4f' % (x, Squart_x(x, 1)))
# 
# import time
# 
# count_learn = 0
# count_resc = 0
# 
# 
# def learn_add(value_x: int, value_y: int):
#     """
#     :param value_x: 输入的一个整数
#     :param value_y: 输入的一个整数
#     :return: x + y 返回二数之和
# 
#     采用了迭代的方法发，实现
#     """
#     global count_learn
#     count_learn += 1
#     while value_x != 0:
#         count_learn += 1
#         value_x -= 1
#         value_y += 1
#     return value_y
# 
# 
# def resc_add(re_x: int, re_y: int):
#     global count_resc
#     count_resc += 1
#     if re_x == 0:
#         return re_y
#     else:
#         return 1 + resc_add(re_x - 1, re_y)
# 
# 
# start1 = time.time()
# print(f'计算3+4：{learn_add(800, 100)}')
# end1 = time.time()
# print(f'所花时间：{count_learn}')
# start2 = time.time()
# print(f'计算3+4：{resc_add(800, 100)}')
# end2 = time.time()
# print('所花时间：%d' % count_resc)
# 
# """
# 
# 计算3+4：900
# 所花时间：801
# 计算3+4：900
# 所花时间：801
# 说明递归和迭代的实践复杂度是相同的，但是它们所占的空间复杂度往
# 往根据题目的数据或题目特性具有相当大的差距
# 迭代只有当前的内存中的数据就可以计算，但是递归必须要之前所有的结果不断传递
# """

# def fib(a: int, b: int, count: int):
#     """
#
#     :param a:
#     :param b:
#     :param count:
#     :return:
#     """
#     if count == 0:
#         return b
#     else:
#         fib(a + b, a, count - 1)
#
#
# def fib2(_a: int, _b: int, _count: float):
#     if _count == 0:
#         return _b
#     else:
#         return fib2(_a + _b, _a, _count - 1)
#
#
# print(f'answer of fib:{fib(1, 0, 5)}')
# print(f'answer of fib2:{fib2(1, 0, 5)}')

list_money = [1, 5, 10, 50, 100, 200, 500, 1000]


def count_change(start: int, end: int, amount):
    """
    用于求找零钱的总方法数量
    :param start:
    :param end:
    :param amount:
    :return:
    """
    global list_money
    if start <= end:
        if amount < 0:
            return 0
        elif amount == 0:
            return 1
        else:
            return count_change(start + 1, end, amount - list_money[start]) + count_change(start + 1, end, amount)
    else:
        return 0


input_money = int(input('请输入要查询的钱数：'))
print(f'找钱{input_money}的方法有{count_change(-1, len(list_money) - 1, input_money)}')


def cc(count_change: int, amount: float):
    global list_money
    if amount < 0 or count_change < 0:
        return 0
    elif amount == 0:
        return 1
    else:
        return cc(count_change-1, amount) + cc(count_change, amount-list_money[count_change])


print(f'找钱{input_money}的方法有{cc(7, input_money)}')