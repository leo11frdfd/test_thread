import threading
import time
from datetime import datetime
from main import read, process, show, now_time

global t
t = [0, 0, 0]


def start_threads():
    name_process = [read, process, show]
    print(name_process)
    for i in range(len(name_process)):
        t[i] = threading.Thread(target=name_process[i])
        t[i].start()


def join_threads():
    name_process = [read, process, show]
    for i in range(len(name_process)):
        t[i].join()


start_threads()
join_threads()

finish = datetime.now()
print('Значиние многопоточки:', finish - now_time)
