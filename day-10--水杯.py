'''
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体

'''
class Cup:
    __height = 0
    __cubage = 0
    __colour = ""
    __texture = ""

    def setHeight(self,height):
        if height > 60 or height < 5:
            print("没有这款水杯")
        else:
            self.__height = height

    def steCubage(self,cubage):
        if cubage > 5 or cubage < 0.5:
            print("没有这个容量的水杯")
        else:
            self.__cubage = cubage

    def setClour(self,clour):
        self.__colour = clour

    def getClour(self):
        return self.__colour

    def setTexture(self,texture):
        self.__texture = texture


    def deposit(self,liquidnaem):
        print("高度为",self.__height,"cm,容积为",self.__cubage,"l,颜色为",
              self.__colour,"材质为",self.__texture,"能存放",liquidnaem,"的大水杯子")

c = Cup()

c.setHeight(12)
c.steCubage(1)
c.setClour("黄色")
c.setTexture("玻璃")

c.deposit("液体")

b = c.getClour()
print(b)







