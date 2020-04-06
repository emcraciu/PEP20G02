"""Cum executam bucati de cod care sunt blocking"""

from threading import Thread
from time import sleep


def do_nothing(wait: int):
    print('before sleep')
    sleep(wait)
    print('after sleep')


process = Thread(target=do_nothing, args=(10,))
print('Start my code')
process.start()
print('Stop my code')
process.join()
