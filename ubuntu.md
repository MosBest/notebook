1. wc

    展现一个文件行的数目，　词个数，　字符的个数

    ```shell
    $ wc ubuntu.md 
         3  6 77 ubuntu.md
    ```
2. cat

    功能：
    1. 连接多个文件,并打印到命令行界面上面
		```shell
        cat todo.txt todo.txt
        ```
    2. 用于将文本文件打印到terminal
	```shell
    cat todo.txt
    ```
    
    缺点：
    仅仅用于查看小文件，要不然命令行界面会崩溃。
    
3. less
	
    功能：相比于cat,　less主要是用于查看大文件。
    ```shell
    less Documents/a-tale-of-two-cities.txt
    ```
    您可以使用向上和向下箭头键逐行向上和向下滚动文件，如果您想要更快地滚动，可以使用空格键转到下一页，使用b键转到上一页。为了减少退出并返回提示，请按q键。

4.  head
	```shell
    head aaa.txt (默认打印前10行)
    
    head -n 12 aaa.txt (指定打印前１２行)
    
    head -n 4 states.txt > four.txt
    ```
5.  tail

	功能：与head类似，只是tail是打印后几行的。

6. echo 

	功能：　打印输出
    
7.  \> 和　\>\>

	这两个符号　理解为　“重定向”
    ```shell
    echo "大家好"　> aaa.txt (将“大家好”　输入到aaa.txt . 如果aaa.txt 之前有内容，那么之前的内容就会背覆盖)
    echo "大家好"　>> aaa.txt (将“大家好”　zjia到aaa.txt . 如果aaa.txt 之前有内容，那么之前的内容就会背覆盖)
    ```
8. nano

	nano 是一个文字编辑器, 功能和vim, emacs类似，只是nano更加适用于初学者.
	
    符号(^)代表键盘上的Control键

9. mv

	功能：移动文件
	```shell
    mv journal-2017-01-24.txt 　Journal　（mv 文件/文件夹路径　目标地址文件夹路径）
    ```
    mv命令的另一个隐藏用途是你可以使用它来重命名文件和文件夹。第一个参数是要重命名的文件夹或文件的路径，第二个参数是具有文件或文件夹的新名称的路径。
    ```shell
    mv  todo.txt  todo-2017-01-24.txt
    ```

10.  cp
	```shell
    cp aaa.txt Desktop
    cp在复制文件时的使用方式与mv完全相同，你希望复制的文件或文件夹是第一个参数，目的地的文件夹路径是第二个参数
    
    cp -r Documents Desktop
    请注意，复制文件和文件夹之间存在一个区别，复制文件夹时需要指定-r选项，这是递归的缩写。这可确保您要复制的目录的基础目录结构保持不变。
    ```
	
11.  rm

    您应该尽量避免使用永久删除文件或文件夹的rm 

    一句非常谨慎的话：一般来说，我不建议在命令行上删除文件或文件夹，因为正如我们之前所讨论的那样，命令行上没有撤消按钮。如果删除对计算机功能至关重要的文件，可能会造成无法挽回的损失。我很高兴建议将文件或文件夹移动(用 mv)到指定的垃圾文件夹，然后按照通常删除命令行之外的文件和文件夹的方式删除它们（垃圾桶的路径是〜/ .Trashon Mac和〜/ .local / share / Trash在Ubuntu上）。
    
    ```shell
    建议：用mv 将文件或文件夹移动(用 mv)到指定的垃圾文件夹。
    rm aaa.txt
    rm -r document (-r 指的是　迭代的意思)
    ```
12.  man

	功能：使用man命令可以查看　其他每个命令的帮助文档
    ```shell
    man ls
    (然后键入“/abs”即可查看ls帮助文档中所有出现“abs”的位置。按n键以搜索下一个出现的单词，如果要转到上一个出现类型Shift + n。当您完成查看手册页时，请键入q以返回提示。)
    ```
13.  apropos

	功能：如果你忘记了你正在寻找的命令的名字呢？您可以使用apropos搜索所有可用命令及其描述。
    ```shell
    比如你忘了什么命令可以调开一个编辑器，那么
    apropos editor
    结果是：
    
        $ ed(1), red(1)            - text editor
        $ nano(1)                  - Nano's ANOther editor, an enhanced free Pico clone
        $ sed(1)                   - stream editor
        $ vim(1)                   - Vi IMproved, a programmers text editor
    ```
