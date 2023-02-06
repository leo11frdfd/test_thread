import logging
import threading
from datetime import datetime
from time import sleep
import time

now_time = datetime.now()

def read():
    global a,b
    print("Thread read: starting")
    a = 4
    b = 5
    time.sleep(9)
    print("Thread read: finishing")


def process():
    global c
    print("Thread process: starting")
    c = a + b
    time.sleep(7)
    print("Thread process: finishing")

def show():
    print("Thread show: starting")
    time.sleep(2)
    print("Thread show: finishing")






















