import threading
import time

def my_job():
	print(threading.current_thread().name)

t=threading.Thread(target=my_job)
t.start()
