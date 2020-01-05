版本控制系统（Version Control System VCS）

# git 的使用
 

## 不使用 git clone的方法
假如将 /learngit 文件夹作为一个 项目，则
1. cd /learngit 
2. git init .
3. 假如不想把文件 test.py 纳入版本控制， 那么可以将其添加到一个特殊的文件.gitignore 中， 告诉git 将其忽略： $ echo "test.py" >> .gitignore $
4. 接下来可以添加当前文件夹(".")中的其他内容: 



##  git push 报错

```ERROR: You must verify your email address.
See https://github.com/settings/emails.
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists. 
```

测试git 是否连接成功github

使用

`ssh git@github.com`

出现 Hi MosBest! You've successfully authenticated, but GitHub does not provide shell access.表明连接成功,本地 git 连接成功github。

原因是： 自己的github的邮箱账号是很久以前就注册的，现在github 要求老用户要重新验证邮箱。



```
记录下遇到的坑问题,
错误:You must verify your email address
github的远程仓库关联成功了,可以拉取代码,不可以提交代码
开始的时候一直以为,是git 账号邮箱错误,查找了半天,config 配置信息都设置了,查看也没有错误,
后来才想起,现在用的github账号是重新注册了新的,原来新github账号没有邮箱验证,重新验证下邮箱就好了
解决:
在任意页面的右上角，单击您的个人资料照片，然后单击“设置”。
在左侧边栏中，单击“ 电子邮件”。
在您的电子邮件地址旁边，点击发送验证邮件。
GitHub会向您发送一封电子邮件，其中包含链接。单击该链接后，您将进入GitHub仪表板并看到确认横幅。

作者：盗梦如画
链接：https://www.jianshu.com/p/30ee5daf1327
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

