"""
使用协程 - 模拟快递中心派发快递

Version:0.1
Author: 蔡伟
Date:2024-08-07
"""
from time import sleep
from random import random


def build_deliver_man(man_id):
    total = 0
    while True:
        total += 1
        pkg = yield
        print('%d号快递员准备今天的第%d单' % (man_id, total))
        print('%d号快递员收到编号为%s的包裹.' % (man_id, pkg))
        sleep(random()*3)


def package_center(deliver_man, max_per_day):
    num = 1
    deliver_man.send(None)
    # next(deliver_man)
    while num <= max_per_day:
        pkg = "PKG-%d" % num
        deliver_man.send(pkg)
        num += 1
    deliver_man.close()
    print('今天的包裹派送完毕')


dm = build_deliver_man(1)
package_center(dm, 10)

#
# def learn_yield():
#     yield 1
#     yield 2
#     yield 3
#
#
# test_value0 = learn_yield()
# for i in range(3):
#     print(next(test_value0))


# def learn_yield2():
#     total = 0
#     while True:
#         value = yield total
#         if value is None:
#             break
#         total += value
#
#
# test_value1 = learn_yield2()
#
#
# def test_yield3():
#     print('test start')
#     count = 1
#     while True:
#         _x = yield count
#         if _x is None:
#             break
#         count += 1
#         print(f"接受内容:{_x}")
#
#
# list_test = ['hello', 'world', '!', None]
# test_value2 = test_yield3()
# print(next(test_value2))
# try:
#     for x in list_test:
#         print(test_value2.send(x))
# except StopIteration:
#     print("测试结束")
