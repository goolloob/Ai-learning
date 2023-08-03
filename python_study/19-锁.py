"""
锁的种类
    Lock(互斥锁):最基本的锁类型,用于互斥访问共享资源。每次只能有一个线程持有该锁。
    RLock(递归锁):也称为可重入锁,允许同一个线程多次获取该锁而不会产生死锁。持有锁的线程可以多次获取它,但释放次数必须与获取次数匹配。
    Semaphore(信号量):用于控制同时访问某个资源的线程或进程的数量。持有计数器表示可以同时获取锁的线程或进程的数量。
    Event:线程间通信的同步原语。允许一个线程等待另一个线程发出信号,然后再继续执行。
    Condition:基于锁的条件变量。允许一个线程等待特定条件的发生,并在条件满足时被唤醒。
其他锁的变体和高级同步原语
    BoundedSemaphore:有界信号量,类似于 Semaphore,但在计数器达到上限时,不能继续增加。
    ThreadLocal:线程本地存储,允许每个线程拥有自己独立的变量,这些变量对其他线程不可见。
    Barrier:屏障,用于在多个线程中同步达到某个点再一起继续执行。
    Timer:计时器,用于创建一个在指定时间后执行特定操作的线程。
    Semaphore、BoundedSemaphore 和 Event 的派生类:可以基于这些锁创建自定义的同步原语。
"""

"""
死锁
    死锁(Deadlock)是多线程或多进程并发编程中的一种常见问题,
    它发生在两个或多个线程(或进程)相互等待对方释放资源,
    从而导致所有线程(或进程)都无法继续执行的情况。
死锁通常由以下四个条件导致:
    互斥条件(Mutual Exclusion):每个资源同时只能被一个线程(或进程)占用。
    请求与保持条件(Hold and Wait):一个线程(或进程)在持有某个资源的同时,又请求其他资源。
    不剥夺条件(No Preemption):资源只能在线程(或进程)自愿释放,其他线程(或进程)不能强制剥夺该资源。
    环路等待条件(Circular Wait):一组线程(或进程)形成循环等待其他线程(或进程)所持有的资源。
    当这四个条件同时满足时,就有可能发生死锁。一旦死锁发生,各个线程(或进程)会陷入无限等待状态,无法继续执行,从而导致整个程序或系统无法正常工作。
解决死锁问题的方法通常包括以下几种:
    死锁预防(Deadlock Prevention):通过破坏死锁发生的四个条件之一,来预防死锁的发生。例如,一次性获取所有资源,避免持有部分资源后再去请求其他资源；或者引入资源优先级,确保资源分配的有序性。
    死锁避免(Deadlock Avoidance):通过运行时动态地检测资源的分配状态,避免分配资源后可能导致死锁的情况。这需要使用某种算法来预测资源请求的安全性。
    死锁检测与恢复(Deadlock Detection and Recovery):在程序运行时,周期性地检测是否存在死锁。一旦检测到死锁,系统可以采取恢复措施,例如中止某些进程,释放资源,从而解除死锁状态。
    资源剥夺(Resource Preemption):作为最后的手段,在发生死锁时,系统可以选择强制剥夺某些进程的资源,以解除死锁状态。被剥夺资源的进程会被中止或被暂停,直到死锁解除为止。
    死锁是一个复杂且棘手的并发编程问题,避免死锁需要合理设计资源分配策略和加锁顺序,并且需要充分理解程序中资源的依赖关系和互斥访问情况
"""
#
# 死锁案列(线程中生效)
import threading

# 创建两个互斥锁
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_one():
    lock1.acquire()
    print("Thread One acquired lock1.")
    # 等待一段时间，模拟线程间的竞争条件
    import time
    time.sleep(1)
    lock2.acquire()
    print("Thread One acquired lock2.")
    # 释放锁
    lock1.release()
    lock2.release()

def thread_two():
    lock2.acquire()
    print("Thread Two acquired lock2.")
    # 等待一段时间，模拟线程间的竞争条件
    import time
    time.sleep(1)
    lock1.acquire()
    print("Thread Two acquired lock1.")
    # 释放锁
    lock2.release()
    lock1.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_one)
    t2 = threading.Thread(target=thread_two)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序执行完毕。")





