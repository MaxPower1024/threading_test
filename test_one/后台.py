#  encoding:utf-8
import threading,time
import os

def worker():
	time.sleep(2)
	print("worker")

t = threading.Thread(target=worker)
t.setDaemon(True)#后台运行线程
t.start()
print(os.getpid())#获取当前线程
# t.join()
print('haha')