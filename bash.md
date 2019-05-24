# bash编程语言
和python, c一样,　bash文件是以 .sh 为结尾的。方式是 在　ubuntu命令行　中输入 bash xxx.sh

bash编程其实就是把　ubuntu命令行 中的　一个个的命令　都整合到　一个以.sh为结尾的文件中。

"#" 的功能是注释

## math


在进行乘法时，您需要转义星形字符(即应该是　5 \* 3 而不能是　5*3)，否则Bash认为您正在尝试创建正则表达式！

在进行除法时，除了5/2 = 2.5之外，除法运算符（/）无法正常工作。(/)执行整数除法，这意味着将一个数字除以另一个数字的结果总是向下舍入到最接近的整数。

在math.sh 中输入
```bash
#!/usr/bin/env bash
# File: math.sh

expr 5 + 2
expr 5 - 2
expr 5 \* 2
expr 5 / 2
```
然后在命令行内　输入　
```
bash math.sh
```
结果是：
```
7
3
10
2

```
模数运算符（％）。模数运算符返回整数除法后的余数。
在math.sh 中输入
```bash
#!/usr/bin/env bash
# File: math.sh

expr 1 / 3
expr 10 / 3
expr 40 / 21
expr 40 / 20

expr 1 % 3
expr 10 % 3
expr 40 % 21
expr 40 % 20
```
然后在命令行内　输入　
```
bash math.sh
```
结果是：
```
0
3
1
2

1
1
19
0
```

### bc命令
bc 命令是一个提供任意精度算术的交互式进程。

-l 执行指定语句前，先加载math函数库

在math.sh 中输入
```bash
#!/usr/bin/env bash
# File: bigmath.sh

echo "22 / 7" | bc -l
echo "4.2 * 9.15" | bc -l
echo "(6.5 / 0.5) + (6 * 2.2)" | bc -l
```
然后在命令行内　输入　
```
bash math.sh
```
结果是：
```
3.14285714285714285714
38.430
26.2
```


## 变量
在Bash中，您可以将数据存储在变量中。避免与　由操作系统设置的环境变量　相同。您还可以创建自己的变量。在命名变量时，请确保遵循这些规则：

每个字符都应该是小写的。

变量名称应以字母开头。

名称应仅包含字母数字字符和下划线（_）。

名称中的单词应以下划线分隔。

如果遵循这些规则，则可以避免意外覆盖存储在环境变量中的数据。

您可以使用等号（=）将数据分配给变量。存储在变量中的数据可以是字符串或数字。

在ubuntu命令行中输入：
chapter_number=5　但是不能是　chapter_number　=　5　，　也就是等号"="两边不能够有空格。

在ubuntu命令行中 使用　变量，　变量名前面加上“$”

```
chapter_number=5
echo $chapter_number
let chapter_number=$chapter_number+1
echo $chapter_number

the_empire_state="New York"
echo $the_empire_state

```
### let 命令

您可以使用let命令　修改变量的值
```
let chapter_number=$chapter_number+1
echo $chapter_number
```

如果你想获得　ubuntu某个命令得到的值作为某个变量的输入，那么可以使用“($(命令))”组合。
```
math_lines=$(cat math.sh | wc -l)
echo $math_lines

```

带有美元符号的变量名也可以在 其他字符串里面　使用，以便将变量的值插入到字符串中：
```
echo "I went to school in $the_empire_state."
```

## bash脚本文件 接收　命令行　参数
在　vars.sh 中　输入
```
#!/usr/bin/env bash
# File: vars.sh

echo "Script arguments: $@"
echo "First arg: $1. Second arg: $2."
echo "Number of arguments: $#"
```

则在命令行中　输入以下值，以及器输出的参数
```
bash vars.sh

## Script arguments:
## First arg: . Second arg: .
## Number of arguments: 0

bash vars.sh red

## Script arguments: red
## First arg: red. Second arg: .
## Number of arguments: 1

bash vars.sh red blue

## Script arguments: red blue
## First arg: red. Second arg: blue.
## Number of arguments: 2

bash vars.sh red blue green

## Script arguments: red blue green
## First arg: red. Second arg: blue.
## Number of arguments: 3
```

## 用户输入
### 使用命令　read
使用方法是: read response　

这样，接收　键盘中得到的输入，并传给response

letsread.sh文件中输入
```
#!/usr/bin/env bash
# File: letsread.sh

echo "Type in a string and then press Enter:"
read response
echo "You entered: $response"
```
命令行中输入：
```
bash letsread.sh
```
输出是：
```
Type in a string and then press Enter:
Hello!
You entered: Hello!
```
## bool
true 和　false
```
>>> ture
>>> false
```
## ubuntu每一个命令执行后，都会有一个返回值
ubuntu每一个命令执行后，都会有一个返回值。

程序的退出状态是整数，最后一个程序运行的退出状态存储在问号变量（$？）
```
>>> this_command_does_not_exist
	Error in running command bash

>>> echo $?
	 127 (如果是因为　命令不存在，那么退出状态为127)

>>> echo "I will succeed."
 	I will succeed.
>>> echo $? 
	0 (成功程序的退出状态为0)

>>> true
>>> echo $?
	0 (true的退出状态为0)
>>> false
>>> echo $?
	1 (false的退出状态为1)
```

## 逻辑运算符 AND运算符（&&）和OR运算符（||）
在AND运算符的情况下，只有在&&左侧的程序**退出状态为0**时，才会执行&&右侧的程序。

在OR运算符的情况下, 仅当左侧的命令失败并因此具有除0以外的退出状态时, 命令在||的右侧才执行。

您可以在命令中组合AND和OR运算符，这些命令从左到右进行求值。

```
true && echo "Program 1 was executed."
false && echo "Program 2 was executed."

false && true && echo Hello
echo 1 && false && echo 3
echo Athos && echo Porthos && echo Aramis

true || echo "Program 1 was executed."
false || echo "Program 2 was executed."

false || echo 1 || echo 2
echo 3 || false || echo 4
echo Athos || echo Porthos || echo Aramis

echo Athos || echo Porthos && echo Aramis
echo Gaspar && echo Balthasar || echo Melchior
```