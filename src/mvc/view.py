import os
from src.share.config import Config


# 打印分割线
def print_line(width):
    if width == 0:
        width = os.get_terminal_size().columns
    for i in range(width):
        print("-", end='')
    print()


# 打印一行
def print_tr(no, ip, username, tag):
    format_str = "  %-10s %-20s %-20s %-20s  "
    print(format_str % (no, ip, username, tag))


# 打印表格
def print_table(data):
    print_line(80)
    print_tr("no", "ip", "username", "tag")
    print_line(80)
    length = len(data)
    if length != 0:
        for i in range(length):
            tr = data[i]
            print_tr(str(i + 1), tr["ip"], tr["username"], tr["tag"])
    else:
        print_error("  当前没有任何记录（请使用a或add命令添加记录）")
    print_line(80)


# 清屏
def clear_screen():
    cmd = ""
    if Config().is_linux():
        cmd = "clear"
    elif Config().is_win():
        cmd = "cls"
    os.system(cmd)


# 打印普通信息
def print_info(text):
    print(text)


# 打印错误信息
def print_error(text):
    if Config().is_linux() or Config().is_win10():
        print(Color.ERROR + text + Color.DEFAULT)
    elif Config().is_win7():
        print_info(text)


# 打印成功信息
def print_success(text):
    if Config().is_linux() or Config().is_win10():
        print(Color.SUCCESS + text + Color.DEFAULT)
    elif Config().is_win7():
        print_info(text)


def print_reverse(text):
    if Config().is_linux() or Config().is_win10():
        print(Color.REVERSE + text + Color.DEFAULT)
    elif Config().is_win7():
        print_info(text)


class Color:
    DEFAULT = "\033[0m"
    SUCCESS = "\033[1;32;40m"
    ERROR = "\033[1;31;40m"
    REVERSE = "\33[7m"
