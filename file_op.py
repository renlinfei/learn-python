# file1 = open('name2.txt', 'w')
# file1.write('诸葛亮')
# file1.close()
#
# file2 = open('name2.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name2.txt', 'a')
# file3.write('刘备')
# file3.close()

# file4 = open('name2.txt')
# print(file4.readline())
# file4.close()
#
# file5 = open('name2.txt')
# for line in file5.readlines():
#     print(line)
#     print("====")

file6 = open('name2.txt')
print(file6.tell())
print(file6.read(3))
print(file6.tell())
file6.seek(0)
print(file6.tell())