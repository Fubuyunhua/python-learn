"""
生成器 - 生成器语法
"""
seq = [x * x for x in range(10)]
print(seq,end='')
print(' 当前类型'+ '%s' % type(seq))

gen = (x * x for x in range(10))
print(gen)
for x in gen:
    print(x , end='')
    print('\t', end='')
print(' 当前类型' + '%s' % type(gen))
