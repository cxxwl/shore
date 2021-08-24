'''
人类：
属性:
姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机时长，所拥有的积分。
功能：
发短信（要求参数传入短信内容）。
打电话（要求传入要打的电话号码和要打的时间长度。
程序里判断号码是否为空或者本人的话费是否小于1元，若为空或者小于1元则报相对应的错误信息，否则的话拨通。
结束后，按照时间长度扣费并返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟））

'''


class People:
    __name = ""
    __sex = ""
    __age = 0
    __telephoneCharge = ""
    __brand = ""
    __batteryCapacity = ""
    __size = ""
    __standByTime = ""
    __integral = ""

    def setName(self, name):
        self.__name = name

    def setSex(self, sex):
        if sex == "男":
            self.__sex = sex
        elif sex == "女":
            self.__sex = sex
        else:
            print("搞什么！男女不分")

    def setAge(self, age):
        if age > 120 or age < 0:
            print("你成神了，跳出三界了")
        else:
            self.__age = age

    def setTelephoneCharge(self, telephoneCharge):
        self.__telephoneCharge = telephoneCharge

    def setBrand(self, brand):
        self.__brand = brand

    def setBatteryCapacity(self, batteryCapacity):
        if batteryCapacity > 5000 or batteryCapacity < 0:
            print("我们没有这款容量的手机")
        else:
            self.__batteryCapacity = batteryCapacity

    def setSize(self, size):
        if size > 6 or size < 3.5:
            print("没有这个尺寸的手机")
        else:
            self.__size = size

    def setStandByTime(self, standByTime):
        if standByTime > 24 or standByTime < 12:
            print("待机时长不对")
        else:
            self.__standByTime = standByTime

    def setIntegral(self, integral):
        if integral < 0:
            print("积分不能为负数")
        else:
            self.__integral = integral

    def showit(self):
        print("一个名叫", self.__name, "的", self.__sex, "生，芳龄", self.__age, "。她有一个",
              self.__brand, "牌的手机，电池容量为", self.__batteryCapacity, "毫安，屏幕尺寸为", self.__size, "英寸，待机时长为",
              self.__standByTime, "小时，积分为", self.__integral, "，话费余额为", self.__telephoneCharge, "元.")

    import random

    a = "182"
    b = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(8):
        index = random.randint(0, len(b) - 1)
        a = a + b[index]

    def call(self, phonenumber, time):
        if phonenumber != a:
            print("号码为空，重新拨号")
        elif self.__telephoneCharge <= 0:
            print("余额不足")
        else:
            print("正在拨打中")
            print("......")
            # 0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，其他：0.65元/钟、48个积分/钟）
            if time > 0 and time <= 10:
                c1 = time * 1
                self.__telephoneCharge -= c1
                i1 = time * 15
                self.__integral += i1
                print("通话", time, "分钟", "花费", c1, "元，剩余话费", self.__telephoneCharge, "元。积分增加", i1, "剩余积分",
                      self.__integral)
            elif time > 10 and time <= 20:
                c2 = time * 0.8
                self.__telephoneCharge -= c2
                i2 = time * 39
                self.__integral += i2
                print("通话", time, "分钟", "花费", c2, "元，剩余话费", self.__telephoneCharge, "元。积分增加", i2, "剩余积分",
                      self.__integral)
            else:
                c3 = time * 0.65
                self.__telephoneCharge -= c3
                i3 = time * 48
                self.__integral += i3
                print("通话", time, "分钟", "花费", c3, "元，剩余话费", self.__telephoneCharge, "元。积分增加", i3, "剩余积分",
                      self.__integral)


import random

a = "182"
b = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for i in range(8):
    index = random.randint(0, len(b) - 1)
    a = a + b[index]

p = People()
p.setName("小宝贝")
p.setAge(18)
p.setSex("女")

p.setTelephoneCharge(110)
p.setBrand("华为")
p.setBatteryCapacity(4500)
p.setSize(5.0)
p.setStandByTime(12)
p.setIntegral(10)
p.showit()
p.call(a,30)