"""
使用多线程形的情况 - 模拟下载多个任务
"""
from random import randint
from threading import Thread
from time import time, sleep


def download_tasks(filename):
    print('开始%s:文件的下载' % filename)
    download2time = randint(5, 10)
    sleep(download2time)
    print('%s：下载任务完成' % filename)


def main():
    start = time()
    list_filename = ['file0', 'file1']
    thread1 = Thread(target=download_tasks, args=(list_filename[0], ))
    thread2 = Thread(target=download_tasks, args=(list_filename[1], ))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    over_time = time()
    print('总共耗时为：%.3f' % (start - over_time) * (-1))


if __name__ == '__main__':
    main()
