import threading
from threading import current_thread
import time

def myThread(arg1, arg2):
    print('%s start' %current_thread().getName())
    time.sleep(1)
    print('%s %s' %(arg1, arg2))
    print('%s end' % current_thread().getName())

for i in range(1, 6, 1):
    # myThread(i, i + 1)
    t1 = threading.Thread(target=myThread, args=(i, i + 1))
    t1.start()
print('%s end' %current_thread().getName())
