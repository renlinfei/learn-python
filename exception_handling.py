# j = i
#
# d = {'a':1, 'b':'2'}
# print(d['c'])

# 1/0

# a = 123
# a.append('1')

# try:
#     int(input('请输入年份'))
# except ValueError as e:
#     print('请输入数字，具体错误为%s' %(e))

# try:
#     int(input('请输入年份'))
#     open('name2.txt')
# except (ValueError, FileNotFoundError) as e:
#     print('%s' %(e))

try:
    raise NameError('文件找不到')
except NameError as e:
    print(e)


