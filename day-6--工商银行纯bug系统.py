import random
print("**************************************************")
print("*                   中国工商银行                   *")
print("*                   账户管理系统                   *")
print("*                      v1.0                      *")
print("**************************************************")
print("                                                  ")
print("*1.开户                                           *")
print("*2.存钱                                           *")
print("*3.取钱                                           *")
print("*4.转账                                           *")
print("*5.查询                                           *")
print("*6.Bye！                                          *")
print("**************************************************")


# 1.开户
bank={}
bank_name="中国工商银行昌平支行"
def bank_add(account,username,password,country,province,street,door):
    if len(bank)>100:
        return 3
    if username in bank :
        return 2
    bank[username]={
        "account":account,
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "money":0,
        "door":door
    }
    return 1


def kaihu_add():
    account=random.randint(10000000,99999999) #账户随机生成8位数
    username=input("请输入用户名")
    password=input("请输入密码")
    print("请输入你的详细资料：")
    country=input("请输入国家")
    province=input("请输入省份")
    street=input("请输入街道")
    door=input("请输入门牌号")
    opening_bank = bank_add(account,username,password,country,province,street,door)
    if opening_bank == 3:
        print("对不起，该支行用户已满，请到其他银行开户！")
    if opening_bank == 2:
        print("对不起，该用户已存在！")
    if opening_bank == 1:
        print("开户成功！以下是你的基本信息：")
        info = '''
          ------------个人信息------------
            用户名:%s
            账号：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info%(username,account,country,province,street,door,bank[username]["money"],bank_name))


# 2.存钱
bank2={"account":"11","password":"123456","money":10}


def cunqian():
    account=input("请输入您的账号：")
    if account == bank2["account"]:
        print("账户正确，请进行下一步")
        password=input("请输入密码：")
        if password == bank2["password"]:
            print("密码正确，进行下一步")
            save_money=input("请输入存款数额：")
            if save_money > "0":
                money=bank2["money"]+int(save_money)
                print("您的账户余额为",money,"元")
            else:
                print("存款金额不能为零")
        else:
            print("密码输入错误")
    else:
        print("账号输入错误")
        return False


#  3.取钱
bank3={"username":{"account":"1","password":"123456","money":100}}


def user_qu(account):
    if account == bank3["username"]["account"]:
        return 0
    else:
        return 1
def mm_qu(password):
    if password == bank3["username"]["password"]:
        return 0
    else:
        return 2
def rmb1(money_qu):
    if money_qu <= bank3["username"]["money"]:
        bank3["username"]["money"]=bank3["username"]["money"]-int(money_qu)
        return 0
    else:
        return 3

def quqian():
    account=input("请输入您的账户：")
    name1=user_qu(account)
    if name1 == 0:
        print("账号正常，进行下一步")
        password=input("请输入密码：")
        name2=mm_qu(password)
        if name2 == 0:
            print("密码正确，进行下一步")
            money_qu=int(input("请输入取钱金额：")) # int类型
            name3=rmb1(money_qu)
            if name3 == 0:
                print("取钱成功，剩余",bank3["username"]["money"],"元")  #
            else:
                print("账户余额不足")
        else:
            print("密码错误")
    else:
        print("账户不存在")


# 4.转账
bank_zz={"username1":{"account_chu":"1","password":"123456","money":100},
      "username2":{"account_ru":"2"}
}
def user(account_chu,account_ru):
    if account_chu == bank_zz["username1"]["account_chu"] and account_ru == bank_zz["username2"]["account_ru"]:
    # if all([account_chu == bank["username1"]["account_chu"], account_ru == bank["username1"]["account_ru"]]):
        return 0
    else:
        return 1
def mm(password):
    if password == bank_zz["username1"]["password"]:
        return 0
    else:
        return 2
def rmb(money_chu):
    if money_chu > bank_zz["username1"]["money"]: # 转出去的钱大于账户余额，返回值3
        return 3
    else:
        bank_zz["username1"]["money"] = bank_zz["username1"]["money"] - int(money_chu)
        return 0


def zhuanzhang():
    account_chu=input("请输入您的账号：")
    account_ru = input("请输入转入账号：")
    name=user(account_chu,account_ru)
    if name == 0:
        print("账号正确，请进行下一步")
        password=input("请输入密码：")
        name2=mm(password)
        if name2 == 0:
            print("密码正确，进行下一步")
            money_chu=int(input("请输入转账金额："))  # int类型
            name3=rmb(money_chu)
            if name3 == 0:
                print("转账成功！账户余额",bank["username1"]["money"],"元")
            else:
                print("账户余额不足")
        else:
            print("密码错误，请重新输入")
    else:
        print("账号不存在")


# 5.查询
bank5 = {"username": {"account": "1",
                      "password": "123456"
                      }
         }


def chaxun():
    account = input("请输入您的账号：")
    if account == bank5["username"]["account"]:
        print("账号正确，请进行下一步")
        password = input("请输入密码：")
        if password == bank5["username"]["password"]:
            info = '''
                ----------个人信息详情--------
                    账户：%s
                    密码：%s

                    '''
            print(info % ("account", "password"))
        else:
            print("密码不正确")
    else:
        print("该用户不存在")


while True :
    print("业务选项：1.开户 2.存钱 3.取钱 4.转账 5.查询 6.Bye! ")
    a=input("请选择你要办理的业务")
    if a== "1":
        kaihu_add()
        print(bank)
    elif a == "2":
        cunqian()
    elif a=="3":
        quqian()
    elif a=="4":
        zhuanzhang()
    elif a=="5":
        chaxun()
    elif a=="6":
        print("Bay！")
        break
    else:
        print("请重新选择你要办理的业务！")
        break























