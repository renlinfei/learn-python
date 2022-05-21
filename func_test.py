from functools import reduce

# def func_test(a, b, c):
#     print('a = %s' %a)
#     print('b = %s' %b)
#     print('c = %s' %c)
#
# func_test(1, 2, 3)
# func_test(b=3, a=2, c=8)
# func_test(1)

# def howlong(first, *others):
#     print(1 + len(others))
#
# howlong(1, 3, 5)

# var1 = 123
#
# def func():
#     global var1
#     var1 = 456
#     print(var1)
#
# func()
# print(var1)

# list = [1, 2, 3]
# it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for i in range(10, 20, 1):
#     print(i)

# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         # yield x
#         # print(x)
#         x += step
#
# it = iter(frange(10, 20, 0.5))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# alist = [2, 3, 4, 5, 7, 8, 9]
#
# print(list(filter(lambda x : x%2 == 0, alist)))
#
# a = [1,2,3]
# b = [4,5,6]
# print(list(map(lambda x,y:x+y, a, b)))
#
#
# for i in zip(a, b):
#     print(i)
#
# adict ={'a':'aa', 'b':'bb'}
# print(dict(zip(adict.values(), adict.keys())))

# 内部函数引用外部函数变量的写法，叫做闭包

def sum(a):
    def add(b):
        return a + b
    return add

print(sum(1)(2))