# from math import sqrt
#
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and a + c > b and b + c > a
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter()/2
#         return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))
#
#
# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法大都采用给类发消息
#     if Triangle.is_valid(a, b, c):
#         triangle = Triangle(a, b, c)
#         print(triangle.perimeter())
#         # print(Triangle.perimeter(triangle))
#         print(triangle.area())
#
#     else:
#         print('无法构成三角形')
# from time import sleep, time, localtime
#
#
# class Clock(object):
#
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     @classmethod
#     # 类方法进行初始化
#     def clock_now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#     def run(self):
#         self._second += 1
#         if self._second == 60:
#             self._minute += 1
#             self._second = 0
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock.clock_now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run

# 继承
# class Person(object):
#     def __init__(self, name, age, gender):
#         self._name = name
#         self._age = age
#         self._gender = gender
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @property
#     def gender(self):
#         return self._gender
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         print('%s正在愉快的玩耍' % self._name)
#
#
# class Student(Person):
#     def __init__(self, name, age, gender, grade):
#         super().__init__(name, age, gender)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#     def study(self):
#         print('%s正在努力的学习' % self._name)
#
#
# def main():
#     stu = Student('caiwei', 24, 'man', '研0')
#     print(stu.name)
#     print(stu.grade)
#     stu.grade = '研一'
#     print(stu.grade)
#     stu.play()

# 多态
# from abc import ABCMeta, abstractmethod
#
# class Pet(object):
#     """宠物"""
#
#     def __init__(self, nickname):
#         self._nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         """发出声音"""
#         pass
#
#
# class Dog(Pet):
#     def make_voice(self):
#         print('%s:汪汪汪'% self._nickname)
# exemple 1
from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者类"""


# 通过slots来限定可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    # 初始化方法
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击

        :param other: 攻击的对象
        :return:
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """奥特曼的属性

        :param name: 姓名
        :param hp: 生命值
        :param mp: 蓝条
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp > 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击

        :param others: 攻击对象
        :return:攻击成功返回True
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
                '生命值：%s\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.hp > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('洛昊', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=====第%02d回合=====' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用了普通攻击攻击了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击' % u.name)
            else:
                print('%s使用魔法失败' % u.name)

        else:
            if u.huge_attack(m):
                print('%s使用了必杀技攻击了%s' % (u.name, m.name))
            else:
                print('%s使用普通攻击攻击力%s' % (u.name, m.name))
                print('恢复了%d点魔法值' % u.resume())

        if m.alive:
            print('%s回击了%s' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n======回合结束=====\n')
    if u.alive:
        print('%s奥特曼赢' % u.name)
    else:
        print('小怪兽赢')


if __name__ == '__main__':
    main()
