"""
异步IO操作 - async和await

version:01
Author:蔡伟
Date:2024-08-07
"""
import asyncio
import threading


# 通过async修饰的函数不再是普通函数而是一个协程
# 注意async和await将再python 3.7中作为关键字出现
async def hello():
    print('%s:hello,world!' % threading.current_thread())
    await asyncio.sleep(2)
    print('%s:goodbye,world!' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步IO操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

