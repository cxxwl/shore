'''
生产消费模型
    面包篮子：容量为500，
    面包：3元一个
    厨师：三个厨师同时在造面包，当篮子的面包为500时，厨师稍等2秒，然后判断篮子是否已满，若不满继续造
    客户：六个客户3000元，同时在抢面包，当篮子的面包不够的时候，稍等2秒，然后再去买。一直到3000元花光
'''
from threading import Thread
import time

bread = 0
price = 3
money = 3000


class chef(Thread):
    c_name = ""
    c_count = 0

    def run(self) -> None:
        while True:
            global bread
            global c_count
            if bread < 500 or bread >= 0:
                bread = bread + 1
                self.c_count = self.c_count + 1
                print(self.c_name, "做了", self.c_count, "个面包")
            elif bread == 500:
                time.sleep(2)


class People(Thread):
    k_name = ""
    k_count = 0

    def run(self) -> None:
        while True:
            global bread
            global money
            global k_count
            if bread > 0:
                bread = bread - 1
                self.k_count = self.k_count + 1
                money = money - 3
                print(self.k_name, "买了", self.k_count, "个面包")
                if money <= 0:
                    print("没钱了")
                    break
            elif bread == 0:
                time.sleep(2)


c1 = chef()
c2 = chef()
c3 = chef()

c1.c_name = "彭祖"
c2.c_name = "伊尹"
c3.c_name = "易牙"

c1.start()
c2.start()
c3.start()

k1 = People()
k2 = People()
k3 = People()
k4 = People()
k5 = People()
k6 = People()

k1.k_name = "客户a"
k2.k_name = "客户b"
k3.k_name = "客户c"
k4.k_name = "客户d"
k5.k_name = "客户e"
k6.k_name = "客户f"

k1.start()
k2.start()
k3.start()
k4.start()
k5.start()
k6.start()
