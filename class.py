# from time import sleep
#
#
# class Clock():
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """
#
#         :param hour:
#         :param minute:
#         :param second:
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._minute += 1
#             self._second = 0
#             if self._minute == 60:
#                 self._hour += 1
#                 self._minute = 0
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%2d:%2d:%2d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
# from math import sqrt
#
#
# class Point():
#
#     def __init__(self, x=0, y=0):
#         """
#         初始化方法
#
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """移动到指定位置
#
#         :param x: 新的横坐标
#         :param y: 新的纵坐标
#         :return:
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """移动相应的增量
#
#         :param dx: 横坐标的增量
#         :param dy: 纵坐标的增量
#         :return:
#         """
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """到另一个坐标的距离
#
#         :param other: 另一个点
#         :return:
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))
#
#
# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))
class Person(object):

    # 限定Person对象只能绑定_name,_age,和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 -getter 方法
    @property
    def age(self):
        return self._age

    # 修改器setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age > 18:
            print('可以玩一些好玩的游戏了')
        else:
            print('只能玩一些不是很好玩的游戏了')


def main():
    person = Person('王大锤', 38)
    person.play()
    person.age = 16
    person.play()


if __name__ == '__main__':
    main()
