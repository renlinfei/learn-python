import threading
from threading import current_thread
from queue import Queue
import time
import random

queue = Queue(5)

class Producer(threading.Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者-%s 生产了数据 %s' %(name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者-%s 休眠了 %s秒' %(name, t))


class Consumer(threading.Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者-%s 消费了数据 %s' %(name, num))
            t = random.randint(1, 10)
            time.sleep(t)
            print('消费者-%s 休眠了 %s秒' %(name, t))

p1 = Producer(name='p1')
p2 = Producer(name='p2')
p1.start()
p2.start()

c1 = Consumer(name = 'c1')
c2 = Consumer(name = 'c2')
c3 = Consumer(name = 'c3')
c1.start()
c2.start()
c3.start()

