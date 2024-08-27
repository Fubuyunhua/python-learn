# def fn(nums: int):
#     if nums == 1:
#         return 1
#     else:
#         return nums * fn(nums-1)
#
#
# def hannuota(in_0:int, source, aux, target):
#     if in_0 == 1:
#         print(f'{source}->{target}')
#         return
#     hannuota(in_0 - 1,source, target, aux)
#     print(f'{source}->{target}')
#     hannuota(in_0 - 1, aux, source, target)
#
#
# def main():
#     num = int(input('please input number'))
#     print('n的阶乘为：%d' % fn(num))
#     num = int(input('please input hannuota numb'))
#     hannuota(num, 'A', 'B', 'C')
#
#
# if __name__ == '__main__':
#     main()
from random import randint
from time import time


def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        for j in range(i + 1, len(items)):
            if comp(items[j], items[i]):
                temp = items[j]
                items[j] = items[i]
                items[i] = temp
    return items


need_sort_list = list()
for _ in range(20):
    need_sort_list.append(randint(1, 100))

result_list = select_sort(need_sort_list)
print(f'select_sort:{need_sort_list}->{result_list}')


def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swap_flag = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swap_flag = True
        if not swap_flag:
            break
    return items


need_sort_list1 = list()
for _ in range(20):
    need_sort_list1.append(randint(1, 100))

result_list1 = bubble_sort(need_sort_list1)
print(f'bubble_sort:{need_sort_list1}->{result_list1}')


def merge(items1, items2, cmp=lambda x, y: x < y):
    items = []
    index1 = index2 = 0
    while index1 < len(items1) and index2 < len(items2):
        if cmp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    if index1 < len(items1):
        extra_list1 = [x for x in items1[index1:]]
        items.append(extra_list1)
    if index1 < len(items1):
        extra_list2 = [x for x in items2[index2:]]
        items.append(extra_list2)
    return items


print(f'merge:{merge(result_list, result_list1)}')
