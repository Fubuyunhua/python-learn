"""
进行装饰器的学习
"""


# 装饰器的作用是输入一个函数返回在此函数为基础上的一个新函数
# def simple_decorate(func):
#     def wrapper():
#         print('Before the function runs')
#         func()
#         print('After the function runs')
#
#     return wrapper
#
#
# @simple_decorate
# def say_hello():
#     print("Hello,World")
#
#
# say_hello()


# 带参数的装饰器
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print('Before function2 running')
        result = func(*args, **kwargs)
        print('After function2 running')
        return result

    return wrapper


@decorator_with_args
def greet(name):
    print('Hello %s!' % name)


greet('caiwei')


# 返回值的处理
def decorator_with_return(func):
    def wrapper(*args, **kwargs):
        print('Before %s running' % func.__name__)
        result = func(*args, **kwargs)
        print('After %s running' % func.__name__)
        return result.upper()

    return wrapper


@decorator_with_return
def greet2(name):
    return f"Hello, {name}!"


print(greet2("caiwei"))


def decorator_with_param(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f'当前的执行次数为：{i}')
                func(*args, **kwargs)
                print(f'第{i}次已经结束！')

        return wrapper

    return decorator


@decorator_with_param(3)
def say_name(name):
    print(f'hello {name}')


say_name('caiwei')
