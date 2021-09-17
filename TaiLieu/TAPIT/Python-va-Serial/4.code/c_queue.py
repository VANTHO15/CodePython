import queue
import random
from threading import Thread
import time

# data = []
#
#
# def create_data():
#     global data
#     while True:
#         data.append(random.randint(1, 100))
#         time.sleep(0.1)
#
#
# Thread(target=create_data).start()
# sum_ = 0
# while True:
#     sum_ += data.pop()
#     print(sum_)


data = queue.Queue()


def create_data():
    global data
    while True:
        data.put(random.randint(1, 10))
        time.sleep(0.1)


Thread(target=create_data).start()
sum_ = 0
while True:
    sum_ += data.get()
    print(sum_)


