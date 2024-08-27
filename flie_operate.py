# def main():
#     print('go')
#     f = open(r"C:\Users\DELL\Desktop\hello.txt", 'r', encoding='utf-8')
#     print('lets go')
#     print(f.read())
#     print('is ok')
#     f.close()
# 程序健壮性的写法
# def main():
#     f = None
#     try:
#         f = open(r"C:\Users\DELL\Desktop\hello.txt", 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件')
#     except LookupError:
#         print('指定了未知编码！')
#     except UnicodeError:
#         print('读取文件时编码错误')
#     finally:
#         if f:
#             f.close()
# with open 可以在离开上下文的环境下自动关闭文件
# def main():
#     try:
#         with open(r"C:\Users\DELL\Desktop\hello.txt", 'r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print("未发现文件！")
#     except LookupError:
#         print('指定了未知编码！')


# 进一步的方法
# def main():
#     try:
#         with open(r"C:\Users\DELL\Desktop\hello.txt", 'r', encoding='utf-8') as f:
#             for line in f.read():
#                 print(line, end='')
#         print()
#         with open(r"C:\Users\DELL\Desktop\hello.txt", 'r', encoding='utf-8') as f:
#             print(f.readlines())
#     except FileNotFoundError:
#         print("警告！警告！我要红温了！")
# 如何进行写入
def isprime(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True if num != 1 else False


def main():
    file_name = (r'C:\Users\DELL\Desktop\a.txt', r'C:\Users\DELL\Desktop\b.txt')
    list_file = []
    try:
        for filename in file_name:
            list_file.append(open(filename, 'w', encoding='utf-8'))

        for numb in range(2, 101):
            if isprime(numb):
                list_file[0].write(str(numb) + '\n')
            else:
                list_file[1].write(str(numb) + '\n')
    except FileNotFoundError:
        print("无法找到文件")
    except IOError as ex:
        print(ex)
        print("读写错误")
    finally:
        for pointerfile in list_file:
            pointerfile.close()


if __name__ == '__main__':
    main()
