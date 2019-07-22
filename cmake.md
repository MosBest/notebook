[TOC]

#  C++程序的执行过程: 预编译、编译、汇编、链接

![source_2_exe](/home/zhaodao/桌面/github/notebook/picture/source_2_exe.png)

源文件变成 可执行文件 需要 进行两个过程： **编译过程** 和 **链接过程**。  

**编译过程**: 

​	编译过程又可以分成两个阶段：编译和汇编。

**编译**:  将高级语言转化为汇编语言。

编译又包含两个主要阶段： 

第一个阶段是预处理阶段， 预编译程序所完成的基本上是对源程序的“替代”工作。

​	 1. 包括 宏定义指令，如 #define a  b ； 

​	2.  条件编译指令，如#ifdef，#ifndef，#else，#elif，#endif等；

​	3.  头文件包含指令，如#include "FileName"或者#include 等。

	4.  特殊符号，预编译程序可以识别一些特殊的符号。

第二个阶段编译、优化阶段。



**汇编**:  汇编语言代码翻译成目标机器指令(01010001001)。

每一个源程序，都将最终经过这一处理而得到相应的**目标文件**。

**目标文件** 中所存放的也就是与源程序等效的目标的**机器语言代码**。



目标文件其实有三种，（1）可重定位文件， （2）共享的目标文件， （3）可执行文件。

但是 经过汇编语言 生成的实际上是第一种类型的目标文件(即 可重定位文件， 其中包含有适合于其它目标文件链接来创建一个可执行的或者共享的目标文件的代码和数据)。



对于后两种目标文件还需要其他的一些处理方能得到，这个就是链接程序的工作了。



目标文件由段组成。通常一个目标文件中至少有两个段：代码段 和 数据段。



**我们在Linux使用的g++编译器便是把以上的几个过程进行捆绑，使用户只使用一次命令就把编译工作完成，**

g++编译器的命令：

```shell
$ g++ --help

-o <file>                Place the output into <file>.
						  指定下面三种情况下 的 输出文件的名称
							
-E                       Preprocess only; do not compile, assemble or link.
						  仅仅做预处理，不编译，不汇编，不链接
						  
-S                       Compile only; do not assemble or link.
						   仅仅做编译， 不汇编， 不链接
						   
-c                       Compile and assemble, but do not link.
                           进行编译和汇编， 但不链接

```

**一般的，如果g++没有设定-E, -S, -c ，那么g++ 默认直接将编译链接一次性完成。**

如果g++ 没有设定-o， 那么输出的默认是.out文件。





**链接过程**

就是将 汇编程序生成的多个 目标文件 链接起来，生成可执行文件。

链接程序的主要工作就是将有关的目标文件彼此相连接，也即将在一个文件中引用的符号同该符号在另外一个文件中的定义连接起来，使得所有的这些目标文件成为一个能够诶操作系统装入执行的统一整体。



如果仅仅只有一个.cpp文件，那么不进行链接也是可以运行的。但是如果有多个.cpp文件，那么只有进行链接才能够得到可自行文件。



g++ 链接器 没有命令，它会默认调用collect2（而不是ld）来完成链接工作， 且链接时是自动发生，不需要人为设定什么内容。

如果使用 ld 命令，要自己设定很多其他方面的 链接文件，很容易报错，而collect2是对ld的封装。

