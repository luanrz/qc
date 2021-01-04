import os


def connect(ip, username, password):
    cmd = "sshpass -p \"" + password + "\" ssh " + username + "@" + ip
    exit_code = os.system(cmd)
    return exit_code
