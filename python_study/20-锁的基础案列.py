# 线程锁
# import threading

# def worker(lock, data):
#     with lock:
#         print(f"Thread {threading.current_thread().name} is working on {data}")

# if __name__ == "__main__":
#     data_list = ["A", "B", "C"]
#     lock = threading.Lock()

#     threads = [threading.Thread(target=worker, args=(lock, data)) for data in data_list]

#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()
#

# 进程锁
import multiprocessing

def worker(lock, data):
    with lock:
        print(f"Process {multiprocessing.current_process().name} is working on {data}")

if __name__ == "__main__":
    data_list = ["A", "B", "C"]
    lock = multiprocessing.Lock()

    processes = [multiprocessing.Process(target=worker, args=(lock, data)) for data in data_list]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

