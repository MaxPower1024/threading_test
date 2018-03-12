#使用进程池（阻塞）py3
import multiprocessing
import time

def func(msg):
    print("msg:",msg)
    time.sleep(3)
    print("end")

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in range(4):
        msg = "hello %d " % (i)
        pool.apply(func,(msg,))
    print('mark-----')
    pool.close()
    pool.join()#
    print("sub-processes done")
