#join()阻塞 py3.x
import queue,time,threading
"""Return the CPU time or real time since the start of the process or since
    the first call to clock().  This has as much precision as the system
    records."""
start = time.clock()

def worker(m):
	time.sleep(1)
	print('worker',m)



if __name__ == '__main__':
	threads = []
	for i in range(5):
		threads.append(threading.Thread(target=worker,args=(i,)))
	for t in threads:
		t.start()
		t.join()#阻塞子程序（如何不要阻塞子程序，请删除该行）

	# t.join()#阻塞父程序（如果不要阻塞父程序，请删除该行）

	end = time.clock()
	print("finished: %0.3fs" % (end-start))