import os
from src.share.config import Config
from src.mvc import view


def connect(ip, username, password):
    if Config().is_linux():
        if is_sshpass_installed():
            from src.share.ssh.linux import linux_sshpass_ssh
            linux_sshpass_ssh.connect(ip, username, password)
        else:
            view.print_info("（你可以安装sshpass，以获得更佳的连接体验）")
            from src.share.ssh.linux import linux_paramiko_ssh
            linux_paramiko_ssh.connect(ip, username, password)
    elif Config().is_win():
        from src.share.ssh.windows import windows_paramiko_ssh
        windows_paramiko_ssh.connect(ip, username, password)


def is_sshpass_installed():
    # cmd = "sshpass -V | grep sshpass | awk '{print $1}'"
    # result = os.popen(cmd).read()
    # return result.find("sshpass") == 0
    return os.path.isfile("/usr/bin/sshpass")
