"""
    进程与线程之间通信可以通过多种机制实现,这些机制既包括线程间通信(Thread Inter-Process Communication,TIPC),
    也包括进程间通信(Inter-Process Communication,IPC)。
    线程间通信主要用于在多线程程序中实现数据共享和协作,
    而进程间通信用于在多进程程序中实现数据交换和协作。
以下是进程与线程间通信的几种常见机制:
    队列(Queue):队列是一种线程安全的数据结构,可用于在进程和线程之间传递数据。
        在 Python 中,multiprocessing.Queue 用于进程间通信,queue.Queue 用于线程间通信。
    共享内存(Shared Memory):共享内存是一种内存区域,允许多个进程或线程共享数据。
        Python 的 multiprocessing.Value 和 multiprocessing.Array 可以实现进程间共享内存,而 multiprocessing.shared_memory 提供了更高级的共享内存支持。
    管道(Pipe):管道是一种单向通信机制,可在父进程与子进程之间传递数据。在 Python 中,multiprocessing.Pipe 用于进程间通信。
    文件(File):进程和线程可以通过读写共享文件来进行通信。Python 的文件操作可以实现这种通信方式。
    信号量(Semaphore)和事件(Event):信号量和事件是一种用于线程间通信的同步原语。Python 提供了 threading.Semaphore 和 threading.Event 来实现线程间通信。
    进程锁(Lock)和线程锁(Lock):锁是一种用于保护共享资源的同步原语,可以避免多个进程或线程同时访问共享资源。Python 的 multiprocessing.Lock 用于进程间通信,threading.Lock 用于线程间通信。
    请注意,进程间通信需要考虑到进程之间独立的内存空间和资源隔离,而线程间通信则需考虑到多线程共享同一进程的内存空间和资源。因此,在实现进程与线程间通信时,需要根据具体情况选择适当的通信机制,并合理规划数据共享和同步操作,以确保通信的正确性和效率。
"""

import multiprocessing
import threading
import random
import time
from queue import Queue


def random_generator(queue):
    while True:
        num = random.randint(1, 100)
        queue.put(num)
        print(f"Generated random number: {num}")
        time.sleep(1)


def consumer(queue, stop_event):
    while not stop_event.is_set():
        try:
            num = queue.get(timeout=1)
            print(f"Received random number from queue: {num}")
        except Exception as e:
            pass


if __name__ == "__main__":
    queue = Queue()
    stop_event = threading.Event()

    process1 = multiprocessing.Process(target=random_generator, args=(queue, ))
    process2 = multiprocessing.Process(target=consumer,
                                       args=(queue, stop_event))

    process1.start()
    process2.start()

    # 让线程定时设置事件,用于停止进程运行
    def stop_process():
        time.sleep(5)
        stop_event.set()

    thread = threading.Thread(target=stop_process)
    thread.start()

    process1.join()
    process2.join()
    thread.join()

    print("程序执行完毕。")
