# Nanjing University Network Login

运行此脚本可以登陆南京大学校园网。

## 使用方法

登陆：

```
python njunet.py login
```

登出：

```
python njunet.py logout
```

输入后会要求输入账户名和密码。如果不希望每次都输入，可以打开文件，将`username`变量设置为你的学号，也可设定`password`变量为你的密码。但可以访问此文件的人都可以看到你的密码，因此请谨慎使用。
