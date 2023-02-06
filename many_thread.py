import threading
import time
from datetime import datetime

from main import read, process, show, now_time

t1 = threading.Thread(target=read)
t2 = threading.Thread(target=process)
t3 = threading.Thread(target=show)

t1.start()
t2.start()
t3.start()



finish = datetime.now()
print('Значиние многопоточки:', finish-now_time)