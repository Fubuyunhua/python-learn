"""
异步I/O操作 - async模块

Version:0.1
Author:蔡伟(我抄的)
Date:2024-08-07
"""
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    # 异步方式等待结果
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    # 异步I/O方式执行写操作
    await writer.drain()
    while True:
        # 异步I/O方式执行读操作
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
hosts_list = ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
tasks = [wget(host) for host in hosts_list]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
