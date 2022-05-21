# 读取人物名称
file1 = open('name.txt')
data = file1.read().split('|')
print(data)
file1.close()

file2 = open('weapon.txt')
i = 1
for line in file2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1
file2.close()

file3 = open('sanguo.txt', encoding='GB18030')
print(file3.read().replace('\n', ''))
file3.close()