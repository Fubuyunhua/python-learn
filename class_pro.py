# from abc import ABCMeta, abstractmethod
#
#
# class Employee(metaclass=ABCMeta):
#     """员工（抽象类）"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         """月薪结算方法（抽象方法）"""
#         pass
#
#
# class Manager(Employee):
#     """部门经理"""
#
#     def __init__(self, name, postiton):
#         super().__init__(name)
#         self.postiton = postiton
#
#     @abstractmethod
#     def get_salary(self):
#         return 15000
#
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working=0):
#         self._working = working
#         super().__init__(name)
#
#     @abstractmethod
#     def get_salary(self):
#         return self._working * 200.0
#
#
# class Salesman(Employee):
#     """销售员"""
#
#     def __init__(self, name, sales=0):
#         self._sales = sales
#         super().__init__(name)
#
#     @abstractmethod
#     def get_salary(self):
#         return self._sales * 0.05 + 1800.0
"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


def main():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()
    for x in futures:
        print(x)
    print(account.balance)


if __name__ == '__main__':
    main()