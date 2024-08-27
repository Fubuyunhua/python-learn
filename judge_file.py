# age = input("欢迎来到德莱联盟，请输入你的年龄")
# age = int(age)
# if age < 18:
#     print("臭小子，这里不是你来的地方")

# i = 5
# while i > 0:
#     i -= 1
#     print(f"当前次数{5 - (i + 1)+1}")
#     if i % 2 == 0:
#         print("努力")
#     else:
#         print("摆烂")
# str1 = "itheima is a brand of itcast"
# count = 0
# for x in str1:
#     if x == 'a':
#         count += 1
# print("字符串中A的数量", count)
"""
九九乘法表：
1 * 1 = 1

1 * 2 = 2	 2 * 2 = 4

1 * 3 = 3	 2 * 3 = 6	 3 * 3 = 9

1 * 4 = 4	 2 * 4 = 8	 3 * 4 = 12	 4 * 4 = 16

1 * 5 = 5	 2 * 5 = 10	 3 * 5 = 15	 4 * 5 = 20	 5 * 5 = 25

1 * 6 = 6	 2 * 6 = 12	 3 * 6 = 18	 4 * 6 = 24	 5 * 6 = 30	 6 * 6 = 36

1 * 7 = 7	 2 * 7 = 14	 3 * 7 = 21	 4 * 7 = 28	 5 * 7 = 35	 6 * 7 = 42	 7 * 7 = 49

1 * 8 = 8	 2 * 8 = 16	 3 * 8 = 24	 4 * 8 = 32	 5 * 8 = 40	 6 * 8 = 48	 7 * 8 = 56	 8 * 8 = 64

1 * 9 = 9	 2 * 9 = 18	 3 * 9 = 27	 4 * 9 = 36	 5 * 9 = 45	 6 * 9 = 54	 7 * 9 = 63	 8 * 9 = 72	 9 * 9 = 81
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{j} * {i} = {i*j}\t", end=" ")
#     print("\n")
#
for i in range(0,12,2):
    if i != 1:
        print("i = %d" % i)
    elif i % 2 == 1:
        print()
    else:
        print("zhe ge jiu shi ren sheng ")
        