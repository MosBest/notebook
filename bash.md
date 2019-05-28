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
echo Gaspar &jieba& echo Balthasar || echo Melchior
```

## 条件表达式
条件表达式要么比较两个值，要么询问关于一个值的问题。条件表达式总是在双括号（[[]]）之间，它们使用逻辑标志或逻辑运算符。

如果我们想看一个整数是否大于另一个，我们可以使用-gt（大于号的标志）
```
[[ 4 -gt 3 ]]
```
上面的逻辑表达式是：4大于3吗？没有结果打印到控制台，所以让我们检查该表达式的退出状态。
```
echo $?

返回　0
```
看起来该程序的退出状态为0，退出状态与true相同。这个条件表达式是[[4 -gt 3]]等于true，当然我们知道它在逻辑上是一致的
```
[[ 3 -gt 4 ]]
```
同样，没有任何内容打印到控制台，所以我们将查看退出状态：
```
echo $?

返回 1
```
显然3不大于4，所以这个错误的逻辑表达式导致退出状态为1，这与false的退出状态相同！因为它们具有相同的退出状态[[3 -gt 4]]，而false基本上是等效的。
```
[[ 4 -gt 3 ]] && echo t || echo f
[[ 3 -gt 4 ]] && echo t || echo f
## t
## f

您可以使用-e逻辑标志测试文件是否存在
[[ -e math.sh ]] && echo t || echo f

其他代码示例
number=7
[[ $number -gt 3 ]] && echo t || echo f
[[ $number -gt 10 ]] && echo t || echo f
[[ -e $number ]] && echo t || echo f

## t
## f
## f
```

```
-gt 大于
-ge　大于等于
-eq　等于
-ne　不等于
-le　小于等于
-lt　小于
-e　某个文件是存在
-d　某个文件夹是否存在
-z　字符串的长度为０
-n　字符串的长度不为０
!　逻辑　非
=~　正则表达式匹配运算符
=　字符串等于
!=　字符串不等于
```

正则表达式匹配运算符　=~ :

正则表达式匹配运算符将字符串与正则表达式进行比较，如果字符串与正则表达式匹配，则表达式等效于true，否则等效于false。
```
[[ rhythms =~ [aeiou] ]] && echo t || echo f
my_name=sean
[[ $my_name =~ ^s.+n$ ]] && echo t || echo f

## f
## t
```

## if and else
if
```
#!/usr/bin/env bash
# File: simpleif.sh

echo "Start program"
($1表示　命令行中　传入的第一个参数　比如：　bash simpleif.sh 77)
if [[ $1 -eq 4 ]]
then
  echo "You entered $1"
fi

echo "End program"
```
然后在命令行中输入：
```
bash simpleif.sh 77
bash simpleif.sh 4
```

else
```
#!/usr/bin/env bash
# File: simpleifelse.sh

echo "Start program"

if [[ $1 -eq 4 ]]
then
  echo "Thanks for entering $1"
else
  echo "You entered: $1, not what I was looking for."
fi

echo "End program"
```
然后在命令行中输入：
```
bash simpleifelse.sh 4
bash simpleifelse.sh 3
```

elif
```
#!/usr/bin/env bash
# File: simpleelif.sh

if [[ $1 -eq 4 ]]
then
  echo "$1 is my favorite number"
elif [[ $1 -gt 3 ]]
then
  echo "$1 is a great number"
else
  echo "You entered: $1, not what I was looking for."
fi
```
然后在命令行中输入：
```
bash simpleifelse.sh 4
bash simpleifelse.sh 5
```

```
#!/usr/bin/env bash
# File: condexif.sh

if [[ $1 -gt 3 ]] && [[ $1 -lt 7 ]]
then
  echo "$1 is between 3 and 7"
elif [[ $1 =~ "Jeff" ]] || [[ $1 =~ "Roger" ]] || [[ $1 =~ "Brian" ]]
then
  echo "$1 works in the Data Science Lab"
else
  echo "You entered: $1, not what I was looking for."
fi
```
```
bash condexif.sh 2
bash condexif.sh 4
bash condexif.sh 6
bash condexif.sh Jeff
bash condexif.sh Brian
bash condexif.sh Sean