14.  “　*　”　通配符

	功能：*（“star”）通配符表示任何字符的零个或多个，它可用于匹配命令行中的文件和文件夹的名称。
	```shell
    ls 2016*
    ls *.jpg
    ls *01.*
    mv 2016-* 2017/
    ```
15.  grep 和　egrep
	
    功能：　对文本文件内容进行搜索
    
    格式为：
    ```shell
    grep 　正则表达式　要搜索的文本文件
    egrep 　正则表达式　要搜索的文本文件
    
    grep 　-v 正则表达式　要搜索的文本文件
    -v标志（代表反转匹配）使grep返回所有与正则表达式不匹配的行。
    
    egrep -n "t$" states.txt
    您可以使用 -n 标志显示匹配发生的行号
        ## 7:Connecticut
        ## 45:Vermont

	您还可以通过提供多个文件参数来一次grep多个文件：
    egrep "New" states.txt canada.txt
        ## states.txt:New Hampshire
        ## states.txt:New Jersey
        ## states.txt:New Mexico
    ```
    ```shell
    比如：
    grep "new" states.txt
    egrep "(i.{2}){3}" states.txt
    ```
16. 　find
	
    功能：查找文件的位置或一组文件的位置
    
    其中第一个参数是您要开始搜索的目录，并且还将搜索该目录中包含的所有目录。然后是第一个参数后跟一个描述您要用于搜索的方法的标志。在这种情况下，我们只会按名称搜索文件，因此我们将使用-name标志。然后-name标志本身接受一个参数，即您正在寻找的文件的名称。
    ```shell
    find . -name "states.txt"
    find . -name "*.jpg"
    ```

17. 　history
	
    功能：　浏览　历史　命令　记录
    ```shell
    history
    ```

18. 　〜/ .bash_history
	
    功能：　每当我们关闭终端时，我们最近的命令都会写入〜/ .bash_history文件。
    
    ```shell
    head -n 5 ~/.bash_history
    grep "canada" ~/.bash_history
    ```
19. 〜/.bash_profile

	功能：　每打开一个　terminal, 就会自动执行的文件
   
   （不过我还没弄懂）
    
20. alias
	
    功能：取别名，自己　自定义命令。
    ```shell
    alias edbp='nano ~/.bash_profile'
    （则　之后在命令行上面输入　edbp 就会执行'nano ~/.bash_profile'语句）
    ```
21. diff

	功能：　查看两个文件在哪些行不同。只有不同的行打印到控制台。
    ```shell
    diff four.txt six.txt
    ```
22. sdiff

	diff只有不同的行打印到控制台。
    但是, 我们还可以使用sdiff在并排比较中比较不同的行。
    ```shell
    sdiff four.txt six.txt
    ```
23. md5 和　shasum
	
    功能：　md5用于生成 md5哈希。　shasum用于生成 SHA-1 哈希。
    
    都是根据　文件内容生成哈希。即　同一个内容的文件，不同文件名，得到的hash值是一样的。
    ```shell
    md5 states.txt
        ## MD5 (states.txt) = 8d7dd71ff51614e69339b03bd1cb86ac
	md5 states_copy.txt
        ## MD5 (states_copy.txt) = 8d7dd71ff51614e69339b03bd1cb86ac
        
	shasum states.txt
        ## 588e9de7ffa97268b2448927df41760abd3369a9  states.txt
	shasum states_copy.txt
        ## 588e9de7ffa97268b2448927df41760abd3369a9  states_copy.txt
    ```
24. 管道 ( | )
	
    功能：　管道允许我们获取命令的输出，该命令通常会打印到控制台，并将其用作另一个命令的输入。这就像在一个程序的末尾之间安装实际管道并将其连接到另一个程序的顶部！
    
    ```shell
    管道的一般语法是
    [生成输出的程序] | [程序使用管道左边的输出作为右边的输入]
    
    cat canada.txt | head -n 5 
    (来自cat canada.txt的输出将进入我们的管道，然后作为head命令的输入，我们用它来查看文件的前几行)
    这与我们从head -n 5 canada.txt得到的结果相同
    
    管道也可以在一个命令中多次使用
    ls -al | grep "Feb" | less
    ```
