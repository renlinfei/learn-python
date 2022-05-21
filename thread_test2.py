import threading

class My_Thread(threading.Thread):
    def run(self):
        print(threading.current_thread().getName(), 'start')
        print('run')
        print(threading.current_thread().getName(), 'end')

t1 = My_Thread()
t1.start()
t1.join()
print(threading.current_thread().getName(), 'end')