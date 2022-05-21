import time

def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('程序运行了%s秒' %(end_time - start_time))
    return wrapper

@timmer
def i_can_sleep():
    time.sleep(3)

# start_time = time.time()
# i_can_sleep()
# end_time = time.time()
# print("程序运行了%s秒" %(end_time - start_time))



# num = timmer(i_can_sleep)
# num()

i_can_sleep()