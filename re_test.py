# .

import re

# .匹配任意单个字符
# ^以。。。开头
# $以。。。结尾
# *前面匹配匹配0次到多次
# +前面的字符一次到多次
# ?前面字符0次或一次
# {m}前面的字符出现m次
# {m,n}出现m-n次
# []中括号内的任意字符匹配成功
# \d匹配数字 等价于 [0-9]+
# \D匹配不包含数字
# \s等价于 [a-z]+
# ()分组

# .*? 不使用贪婪模式

# p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2022-5-02').group(2))
# print(p.match('2022-5-02').groups())
# year, month, day = p.match('2022-5-02').groups()
# print(year)

# print(p.search('aa2022-5-02bb'))

# phone = '123-456-789 # 这是电话号码'
# p2 = re.sub(r'#.*', '', phone)
# print(p2)
# p3 = re.sub(r'\D', '', p2)
# print(p3)

# re.S 整行匹配

# a = '''asdfhellopass:
#     worldaf
#     '''
# b = re.findall('hello(.*?)world', a)
# c = re.findall('hello(.*?)world', a, re.S)
# print(b)
# print(c)
#
# # re.I 不区分大小写
# res = re.findall(r"A", "abc", re.I)
# print(res)

# re.M 将所有行的尾字母输出
s = '12 34\n56 78\n90'
print(re.findall(r'^\d+', s, re.M)) # 匹配位于首行的数字

print(re.findall(r'\A\d+', s, re.M)) # 匹配位于字母串开头的数字

print(re.findall(r'\d+$', s, re.M)) # 匹配位于行位的数字

print(re.findall(r'\d+\Z', s, re.M)) # 匹配位于字符串尾的数字




