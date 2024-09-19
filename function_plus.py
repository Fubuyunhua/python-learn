# 2024.09.19
# 关于函数的闭包和实现计算机中的与或非和加法
# 一下为课堂代码
# 2024-2025（1）
# 2024-09-19、
def K(x):
    def Ky(y):
        return x

    return Ky


"""
这个可以理解为一个闭包，输入一个参数（可以是函数）返回一个函数
调用方式:K(para1)(para2)
代表着：K(para1)就是一个返回参数为para1的函数如KY(para1)
"""


def KI(x):
    def Ky(y):
        return y

    return Ky


def pair(x, y):
    return lambda f: f(x)(y)


"""
这里要多解释一个lambda函数，这个函数的语法是:lambda 参数1，参数2，参数3……: 正常函数流程（一行之内且没有return）
这里pair的作用就是将两个参数（包括函数）可以用额外的函数进行作用
pair(T,K)(T)
"""

def first(p):
    return p(K)


def second(p):
    return p(KI)


T = K
F = KI


def Not(x):
    return x(F)(T)


def And(x, y):
    return x(y)(F)


def Or(x, y):
    return x(T)(y)


def tob(b):
    return b(True)(False)


def Xor(x, y):
    return Or(And(x, Not(y)), And(Not(x), y))


def If(cond, x, y):
    return cond(x)(y)



"""
看懂这段代码的核心就是抽象，不能关注局部个体
add(n2, n3)
<function succ.<locals>.<lambda> at 0x000002CFFEFDD0D0>
result = add(n2, n3)
toi(result)
toi(n2)
2
toi(n3)
3
补充一个教会数的概念，教会数本身是一个高级函数
"""

n0 = lambda f: lambda x: x
n1 = lambda f: lambda x: f(x)
n2 = lambda f: lambda x: f(f(x))


def succ(n):
    return lambda f: lambda x: f(n(f)(x))


def toi(n):
    return n(lambda x: x + 1)(0)


n3 = succ(n2)


def add(a, b):
    return b(succ)(a)


def mul(a, b):
    return lambda f: b(a(f))


def power(a, n):
    return n(a)



