import select
import sys
import termios
import tty

import paramiko


def connect(ip, username, password):
    # 建立一个socket
    transport = paramiko.Transport((ip, 22))
    # 启动一个客户端
    transport.start_client()
    # 使用用户名和密码登录
    transport.auth_password(username=username, password=password)
    # 打开一个通道
    channel = transport.open_session()
    # 获取终端
    channel.get_pty()
    # 激活终端，这样就可以登录到终端了，就和我们用类似于xshell登录系统一样
    channel.invoke_shell()

    # 获取原操作终端属性
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        # 将现在的操作终端属性设置为服务器上的原生终端属性,可以支持tab了
        tty.setraw(sys.stdin)
        channel.settimeout(0)

        while True:
            readlist, writelist, errlist = select.select([channel, sys.stdin, ], [], [])
            # 如果是用户输入命令了,sys.stdin发生变化
            if sys.stdin in readlist:
                # 获取输入的内容，输入一个字符发送1个字符
                input_cmd = sys.stdin.read(1)
                # 将命令发送给服务器
                channel.sendall(input_cmd)

            # 服务器返回了结果,channel通道接受到结果,发生变化 select感知到
            if channel in readlist:
                # 获取结果
                result = channel.recv(1024)
                # 断开连接后退出
                if len(result) == 0:
                    break
                # 输出到屏幕
                sys.stdout.write(result.decode())
                sys.stdout.flush()
    finally:
        # 执行完后将现在的终端属性恢复为原操作终端属性
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    # 关闭通道
    channel.close()
    # 关闭链接
    transport.close()

