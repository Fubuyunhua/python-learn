"""
使用多线程的情况 - 模拟多个下载任务
"""
from random import randint
from time import time, sleep
import atexit
import _thread


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    print('剩余时间%d秒.' % time_to_download)
    sleep(time_to_download)
    print('%s下载完成！' % filename)


def shutdown_hook(start):
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


def main():
    start = time()
    # 将多个下载任务放到多个线程中执行
    thread1 = _thread.start_new_thread(download_task, ('python从入门到住院.pdf', ))
    thread2 = _thread.start_new_thread(download_task,('Peking Hot.avi', ))
    atexit.register(shutdown_hook, start)


if __name__ == '__main__':
    main()


