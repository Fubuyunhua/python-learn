"""
使用process类创建多个进程
"""
import random
from multiprocessing import Process,Queue,current_process
from time import sleep


def sub_task(content, counts, time):
    print(f'PID:{current_process().pid}')
    counter = 0
    while counter <= counts:
        counter += 1
        print(f'{content}:{counter}')
        sleep(time)


def main():
    number = random.randrange(5, 10)
    Process(target=sub_task, args=('Ping', number, 0.01)).start()
    Process(target=sub_task, args=('Pong', number, 0.02)).start()


if __name__ == '__main__':
    main()