25. 　make

	功能：
	    １．用于安装软件
        ２．自动产生文档
    
    makefile　是一个包含了一系列rules的文本文件。
    rules的书写格式是：
       
    ```   
    target: dependencies...
        commands...
    (注意：commands相对于target是有一个tab的缩进的，有的系统是２个空格，有的是８个空格。	所以，不能够用空格，直接一个缩进就可以了)
    ```
    以下为所有例子
    ```
    zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
    zhaodao@wayne-MS-7B24:~/cvp/aa$ nano makefile
            (写入的内容是
            draft_journal_entry.txt:
                touch draft_journal_entry.txt
            )
            
    zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
    makefile
    zhaodao@wayne-MS-7B24:~/cvp/aa$ make draft_journal_entry.txt
    touch draft_journal_entry.txt
    zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
    draft_journal_entry.txt  makefile
    
    #　因为makefile中的内容draft_journal_entry.txt:后面没有跟依赖关系，所以makefile的draft_journal_entry.txt不会随着外界改变
    zhaodao@wayne-MS-7B24:~/cvp/aa$ make draft_journal_entry.txt
	make: “draft_journal_entry.txt”已是最新。
```
```
    # 依赖关系
    zhaodao@wayne-MS-7B24:~/cvp/aa$ echo "1. 2017-06-15-In-Boston" > toc.txt
	zhaodao@wayne-MS-7B24:~/cvp/aa$ nano makefile
        (写入的内容是
            draft_journal_entry.txt:
            	touch draft_journal_entry.txt
    		
            readme.txt: toc.txt
	      	  echo "This journal contains the following number of entries:" > readme.txt
		        wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
        )
	zhaodao@wayne-MS-7B24:~/cvp/aa$ make readme.txt 
	echo "This journal contains the following number of entries:" > readme.txt
	wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
	zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
	draft_journal_entry.txt  makefile  readme.txt  toc.txt
	zhaodao@wayne-MS-7B24:~/cvp/aa$ cat readme.txt 
	This journal contains the following number of entries:
	1
	# 再一次make readme.txt, 由于依赖的文件toc.txt没有改变，所以readme.txt已是最新。
	zhaodao@wayne-MS-7B24:~/cvp/aa$ make readme.txt 
	make: “readme.txt”已是最新。
	＃那么现在修改readme.txt的依赖文件toc.txt, 发现readme.txt可以重新make,　且内容也更新了。
	zhaodao@wayne-MS-7B24:~/cvp/aa$ echo "2. 2017-06-16-IQSS-Talk" >> toc.txt
	zhaodao@wayne-MS-7B24:~/cvp/aa$ make readme.txt
	echo "This journal contains the following number of entries:" > readme.txt
	wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
	zhaodao@wayne-MS-7B24:~/cvp/aa$ cat readme.txt 
	This journal contains the following number of entries:
	2
```
```
# 在makefile最前面写入all, 则以后只需输入make，就可以make makefile里面所有的内容。
# 在makefile最后面使用clean, 则可以消除文件
zhaodao@wayne-MS-7B24:~/cvp/aa$ nano makefile
	（写入的内容是:
    	all: draft_journal_entry.txt readme.txt
    
		draft_journal_entry.txt:
  			touch draft_journal_entry.txt
            
		readme.txt: toc.txt
  			echo "This journal contains the following number of entries:" > readme.txt
 			 wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
             
		clean:
  			rm draft_journal_entry.txt
  			rm readme.txt
    ）
zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
draft_journal_entry.txt  makefile  readme.txt  toc.txt
zhaodao@wayne-MS-7B24:~/cvp/aa$ make clean
rm draft_journal_entry.txt
rm readme.txt
zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
makefile  toc.txt
zhaodao@wayne-MS-7B24:~/cvp/aa$ make
touch draft_journal_entry.txt
echo "This journal contains the following number of entries:" > readme.txt
wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
zhaodao@wayne-MS-7B24:~/cvp/aa$ ls
draft_journal_entry.txt  makefile  readme.txt  toc.txt

    ```


	

    