见 [使用ld命令链接目标文件生成可执行文件](https://dablelv.blog.csdn.net/article/details/88094902)





#  GNU工具集 , MinGW 和 CMake 联系

以下内容全部来自：  http://c.biancheng.net/view/3868.html



##  GNU工具集



Unix 系统都是商业软件，里面的应用软件也是商业软件， 全是封闭的环境。 系统程序员 Richard M. Stallman (RMS) 在此环境下创立了与众不同的 [GNU 项目](https://www.gnu.org/) (GNU's Not Unix) ， 以及推进自由软件发展的 [Free Software Foundation (FSF) 自由软件基金会](https://www.fsf.org/)。



GNU 项目是为了创建自由的类 Unix 系统，也因此开发出来很多开源的系统工具，其中非常著名的就是 [GCC](http://c.biancheng.net/gcc/) （GNU Compiler Collection，GNU编译器套件）。



在 GNU 工具集里面，开发时常见到的几个罗列如下（这些工具通常位于 Linux 或 Unix 系统里的 /usr/bin/ 目录）：

| 工具 |                             说明                             |
| :--: | :----------------------------------------------------------: |
| gcc  |                      GNU C 语言编译器。                      |
| g++  |    GNU [C++](http://c.biancheng.net/cplus/) 语言编译器。     |
|  ld  | GNU 链接器，将目标文件和库文件链接起来，创建可执行程序和动态链接库。 |
|  ar  |          生成静态库 .a ，可以编辑和管理静态链接库。          |
| make | 生成器，可以根据 makefile 文件自动编译链接生成可执行程序或库文件。 |
| gdb  |                 调试器，用于调试可执行程序。                 |
| ldd  |  查看可执行文件依赖的共享库（扩展名 .so，也叫动态链接库）。  |



##  MinGW

原本 GNU 工具只在 Linux/Unix 系统里才有，随着 Windows 系统的广泛使用， 为了在 Windows 系统里可以使用 GNU 工具，诞生了 MinGW（Minimalist GNU for Windows） 项目，利用 MinGW 就可以生成 Windows 里面的 **exe 程序**和 **dll 链接库**。

需要注意的是，MinGW 与 Linux/Unix 系统里 GNU 工具集的有些区别：

- MinGW 里面工具带有扩展名 .exe， Linux/Unix 系统里工具通常都是没有扩展名的。
- MinGW 里面的生成器文件名为 mingw32-make.exe，Linux/Unix 系统里就叫 make。
- MinGW 在链接时是链接到 *.a 库引用文件，生成的可执行程序运行时依赖 *.dll，而 Linux/Unix 系统里链接时和运行时都是使用 *.so 。
- 另外 MinGW 里也没有 ldd 工具，因为 Windows 不使用 .so 共享库文件。如果要查看 Windows 里可执行文件的依赖库，需要使用微软自家的 Dependency Walker 工具。Windows 里面**动态库扩展名为 .dll**，MinGW 可以通过 dlltool 来生成**用于创建和使用动态链接库需要的文件，如 .def 和 .lib**。



MinGW 原本是用于生成 32 位程序的，随着 64 位系统流行起来， 从 MinGW 分离出来了 MinGW-w64 项目，该项目同时支持生成 64 位和 32 位程序。

##  MSYS（Minimal SYStem)



另外提一下，由于 MinGW 本身主要就是编译链接等工具和头文件、库文件，并不包含系统管理、文件操作之类的 [Shell](http://c.biancheng.net/shell/)[Linux 命令](http://c.biancheng.net/linux/)
MSYS 对于熟悉 Unix/Linux 系统环境或者要尝试学习 Unix/Linux 系统的人都是一种便利。MSYS 和 MinGW 的安装升级都是通过其官方的 mingw-get 工具实现，二者是统一下载安装管理的。



对于 MinGW-w64 项目，它对应的小型系统环境叫 MSYS2（Minimal SYStem 2），MSYS2 是 MSYS 的衍生版，不仅支持 64 位系统和 32 位系统，还有自己的独特的软件包管理工具，它从 Arch Linux 系统里移植了 pacman 软件管理工具，所以装了 MSYS2 之后，可以直接通过 pacman 来下载安装软件，而且可以自动解决依赖关系、方便系统升级等。装了 MSYS2 之后，不需要自己去下载 MinGW-w64，可以直接用 pacman 命令安装编译链接工具和 git 工具等。



## cmake



CMake（Cross platform Make）是一个开源的跨平台自动化构建工具， 可以跨平台地生成各式各样的 makefile 或者 project 文件， 支持利用各种编译工具生成可执行程序或链接库。
CMake 自己不编译程序， 它相当于用自己的构建脚本 CMakeLists.txt，叫各种编译工具集去生成可执行程序或链接库。

一般用于编译程序的 makefile 文件比较复杂，自己去编写比较麻烦， 而利用 CMake ，就可以编写相对简单的 CMakeLists.txt ，由 CMake 根据 CMakeLists.txt 自动生成 makefile，然后就可以用 make 生成可执行程序或链接库。

#  c++ 项目编写

##  g++

编写完源码后，需要将源码进行编译，汇编，链接 最终得到 可自行文件。

这个过程，（对于c++源码）可以用g++来完成。前面已经讲过，这里不在重复。

##  Makefile 和 make

即生成脚本，虽然可以直接调用编译器如 g++ 编译程序，但是如果项目里的代码文件变多了，哪些代码文件更新了需要重新编译，哪些代码没有改不需要重新编译等等，靠程序员自己记忆去处理是比较麻烦的事，还有哪些代码 需要预处理或是链接哪些库文件， 这些都是繁杂的过程。

**为了规范程序的编译生成过程，产生了规范化的生成脚本，就是 Makefile，生成器 make 可以依据规范的 Makefile 自动生成目标程序或库文件。而不需要自己去写 g++。**



简单的说，就是定义好 Makefile ，让程序员只需要去关注如何编写代码，而生成程序过程中的脏活累活都交给 make 程序。



##   CMakeLists.txt  和 cmake

一般用于编译程序的 makefile 文件比较复杂，自己去编写比较麻烦， 而利用 CMake ，就可以编写相对简单的 CMakeLists.txt ，由 CMake 根据 CMakeLists.txt 自动生成 makefile，然后就可以用 make处理makefile， 生成可执行程序或链接库。



##  项目排版（简单版）

加入整个项目在文件夹 a 中，则在文件夹a中在生成4个基本的文件夹，分别为 ./a/src/,  ./a/include/,  ./a/bin/,  ./a/build/ 。（当然，根据需求，你也可以多生成其他功能的文件夹）



./a/src/ : 用于存放 .cpp源码

./a/include/: 用于存放各种.h头文件

./a/bin/:  我们会在CMakeLists.txt中指定项目的产生的可执行文件存放与此。

./a/build/:  用于存放 使用 cmake和make产生的一些之间文件。



整个(简单的)项目的流程：

1.  编写源码并存放在./a/src/  和  ./a/include/。
2.  在文件夹./a中 编写 CMakeLists.txt. 也就是说 CMakeLists.txt的路径是 ./a/CMakeLists.txt
3. 在 ./a/build/ 路径下执行 **cmake ..**
4.  在 ./a/build/ 路径下执行 **make**
5. 切换到./a/bin/中你就可以看到 生成的可执行文件。



```shell
dao:~/distance_measure$ tree -x
.
├── README.md
├── CMakeLists.txt
|
├── bin
│   ├── img_RR_matches_0.jpg
│   ├── img_RR_matches_1.jpg
│   ├── main
├── build
├── include
│   └── test.h
├── picture
│   └── 9.png
└── src
    ├── main.cpp
    └── test.cpp

```



对应的CMakeLists.txt是：

```cmake
cmake_minimum_required (VERSION 2.8)

project (demo)
set(CMAKE_PREFIX_PATH "/home/zhaodao/Qt5.9.0/5.9/gcc_64/lib/cmake")

#打开全局moc
set(CMAKE_AUTOMOC ON)
#打开全局uic
#打开全局rcc，本示例中没有使用qrc，此句可以去掉
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


set(HEADERS 
    ${PROJECT_SOURCE_DIR}/include/test.h
)

set(SOURCES 
    ${PROJECT_SOURCE_DIR}/src/main.cpp
    ${PROJECT_SOURCE_DIR}/src/test.cpp
)

set(RESOURCES 
    ${PROJECT_SOURCE_DIR}/src/qml.qrc
)

set(QMLS
    ${PROJECT_SOURCE_DIR}/src/main.qml
    ${PROJECT_SOURCE_DIR}/src/ColorSquare.qml
)

aux_source_directory (${PROJECT_SOURCE_DIR}/src SRC_LIST)
set (INCLUDE_LISTSS ${PROJECT_SOURCE_DIR}/include/test.h)


find_package( OpenCV REQUIRED )
find_package(Qt5 REQUIRED Widgets Core Gui Quick Qml)


include_directories (${PROJECT_SOURCE_DIR}/include)

add_executable (main ${SRC_LIST} ${INCLUDE_LISTSS} ${HEADERS} ${SOURCES} ${RESOURCES} ${QMLS})

target_link_libraries(main ${OpenCV_LIBS} )
target_link_libraries(main Qt5::Widgets Qt5::Core Qt5::Gui Qt5::Quick Qt5::Qml)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
```





# c++ 编程的关键术语和名词

http://c.biancheng.net/view/3871.html

##  Debug 和 Release

   Debug 即调试，Release 即发行。代码编写之后，生成的目标程序或库文件通常不会绝对正确，或多或少有些毛病（bug）， 因此需要进行纠错调试（Debug）。调试过程中需要源代码和二进制目标程序之间一一对应的关系， 这样才能定位到错误代码，所以 Debug 版本的程序是臃肿而不进行优化的。

   与之相对的是 Release 发行版，在纠正了发觉到的错误后，需要发布程序用于实际用途，实际应用时强调运行效率高，减少冗余代码，因此会对二进制程序进行大量优化，提升性能。这样发布的二进制目标程序就是 Release 版。

- Debug 版本程序通常链接的也是 Debug 版本的库文件，比如 libQt5Guid.a/Qt5Guid.dll，库文件的简短名（不含扩展名）都是以 d 结尾的，Debug 库通常都比较大 。
- Release 版本程序链接的通常就是 Release 版本的库文件，Release 版本库文件名字比 Debug 版本库文件少一个字母 d ，如 libQt5Gui.a/Qt5Gui.dll，而且 Release 版本库一般都比 Debug 版本小很多，运行效率也高很多。



##  动态链接 和 静态链接

Dynamic Link 即动态链接，Static Link 即静态链接。

###  动态链接库

目标程序通常都不是独立个体，生成程序时都需要链接其他的库，要用到其他库的代码。对于多个程序同时运行而言，内存中就可能有同一个库的多个副本，占用了太多内存而干的活差不多。
为了优化内存运用效率，引入了动态链接库（Dynamic Link Library），或叫共享库（Shared Object）。使用动态链接库时，内存中只需要一份该库文件，其他程序要使用该库文件时，只要链接过来就行了。由于动态库文件外置，链接到动态库的目标程序相对比较小，因为剥离了大量库代码，而只需要一些链接指针。

### 静态链接库

静态库就是将链接库的代码和自己编写的代码都编译链接到一块，链接到静态库的程序通常比较大，但好处是运行时依赖的库文件很少，因为目标程序自己内部集成了很多库代码。

###  库文件后缀

[Linux](http://c.biancheng.net/linux_tutorial/)/Unix 系统里**静态库扩展名一般是 .a**，**动态库扩展名一般是 .so** 。

Windows 系统里 VC 编译器用的**静态库扩展名一般是 .lib**，**动态库扩展名一般是 .dll** 。



##  动态链接： 显式链接 和 隐式链接

Explicit Linking 即显式链接，Implicit Linking 即隐式链接，这两种都是动态链接库的使用方式。



动态链接库通常都有其导出函数列表， 告知其他可执行程序可以使用它的哪些函数。可执行程序使用这些导出函数有两种方式：一是在运行时使用主动加载动态库的函数，Linux 里比如用 dlopen 函数打开并加载动态库，Windows 里一般用 LoadLibrary 打开并加载动态库，只有当程序代码执行到这些函数时，其参数里的动态库才会被加载，这就是显式链接。显式链接方式是在运行时加载动态库，其程序启动时并不检查这些动态库是否存在。



隐式链接是最为常见的，所有的编译环境默认都是采用隐式链接的方式使用动态库。隐式链接会在链接生成可执行程序时就确立依赖关系，在该程序启动时，操作系统自动会检查它依赖的动态库，并一一加载到该程序的内存空间，程序员就不需要操心什么时候加载动态库了。

比如 VC 编译环境，链接时使用动态库对应的 .lib 文件（包含动态库的导出函数声明，但没有实际功能代码），在 .exe 程序运行前系统会检查依赖的 .dll，如果找不到某个动态库就会弹出报错框。

MinGW 是将动态库的导出函数声明放在了 .a 文件里，程序运行依赖的动态库也是 .dll 。

请注意，VC 链接器使用的 .lib 文件分两类，一种是完整的静态库，体积比较大，另一种是动态库的导出声明，体积比较小。MinGW 链接器使用的 .a 文件也是类似的，Qt 官方库都是按照动态库发布的，静态库只有自己编译才会有。



#  CMake 详细使用手册

https://cmake.org/cmake-tutorial/





#  其他



c语言中文网: c++教程, 如何编译和运行c++程序? http://c.biancheng.net/view/2191.html



在C语言中，我们会把重复使用或具有某项功能的代码封装成一个函数，将拥有相关功能的多个函数放在一个源文件，再提供一个对应的头文件，这就是一个模块。使用模块时，引入对应的头文件就可以。

而在 C++ 中，多了一层封装，就是类（Class）。类由一组相关联的函数、变量组成，你可以将一个类或多个类放在一个源文件，使用时引入对应的类就可以。

![c和c++项目结构](/home/zhaodao/桌面/github/c++/picture/c和c++.md  "c和c++项目结构")

**面向对象编程在代码执行效率上绝对没有任何优势，它的主要目的是方便程序员组织和管理代码，快速梳理编程思路，带来编程思想上的革新。**

# 编译和运行　c++ 程序
![编译和运行c++程序](/home/zhaodao/桌面/github/c++/picture/编译和运行c++程序.md  "编译和运行c++程序")

+ C语言源文件的后缀非常统一，在不同的编译器下都是.c　
+ C++ 源文件的后缀则有些混乱，不同的编译器支持不同的后缀，推荐使用.cpp作为 C++ 源文件的后缀，这样更加通用和规范。

## 使用gcc 命令编译和链接　.c文件
```c++
// 编译单个源文件：
gcc main.c

// 编译多个源文件：
gcc main.c module.c
```
## 使用gcc 命令 并　增加-lstdc++选项　编译和链接　.cpp文件
gcc命令在链接时默认使用C的库，只有添加了-lstdc++选项才会使用 C++ 的库。
```c++
// 编译单个源文件：
gcc main.cpp -lstdc++

// 编译多个源文件：
gcc main.cpp module.cpp -lstdc++
```
## 使用 g++ 命令　直接　编译和链接　.cpp文件
g++命令　专门用来编译 C++ 程序，广大 C++ 开发人员也都使用这个命令。
```c++
// 编译单个源文件：
g++ main.cpp

// 编译多个源文件：
g++ main.cpp module.cpp

// 使用-o选项可以指定可执行文件的名称：
g++ main.cpp -o demo
./demo
```
## gcc 和　g++ 的关系
GCC 是由 GUN 组织开发的，最初只支持C语言，是一个单纯的C语言编译器，后来 GNU 组织倾注了更多的精力，使得 GCC 越发强大，增加了对 C++、Objective-C、Fortran、Java 等其他语言的支持，此时的 GCC 就成了一个编译器套件（套装），是所有编译器的总称。

在这个过程中，gcc命令也做了相应地调整，它不再仅仅支持C语言，而是默认支持C语言，增加参数后也可以支持其他的语言。也就是说，gcc是一个通用命令，它会根据不同的参数调用不同的编译器或链接器。

但是让用户指定参数是一种不明智的行为，不但增加了学习成本，还使得操作更加复杂，所以后来 GCC 又针对不同的语言推出了不同的命令，例如g++命令用来编译 C++，gcj命令用来编译 Java，gccgo命令用来编译Go语言。

在以后使用 Linux GCC 时，我推荐使用g++命令来编译 C++ 程序，这样更加简洁和规范。

