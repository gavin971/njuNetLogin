# Nanjing University Network Login

运行此脚本可以登陆南京大学校园网。主要可以被用来放到使用图形界面不方便的服务器上用以登陆校园网。

## 下载

在你想要放置此项目的目录下输入以下命令可以下载此项目：

```
git clone https://github.com/Pavinberg/njuNetLogin.git
```

也可单独下载 python 文件`njunet.py`。

## 使用

登陆校园网：

```
python njunet.py login
```

登出校园网：

```
python njunet.py logout
```

输入后会要求输入账户名和密码。如果不希望每次都输入，可以打开文件，将`username`变量设置为你的学号，也可设定`password`变量为你的密码。但可以访问此文件的人都可以看到你的密码，因此请谨慎设置。

在已登陆的情况下输入登陆命令，会显示当前登陆账号的信息，不会重复登陆。
