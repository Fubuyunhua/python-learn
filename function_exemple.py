"""
# 华氏温度转化为摄氏温度
F_temperature = int(input('请输入华氏度，如果输入大于200则程序终止'))


def f2c(temp: int):
    C_temperature = (temp - 32) / 1.8
    return C_temperature


while F_temperature <= 200:
    answer = f2c(F_temperature)
    print('answer is %f' % answer)
    F_temperature = int(input('请输入华氏度，如果输入大于200则程序终止'))

"""

"""
# 输入圆的半径计算周长和面积

r = int(input('please input r'))


def calculate_square_length(r:int):
    s_answer = r*r*3.1415926
    l_answer = 2*r*3.1415926
    return s_answer, l_answer


s, l = calculate_square_length(r)

print(f'length = {s}, square = {l}')

"""

"""
# 判断平年还是闰年

year = int(input('请输入年份：'))
is_yaerp = year % 4 == 0 and year % 100 != 0 \
    and year % 400 ==0
print(is_yaerp)

"""

"""
# 钱百鸡问题

count = 0
for i in range(0, 21):
    for j in range(0, 34):
        for k in range(0, 101):
            if i * 5 + j * 3 + k == 100:
                print('公鸡：%d 母鸡：%d 小鸡：%d ' % (i, j, k*3))
                count += 1

print(count)
"""


# 最大公倍数

"""
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input('a input'))
b = int(input('b input'))

print('a and b 最大公倍数：%d' % gcd(a, b))

"""

#
def main():
    # Todo: Add your code here
    pass


if __name__ == '__main__':
    main()