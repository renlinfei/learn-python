import re

def find_item(name):
    with open('sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(name, data)
        print('主角 %s 出现了 %s 次' %(name,len(name_num)))
    return len(name_num)

num_dict = {}
# 读取人物名字
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for name in names:
            # print(name)
            num_name = find_item(name)
            num_dict[name] = num_name

name_sorted = sorted(num_dict.items(), key=lambda item : item[1], reverse=True)
print(name_sorted[0:10])