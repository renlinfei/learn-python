zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
               u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

cz_num = {}
z_num = {}
for i in zodiac:
    cz_num[i] = 0

for i in zodiac_name:
    z_num[i] = 0
# for zodiac_num in range(0, len(zodiac_days)):
#     if zodiac_days[zodiac_num] >= (month, day):
#         print(zodiac_name[zodiac_num])
#         break
#     elif month == 12 and day > 23:
#         print(zodiac_name[0])
#         break
while True:
    year = int(input('请输入年份'))
    month = int(input('请输入月份'))
    day = int(input('请输入日'))
    print('%s年的生肖是%s' %(year, zodiac[year % 12]))
    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1
    print(zodiac_name[n])

    cz_num[zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    for cz_key in cz_num.keys():
        print("生肖%s有个%s" %(cz_key, cz_num[cz_key]))

    for z_key in z_num.keys():
        print("星座%s有个%s" %(z_key, z_num[z_key]))