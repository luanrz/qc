import paramiko
import sys
import threading
import re
from src.share.config import Config


def connect(ip, username, password):
    trans = paramiko.Transport((ip, 22))
    trans.start_client()
    trans.auth_password(username=username, password=password)
    channel = trans.open_session()
    channel.get_pty()
    channel.invoke_shell()

    def write(channel):
        while True:
            data = channel.recv(1024)
            result = format_result(data.decode())
            sys.stdout.write(result)
            sys.stdout.flush()

    def format_result(result):
        # Windows7不支持终端颜色显示
        if Config().is_win7():
            # linux颜色标识字符串
            linux_color_regex = r"(\[(\w|;)*m)|()"
            # linux_color_regex = r"(\[01;34m)|(\[0m)|()"
            # 删除linux颜色标识字符串
            result = re.sub(linux_color_regex, "", result)
        return result

    threading.Thread(target=write, args=[channel, ]).start()

    exit_code = ["", "", "", ""]

    def is_exit_code(cmd):
        for i in range(3, -1, -1):
            exit_code[i] = exit_code[i - 1]
        exit_code[0] = cmd
        return "tixe" == "".join(exit_code)

    while True:
        cmd = sys.stdin.read(1)
        channel.send(cmd)
        if is_exit_code(cmd):
            break

