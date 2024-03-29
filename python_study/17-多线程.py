"""
多线程类似于同时执行多个不同程序,多线程运行有如下优点：

使用线程可以把占据长时间的程序中的任务放到后台去处理。
用户界面可以更加吸引人,比如用户点击了一个按钮去触发某些事件的处理,可以弹出一个进度条来显示处理的进度。
程序的运行速度可能加快。
在一些等待的任务实现上如用户输入、文件读写和网络收发数据等,线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。
每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行,必须依存在应用程序中,由应用程序提供多个线程执行控制。

每个线程都有他自己的一组CPU寄存器,称为线程的上下文,该上下文反映了线程上次运行该线程的CPU寄存器的状态。

指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器,线程总是在进程得到上下文中运行的,这些地址都用于标志拥有线程的进程地址空间中的内存。

线程可以被抢占（中断）。
在其他线程正在运行时,线程可以暂时搁置（也称为睡眠） -- 这就是线程的退让。
线程可以分为:

内核线程：由操作系统内核创建和撤销。
用户线程：不需要内核支持而在用户程序中实现的线程。
Python3 线程中常用的两个模块为：

_thread
threading(推荐使用)
thread 模块已被废弃。用户可以使用 threading 模块代替。所以,在 Python3 中不能再使用"thread" 模块。为了兼容性,Python3 将 thread 重命名为 "_thread"
"""

# import threading # 导入线程模块

"""
Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

_thread 提供了低级别的、原始的线程以及一个简单的锁,它相比于 threading 模块的功能还是比较有限的。

threading 模块除了包含 _thread 模块中的所有方法外,还提供的其他方法：

threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前,不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量,与len(threading.enumerate())有相同的结果。
除了使用方法外,线程模块同样提供了Thread类来处理线程,Thread类提供了以下方法:

run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
"""


import threading
import time


exitnum = 0

class Myclass(threading.Thread):
    def __init__(self,threadingID,name,day):
        threading.Thread.__init__(self)
        threadingID = threadingID
        self.name = name
        self.day = day

    def run(self): # 函数名称必须为run才能start启动
        print('开始线程',self.name)
        print_time(self.name,self.day,5)
        print('退出线程',self.name)
#

def print_time(threadName, delay, counter):
    while counter:
        if exitnum:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


if __name__ == "__main__":
    x1 = Myclass(1,'ID1',1)
    x2 = Myclass(2,'ID2',2)
    x1.start() # 调用类中的run方法
    x2.start()
    x1.join() # 关闭线程
    x2.join()

"""
关于一个进程能创建多少线程
https://zhuanlan.zhihu.com/p/387673151
"""