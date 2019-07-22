
#  作用
让项目运行在一个独立的局部的 Python 环境中，使采用不同环境的项目互不干扰。

# 安装 virtualenv
1. virtualenv，就是一个三方包
2. 安装命令，pip3 install virtualenv
3. 使用文档 https://virtualenv.pypa.io/en/stable/userguide/

安装过程中，如果出现如下 error 信息是，可以尝试切换源重新下载
 
 豆瓣源: pip install virtualenv --trusted-host pypi.douban.com  
 
 官方源: pip install virtualenv -i https://pypi.python.org/simple/
 
 清华源: pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple/
 
 等等其他源
 
# 使用虚拟环境
1 创建一个局部的隔离的virtualenv虚拟环境
1.1 cd 到存放虚拟环境的的地址
```shell
$ mkdir 111
$ cd ./111
```
1.2 执行命令virtualenv ENV，创建名为ENV 的虚拟环境
```python
~/111$ virtualenv eennvv
Using base prefix '/usr'
New python executable in 111/eennvv/bin/python3
Also creating executable in 111/eennvv/bin/python
Installing setuptools, pip, wheel...
done.

```
好了，现在你在 111文件夹中，就有了一个名为eennvv的虚拟环境。

# 注意：
* 虚拟环境文件包括：Python解析器，包管理工具(setuptools, pip, wheel)，三方包等
* 即使创建的 bin 脚本命令集含有 python 和 python3两个脚本，实际它们的版本都是3.6，这个防止使用者理解不足导致已为使用 python 命令时是使用Python2.x 版本。

# 指定 Python 版本创建虚拟环境
* 可选参数：-p
* 指定 Python2.x 版本创建虚拟环境
```shell
$ virtualenv -p /usr/local/bin/python2.7 testvirtual2
```

# 是否继承系统三方库 --system-site-packages
添加参数--system-site-packages，项目检索库的时候，也会到系统的三方库中找
不添加时，默认只到虚拟环境中查找库
```
$ virtualenv --system-site-packages ENV
```

# 激活/退出 虚拟环境
1. cd 到虚拟环境文件夹目录
```shell
cd /Users/xxx/Desktop/testvirtuals/virtual1
```
2. 执行命令 source bin/activate，shell 会打印出已激活的虚拟环境名称
```
$ source bin/activate
```
3. 验证当前确实在已激活的虚拟环境中，执行命令 pip --version 和 pip list
如果是虚拟环境，则每次打印后都会提示(virtual1)，所在环境是虚拟环境

4. 退出虚拟环境，在激活的虚拟环境中，执行命令 deactivate
```
$ deactivate
```
5. 验证已经退出，执行命令 pip --version 和 pip list
结果都是来自系统环境, 即末尾没有提示(virtual1)

# 在激活状态下，操作

1. 操作三方块
```
pip install requests
```
2. 执行 py 文件
```
python xx.py
```
以上操作均作用在虚拟环境中。

# 删除虚拟环境
直接删除虚拟环境所在目录即可.

#项目交接 requirements.txt文件
要求： 确保共享的项目能够在其他电脑上正常运行
解决：

## 方案一：

	连同虚拟环境和项目一起拷贝给他人
	
## 方案二：

1. 在虚拟环境中，冻结依赖需求文本
2. 把项目和依赖需求文本给他人
3. 他人在本地创建一个新的虚拟环境，并根据依赖需求文本安装相关库
**冻结项目需求文本 pip freeze > requirements.txt**

**根据需求文本，安装项目依赖库 pip install -r requirements.txt （在激活的虚拟环境中）**