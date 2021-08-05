'''姐就是女王:
随机选择人物： 1、普通没有技能
2、稀有英雄初始值为30。3、传奇英雄不会减少只会增加
需求：
初始值为：10
随机生成三个数字
随机选择一个数字
选择的数字和初始值进行计算（随机加减）
计算过后大于100则任务成功
计算过后小于或等于0则任务失败
'''
import random
list1=["普通","稀有","传奇"]
geshu=len(list1)
#print(num)
jiaobiao=random.randint(0,geshu-1)
#print(a)
name=list1[jiaobiao]
print("选手名字:",name)
num=50
if name == "普通":
    while True:
        i = 0
        list_p1 = []
        while i < 3:
            i = i + 1
            a=random.randint(20,60)
            list_p1.append(a)
        print("循环的分数:",list_p1)
        num_p=list_p1[random.randint(0,len(list_p1)-1)]
        print("三选一的数:",num_p)
        list_p2=[1,2]
        name_p=list_p2[random.randint(0,len(list_p2)-1)]
        print("选择1or2:",name_p)
        if name_p==1 :
            num=num_p+num
            print("相加后的",num)
        elif name_p==2 :
            num=num_p-num
            print("相减后的",num)
        if num>100:
            print("恭喜你！你赢了，你的分数为",num)
            break
        elif num < 100:
            print("很抱歉！你输了，你的分数为", num)
            break
if name == "稀有":
    while True:
        i = 0
        list_x1 = []
        while i < 3:
            i = i + 1
            a = random.randint(20, 60)
            list_x1.append(a)
        print("循环的分数:", list_x1)
        num_x = list_x1[random.randint(0, len(list_x1) - 1)]
        print("三选一的数:", num_x)
        list_x2 = [1, 2]
        name_x = list_x2[random.randint(0, len(list_x2) - 1)]
        print("选择1or2:", name_x)
        if name_x == 1:
            num = num_x + num
            print("相加后的",num)
        elif name_x == 2:
            num = num_x - num
            print("相减后的",num)
        if num > 100:
            print("恭喜你！你赢了，你的分数为",num)
            break
        elif num < 100:
            print("很抱歉！你输了，你的分数为",num)
            break

if name == "传奇":
    while True:
        i = 0
        list_c1 = []
        while i < 3:
            i = i + 1
            a = random.randint(20, 60)
            list_c1.append(a)
        print("循环的分数:", list_c1)
        num_c = list_c1[random.randint(0, len(list_c1) - 1)]
        print("三选一的数:", num_c)
        list_c2 = [1]
        name_c = list_c2[random.randint(0, len(list_c2) - 1)]
        print("选择1or2:", name_c)
        if name_c == 1:
            num = num_c + num
            print("相加后的",num)

        if num > 100:
            print("恭喜你！你赢了，你的分数为",num)
            break
        elif num < 100:
            print("很抱歉！你输了，你的分数为",num)
            break
