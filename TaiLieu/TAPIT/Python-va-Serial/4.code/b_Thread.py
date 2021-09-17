import threading
import time


def print_cube(x):
    while True:
        y = x * x * x
        print('Cube: {}'.format(y))
        time.sleep(0.5)


def print_square(x):
    while True:
        y = x * x
        print('Square: {}'.format(y))
        time.sleep(0.5)


t1 = threading.Thread(target=print_cube, args=(10, ))
t2 = threading.Thread(target=print_square, args=(10, ))
t1.start()
t2.start()



