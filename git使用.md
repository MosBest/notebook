版本控制系统（Version Control System VCS）

# git 的使用
## 不使用 git clone的方法
假如将 /learngit 文件夹作为一个 项目，则
1. cd /learngit 
2. git init .
3. 假如不想把文件 test.py 纳入版本控制， 那么可以将其添加到一个特殊的文件.gitignore 中， 告诉git 将其忽略： $ echo "test.py" >> .gitignore $
4. 接下来可以添加当前文件夹(".")中的其他内容: 
