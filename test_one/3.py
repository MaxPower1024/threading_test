#使用进程池(非阻塞） py3
"""
创建一个进程池pool，并设定进程的数量为3，
range(4)会相继产生四个对象[0, 1, 2, 4]，
四个对象被提交到pool中，因pool指定进程数为3,
所以0、1、2会直接送到进程中执行，当其中一个执行完事后才空出一个进程处理对象3，
所以会出现输出“msg: hello 3”出现在"end"后。因为为非阻塞，主函数会自己执行自个的，不搭理进程的执行，
所以运行完for循环后直接输出“mMsg: hark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~”，主程序在pool.join（）处等待各个进程的结束。
"""
import multiprocessing
import time
def func(msg):
    print('msg:',msg)
    time.sleep(3)
    print('end')

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)#设置进程总数为3
    for i in range(4):
        msg = "hello %d " %(i)
        pool.apply_async(func,(msg,))
    print("mark---------")
    pool.close()
    pool.join()#主程序在pool.join（）处等待各个进程的结束
    print("sub-process(es) done")
