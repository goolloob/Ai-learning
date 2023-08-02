import multiprocessing
import time

class Mycalss(multiprocessing.Process): # 将其模块作为父类传入
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print(f'我是进程{self.name}')
        time_class()
        print(f'结束进程{self.name}')

#
def time_class():
    for i in range(5):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    x1 = Mycalss(name = '1')
    x2 = Mycalss(name = '2')
    x1.start()
    x2.start()
    x1.join()
    x2.join()
