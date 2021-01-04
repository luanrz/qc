from src.share.ssh.linux import linux_sshpass_ssh as ssh

ip = "49.232.50.172"
username = "root"
password = "123456"
ssh.connect(ip, username, password)
