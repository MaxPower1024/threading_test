# python3.x
#判断是否有余票，然后加上互斥锁，这样不会造成一个线程刚判断没有余票，而另一个线程就执行买票操作
import threading
import time
import os
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()#加锁
        if i != 0:
            i =i - 1
            print("窗口：",tid,",剩余票数: ",i)
            time.sleep(0.1)
        else:
            print("窗口：",tid,"No more tickets")
            os._exit(0)
        lock.release()#解锁
        time.sleep(0.1)

i = 43
lock = threading.Lock()
for k in range(1,10):
    new_thread = threading.Thread(target=booth,args=(k,))#传参数需要加一个“，”这样不会报错,创建线程
    new_thread.start()
    # booth(k)
    # print(k)


