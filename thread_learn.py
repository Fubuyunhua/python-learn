"""
异步I/O操作 - asyncio模块

Version:0.1
Author:蔡伟
Date:2018-03-21
"""

# 导入异步I/O包
import asyncio
# 导入多线程包
import threading
# import time


async def hello():
    print('%s:hello, world' % threading.current_thread())
    # 休眠不hi阻塞主线程因为使用了异步步I.O
    # 注意有yield from才会等待休眠操作执行，由于这些语法都是3.4版本的，现在采用了await和asy这些关键字
    await asyncio.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s:goodbye,world' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结果，就是说这个loop中的协程就是在同一个线程
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
