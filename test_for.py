zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
               u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

alist = [i * i for i in range(1, 11) if (i % 2) == 0]
print(alist)

zc_num = { i:0 for i in zodiac_name}
print(zc_num)