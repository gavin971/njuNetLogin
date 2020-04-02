# 南京大学校园网登陆脚本

运行此脚本可以登陆南京大学校园网。主要可以被用来放到使用图形界面不方便的服务器上用以登陆校园网。

## 环境配置

```
python>=3.6
```

事实上，这只是由于代码中使用了 f-string。如果想运行在更低版本的 python 中，可以自己改动一下源码 print 函数中有 f-string 的部分，换成如 format 函数即可。

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

输入后会要求输入账户名和密码。如果不希望每次都输入，可以打开源文件 `njunet.py`，将 `username` 变量设置为你的学号。也可设定 `password` 变量为你的密码。但可以访问此文件的人都可以看到你的密码，因此请谨慎设置。

在已登陆的情况下输入登陆命令，会显示当前登陆账号的信息，不会重复登陆。

## 设为命令

如果希望能在任何目录下都能通过一句命令登陆/登出校园网，例如：

```
njunet.py login
```

可以打开源文件 `njunet.py`，在开头第一行写一行 shebang，类似于：

```
#!/path/to/your/python
```

可以通过命令 `which python` 查看当前 python 的位置，常见位置对应的 shebang 有 `#!/usr/local/bin/python`、`#!/anaconda3/bin/python` 等，注意写成绝对路径。

随后将此脚本设定为可执行：

```
chmod u+x njunet.py
```

最后把此脚本放入合适的目录下，例如 `~/bin/`，并把该目录添加到环境变量中，如输入命令：

```
export PATH=$HOME/bin:$PATH >> ~/.bashrc
``` 

重启终端或 `source ~/.bashrc` 即可使用。
