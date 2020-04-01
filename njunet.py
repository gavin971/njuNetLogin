'''
登陆或登出南京大学校园网
使用：
    登陆：python njunet.py login
    登出：python njunet.py logout
    帮助：python njunet.py --help
账号密码可在输入上述命令后提示输入。也可写在此文件的usernmae和password变量中，
避免每次都要输入。

Author: Pavinberg
Repository: https://github.com/Pavinberg/njuNetLogin

'''

import sys
import requests
import json
import time
import argparse

###############################################################################
# 设置账号密码
###############################################################################
# default username = "xxxx"
# 你可以将自己的学号写在这里，避免每次都要输入
username = "xxxx"

# defualt password = "****"
# 你也可以将密码写在这里。但其他能够访问此文件的人都能看到你的密码，请谨慎填写。
# password 为默认值("****") 或为空字符串时，需要从命令行运行时输入密码。
password = "****"
###############################################################################


PRICE = 360  # seconds per cent


def getInfo():
    ''' Get information of the account's balance and time used. '''
    def formatTime(secs):
        '''
        Input: total seconds
        Output: hour, minute, second
        Transfer secs to format of "hour, minute, second"
        '''
        hour = secs // 3600
        minute = (secs - hour * 3600) // 60
        second = secs - hour * 3600 - minute * 60
        return hour, minute, second

    url1 = "http://p.nju.edu.cn/portal_io/selfservice/userinfo/getlist"
    try:
        r = requests.get(url1)
        cont = r.content
        if r.status_code != 200:
            raise SystemExit
    except:
        sys.exit()
    js = json.loads(cont.decode("utf8"))
    balance = js["rows"][0]["account_balance"] / 10  # cents
    name = js["rows"][0]["fullname"]
    id = js["rows"][0]["username"]
    print(f"账户：{name} {id}")

    url2 = "http://p.nju.edu.cn/portal_io/selfservice/volume/getlist"
    cont = requests.get(url2).content
    js = json.loads(cont.decode("utf8"))
    timeCost = js["rows"][0]["total_time"]  # seconds
    hour, minute, _ = formatTime(timeCost)

    consumed = (timeCost - 30 * 3600) / PRICE
    if consumed > 2000:
        consumed = 2000
    if consumed < 0:
        consumed = 0
    print(f"余额：{balance/100:.2f} 元，已使用：{hour} 小时 {minute} 分钟, "
          f"本月已消费 {consumed/100:.2f} 元。")

    topTimeLeft = 130 * 3600 - timeCost # 130 hours max per month
    if topTimeLeft > 0:
        moneyToGo = topTimeLeft / PRICE # 1 cent for 6 mintes.
        if balance <= moneyToGo:
            h, m, _ = formatTime(balance * PRICE)
            if hour < 30:
                h += 30 - hour
            print(f"余额不足本月封顶，还可使用 {h:.0f} 小时 {m:.0f} 分钟。")
        else:
            h, m, _ = formatTime(topTimeLeft)
            print(f"余额充足，距离封顶还有 {h}小时 {m}分钟。")
    else:
        print("本月费用已封顶 20 元.")


def checkInternet():
    try:
        r = requests.get("http://www.baidu.com")
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False


def login():
    ''' Login to campus network if network is unavailable.'''
    if checkInternet():
        getInfo()
        return
    global username, password
    if username == "xxxx" or username == "":
        username = input("输入账户名：")
    else:
        print(f"账户名: {username}")
    if password == "****" or password == "":
        import getpass
        password = getpass.getpass()

    param = {
        "username": username,
        "password": password
    }
    url = "http://p.nju.edu.cn/portal_io/login"
    try:
        cont = requests.post(url, params=param).status_code
    except:
        print("登陆失败")

    if cont == 200:
        time.sleep(1)  # wait before login finishes, or would fail to get info.
        if checkInternet():
            print("登陆成功")
            getInfo()
        else:
            print("登陆失败")
    else:
        print("登陆失败")


def logout():
    url = "http://p.nju.edu.cn/portal_io/logout"
    for _ in range(3):
        requests.post(url)
        if not checkInternet():
            print("已退出登陆")
            return
        time.sleep(0.5)
    else:
        print("退出登陆失败，请重试，或用浏览器退出登陆。")


def main():
    if len(sys.argv) == 1:
        print(f"usage:\n    登陆: 'python njunet.py login'"
              f"\nor  登出: 'python njunet.py logout' to logout")
        sys.exit()
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["login", "logout"],
                        help=f"choose from login/logout to "
                        f"login or logout the NJU network")
    args = parser.parse_args()
    if args.action == "login":
        login()
    else:
        logout()


if __name__ == '__main__' :
    main()
