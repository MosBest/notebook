import getopt
import sys

def print_help():
    string = """
用法：
    python3 merge_code.py [-f] [背景图像路径] [缺陷图像路径]

帮助选项：
    -h, --help          显示帮助选项
应用程序选项：
    -f, --filePath      运行程序
        
    """
    print(string)


def receiving_parameters(argv):
    opts, args = getopt.getopt(argv[1:], '-hf:', ['help','filePath='])
    for opt_name, opt_value in opts:
        if opt_name in ('-h', '--help'):
            print_help()
            return True

        if opt_name in ('-f', '--filePath'):
            print("input background image path:", argv[2])
            print("defect image path:", argv[3])
            return True

    print("输入有误,请按以下格式操作: python3 merge_code.py [-f] [背景图像路径] [缺陷图像路径]")
    return False