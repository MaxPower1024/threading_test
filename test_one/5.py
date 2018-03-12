#使用进程池，并且关注结果 py3
import multiprocessing
import time

def func(msg):
    print("msg:",msg)
    time.sleep(3)
    print("end")
    return "done" + msg

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    result = []
    for i in range(4):
        msg = 'hello %d '% (i)
        result.append(pool.apply_async(func,(msg,)))
    pool.close()
    pool.join()#主程序在pool.join（）处等待各个进程的结束
    for re in result:
        print(":::",re.get())
    print("sub-processes done")

