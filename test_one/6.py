#使用多个进程池 py3
"""多次执行（屏蔽sleep的），会发现有时一样，有时不一样。
而如果把sleep换成更复杂的执行过程，如，那么执行结果pid都不是一样的，
说明屏蔽了sleep以后，执行完了，
另外一个进程才刚开始执行，正好用刚才那个进程释放掉的进程号"""
import multiprocessing
import os,time,random

def Lee():
    print("\nRun task Lee-%s" %(os.getpid()))#os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(random.random() * 10) #random.random()随机生成0-1之间的小数
    end = time.time()
    print('Task Lee, runs %0.2f seconds.' %(end - start))

def Marlon():
    print("\nRun task Marlon-%s" %(os.getpid()))
    start = time.time()
    time.sleep(random.random() * 40)
    end=time.time()
    print('Task Marlon runs %0.2f seconds.' %(end - start))

def Allen():
    print("\nRun task Allen-%s" %(os.getpid()))
    start = time.time()
    time.sleep(random.random() * 30)
    end = time.time()
    print('Task Allen runs %0.2f seconds.' %(end - start))

def Frank():
    print("\nRun task Frank-%s" %(os.getpid()))
    start = time.time()
    time.sleep(random.random() * 20)
    end = time.time()
    print('Task Frank runs %0.2f seconds.' %(end - start))

if __name__ == '__main__':
    function_list = [Lee,Marlon,Allen,Frank]
    print("parent process %s" %(os.getpid()))
    pool = multiprocessing.Pool(processes=4)
    for func in function_list:
        pool.apply_async(func)#pool执行函数，apply执行函数，当有一个进程执行完毕后，会添加一个新的进程到pool中
    print("waiting for all subprocesses done")
    pool.close()
    pool.join()#调用join之前，一定要想调用close函数，否则会出错，close（）执行后不会 有新的进程加入到pool，join函数等待所有子进程结束
    print('all subprocesses done')

