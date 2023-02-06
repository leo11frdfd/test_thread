import time
from datetime import datetime

from main import read, process, show, now_time

read()
process()
show()

finish = datetime.now()
print('Значиние многопоточки:', finish-now_time)