```

## 数组 array
Bash中的数组是有序的值列表。列表使用括号（）创建，并使用空格分隔列表中的每个元素
```
aa = (name1 aa bbb ccc ddd eee fff)
```
要检索数组，您需要使用参数扩展，它涉及美元符号和大括号（$ {}）。

数组中元素的位置从零开始编号。

要获取此数组的第一个元素，请使用$ {plagues [0]}。
```
echo ${a[0]}
```

要获得a的所有元素，请在方括号之间使用星号（*）:
```
echo ${a[*]}
```
更改数组内的值
```
a[1] = qqq
```
使用切片获取数组的一部分
```
echo ${a[*]:5:3}
从数组a中第六个元素开始得到3个数组元素（记住，第六个元素的索引为5）。
```
您可以使用井号（＃）找到数组的长度：
```
echo ${#a[*]}
```
您可以使用运算符（+=）将一个数组添加到另一个数组的末尾：
```
a = (ttt yyy uuu)
echo ${a[*]}
a += (www eee rrr)
echo ${a[*]}
```
## 创建连续序列
### {..}
```
echo {0..9}

## 0 1 2 3 4 5 6 7 8 9

echo {a..e}
echo {W..Z}

## a b c d e
## W X Y Z

echo a{0..4}
echo b{0..4}c

## a0 a1 a2 a3 a4
## b0c b1c b2c b3c b4c

echo {1..3}{A..C}

## 1A 1B 1C 2A 2B 2C 3A 3B 3C

要使用eval
start=4
end=9
echo {$start..$end}
eval echo {$start..$end}

## {4..9}
## 4 5 6 7 8 9
```
### {,}
```
echo {{1..3},{a..c}}
(注意　不要多加空格，要不然就错了)
## 1 2 3 a b c

echo {Who,What,Why,When,How}?
## Who? What? Why? When? How?
```

## 循环
for
```
#!/usr/bin/env bash
# File: forloop.sh

echo "Before Loop"

for i in {1..3}
do
    echo "i is equal to $i"
done

echo "After Loop"
```
```
#!/usr/bin/env bash
# File: manyloops.sh

echo "Explicit list:"

for picture in img001.jpg img002.jpg img451.jpg
do
    echo "picture is equal to $picture"
done

echo ""
echo "Array:"

stooges=(curly larry moe)

for stooge in ${stooges[*]}
do
    echo "Current stooge: $stooge"
done

echo ""
echo "Command substitution:"

for code in $(ls)
do
    echo "$code is a bash script"
done
bash manyloops.sh
## Explicit list:
## picture is equal to img001.jpg
## picture is equal to img002.jpg
## picture is equal to img451.jpg
##
## Array:
## Current stooge: curly
## Current stooge: larry
## Current stooge: moe
##
## Command substitution:
## bigmath.sh is a bash script
## condexif.sh is a bash script
## forloop.sh is a bash script
## letsread.sh is a bash script
## manyloops.sh is a bash script
## math.sh is a bash script
## nested.sh is a bash script
## simpleelif.sh is a bash script
## simpleif.sh is a bash script
## simpleifelse.sh is a bash script
## vars.sh is a bash script
```

while
```
#!/usr/bin/env bash
# File: whileloop.sh

count=3

while [[ $count -gt 0 ]]
do
  echo "count is equal to $count"
  let count=$count-1
done
```

```
!/usr/bin/env bash
# File: foreverloop.sh

count=3

while [[ $count -gt 0 ]]
do
  echo "count is equal to $count"
  let count=$count+1              # We only changed this line!
done

## ...
## count is equal to 29026
## count is equal to 29027
## count is equal to 29028
## count is equal to 29029
## count is equal to 29030
## ...

```

## 函数
```
function 函数名 {
  # code here
}
```
比如：
```
#!/usr/bin/env bash
# File: hello.sh

function hello {
  echo "Hello"
}

```

函数的输入参数　在　命令行　中提供

函数与单独的bash脚本共享许多行为，包括它们如何处理参数。通常的bash脚本参数（如$ 1，$ 2和$ @）都在函数内工作，这允许您指定函数参数。
```
#!/usr/bin/env bash
# File: ntmy.sh

function ntmy {
  echo "Nice to meet you $1"
}
```
那么命令行中可执行
```
bash ntmy.sh jeck
```
### source命令 (用于创造自己的命令)
到目前为止，在本章中我们一直在使用`bash　xxx.sh`的语法来执行脚本的内容。现在我们将开始使用source命令，它允许我们将　bash脚本中的函数　定义为　命令行的命令。
```
source ntmy.sh
ntmy Jeff
ntmy Philip
ntmy Jenny

## Nice to meet you Jeff
## Nice to meet you Philip
## Nice to meet you Jenny

```
就像那样，你已经创造了自己的命令！关闭当前shell后，您将无法访问ntmy命令，但在之后的内容中，我们将讨论如何设置自己的命令，以便始终可以访问它们。

### $@ 接收命令行所有的参数
```
#!/usr/bin/env bash
# File: addseq.sh

function addseq {
  sum=0

  for element in $@
  do
    let sum=sum+$element
  done

  echo $sum
}
```
结果是
```
source addseq.sh
addseq 12 90 3
addseq 0 1 1 2 3 5 8 13
addseq
addseq 4 6 6 6 4

## 105
## 33
## 0
## 26
```
### local　命令
我们在addseq.sh里面实现了一个函数。

然后，执行这个函数：
```
sourch addseq.sh
addseq 3 0 0
```
或者直接地
```
bash addseq.sh 3 0 0
```
注意：执行addseq.sh后，　addseq.sh函数里面的变量　将被视为　全局变量（没错，函数里面的变量被视为全局变量，而不是局部变量）。　也就是说，执行完addseq.sh，　可以在命令行中直接访问（设置可以修改）　addseq.sh 里面的　的变量。
```
比如可在命令行中访问　addseq.sh　中的变量$sum

echo $sum
```

这样做就会有很大的风险，不小心　让函数的值　覆盖了　命令行中关键变量的值　；　不小心　用命令行中关键变量的值　覆盖了　函数里面的值。

解决方案就是：　对函数中　变量　使用local 命令	
```
#!/usr/bin/env bash
# File: addseq2.sh

function addseq2 {
  local sum=0

  for element in $@
  do
    let sum=sum+$element
  done

  echo $sum
}

```
```
source addseq2.sh
sum=4444
addseq2 5 10 15 20
echo $sum

## 50
## 4444
```
### 函数返回值
```
my_sum=$(addseq2 5 10 15 20)
echo $my_sum

## 50
```

## 文件权限
