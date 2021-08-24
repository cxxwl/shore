'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），
行为（打字，打游戏，看视频）
'''


class Notebook:
    __size = 0
    __price = 0
    __cpu = ""
    __memory = 0
    __stand = 0

    def setSize(self, size):
        if size > 100 or size < 10:
            print("没有该尺寸的")
        else:
            self.__size = size

    def setPrice(self, price):
        if price <= 0:
            print("价格不能为0")
        else:
            self.__price = price

    def setCpu(self, cpu):
        self.__cpu = cpu

    def setMemory(self, memory):
        if memory > 500 or memory < 100:
            print("没有这个容量内存")
        else:
            self.__memory = memory

    def setStand(self, stand):
        if stand > 24:
            print("待机时长没有那么长")
        else:
            self.__stand = stand


    def Type(self,type):
        print("这台机子能", type)

    def PlayGames(self,playgames):
        print("这台机子能",playgames)

    def WatchVideo(self,watchvideo):
        print("这台机子能",watchvideo)


    def ShowIt(self):
        print("这台尺寸为",self.__size,"寸，价格为",self.__price,"元，cpu为",self.__cpu,"内存为",self.__memory,"G，待机时长为",self.__stand,
              "小时，的笔记本电脑")

n = Notebook()

n.setSize(22)
n.setPrice(8000)
n.setCpu("2050Ti")
n.setMemory(500)
n.setStand(24)

n.Type("打字")
n.PlayGames("打游戏")
n.WatchVideo("看视频")


n.ShowIt()

















