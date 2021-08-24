import random
from DB import update
from DB import select

bank_name = "中国工商银行昌平支行"


def bankadd(account, username, password, country, province, street, door):
    sql = "select count(*) from user"
    data = select(sql, [])
    if data[0][0] >= 100:
        return 3
    sql1 = "select * from user where account = %s"
    data1 = select(sql1, account)
    if len(data1) != 0:
        return 2
    sql2 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s) "
    param2 = [account, username, password, country, province, street, door, 0, bank_name]
    update(sql2, param2)
    return 1


# 开户
def useradd():
    account = random.randint(10000000, 99999999)
    username = input("请输入用户名：")
    password = input("请输入密码：")
    country = input("\t国家:")
    province = input("\t省份：")
    street = input("\t街道：")
    door = input("\t门牌号：")
    a = bankadd(account, username, password, country, province, street, door)
    if a == 3:
        print("用户已满！抱歉！")
    elif a == 2:
        print("用户已存在")
    elif a == 1:
        print("恭喜开户成功！")
        info = '''
                  ------------个人信息----------------
                  账号：%s,
                  用户名：%s,
                  取款密码：%s,
                  地址信息：
                      国家：%s,
                      省份：%s,
                      街道：%s,
                      门牌号：%s,
                  余额：%s,
                  开户行：%s
                  -----------------------------------
              '''
        print(info % (account, username, password, country, province, street, door, 0, bank_name))


# 存钱
def saveadd():
    account = input("请输入账号：")
    sqls = "select * from user where account = %s"
    s = select(sqls, account)
    if len(s) != 0:
        print("进行下一步")
        moneys = int(input("请输入存款金额："))
        sqls1 = "update user set money = money + %s where account = %s "
        params = [moneys, account]
        update(sqls1, params)
        sqls2 = "select money from user where account = %s"
        s2 = select(sqls2, account)
        moneys2 = s2[0][0]
        print("存款成功，余额为", moneys2, "元")
    else:
        print("账号错误")
        return False


# 取钱
def drawadd():
    account = input("请输入账号：")
    sqld = "select * from user where account = %s"
    d = select(sqld, account)
    if len(d) != 0:
        print("下一步")
        password = input("请输入密码")
        sqld1 = "select * from user where password = %s"
        d1 = select(sqld1, password)
        if len(d1) != 0:
            print("下一步")
            moneydraw = int(input("请输入取款额："))
            sqld2 = "select money from user where account = %s"
            d2 = select(sqld2, account)
            if d2[0][0] > moneydraw:
                sqld3 = "update user set money = money - %s where account = %s"
                paramd3 = [moneydraw, account]
                update(sqld3, paramd3)
                sqld4 = "select money from user where account = %s"
                d4 = select(sqld4, account)
                dm = d4[0][0]
                print("取款成功,余额为", dm, "元")
                return 0
            else:
                print("余额不足")
                return 3
        else:
            print("密码错误")
            return 2
    else:
        print("账号不对")
        return 1


# 转账
def turnadd():
    account = input("请输入账号：")
    sqlt = "select * from user where account = %s"  # 查 转出账号
    t = select(sqlt, account)
    if len(t) != 0:  # 判断转出账号是否在数据库
        print("下一步")
        accountturn = input("请输入转入账号：")
        sqlt1 = "select * from user where account = %s"
        t1 = select(sqlt1, accountturn)
        if len(t1) != 0:
            print("新一步")
            password = input("请输入密码：")
            sqlt2 = "select * from user where password = %s"
            t2 = select(sqlt2, password)
            if t2 != 0:
                print("下一步")
                moneyturn = int(input("转出金额："))
                sqlt3 = "select money from user where account = %s"
                t3 = select(sqlt3, account)
                if t3[0][0] > moneyturn:
                    sqlt4 = "update user set money = money - %s where account = %s"
                    paramt4 = [moneyturn, account]
                    update(sqlt4, paramt4)
                    sqlt5 = "select money from user where account = %s"
                    t5 = select(sqlt5, account)
                    print("转账成功，余额为", t5[0][0], "元")  # 72295138  33094901
                    sqlt6 = "update user set money = money + %s where account = %s"  # 更新 转入账号的钱
                    paramt6 = [moneyturn, accountturn]
                    update(sqlt6, paramt6)
                    return 0
                else:
                    print("余额不足")
                    return 3
            else:
                print("密码错误")
                return 2
        else:
            print("账号错误")
            return 1
    else:
        print("账号错误")
        return 1


# 查询
def queryadd():
    account = input("请输入账号：")
    sqlq1 = "select * from user where account = %s"
    q1 = select(sqlq1, account)
    if len(q1) != 0:
        print("下一步")
        password = input("请输入密码：")
        sqlq2 = "select * from user where password = %s"
        q2 = select(sqlq2, password)
        if len(q2) != 0:
            selq3 = "select * from user where account = %s"
            q3 = select(selq3, account)
            account = q3[0][0]
            username = q3[0][1]
            password = q3[0][2]
            country = q3[0][3]
            province = q3[0][4]
            street = q3[0][5]
            door = q3[0][6]
            money = q3[0][7]
            date = q3[0][8]
            print("以下是您的信息")
            info = '''
            ---------个人信息----------
            账号：%s
            姓名：%s
            密码：%s
            居住地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户时间：%s
            开户银行：%s
            '''
            print(info % (account, username, password, country, province, street, door, money, date, bank_name))
    else:
        print("账号错误")


def welcome():
    print("---------------------------------")
    print("-  中国工商银行账户管理系统V3.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")


while True:
    welcome()
    choose = input("请选择业务：")
    if choose == "1":
        useradd()
    elif choose == "2":
        saveadd()
    elif choose == "3":
        drawadd()
    elif choose == "4":
        turnadd()
    elif choose == "5":
        queryadd()
    elif choose == "6":
        break
    else:
        print("请别乱搞！")
        break
