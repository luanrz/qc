import sys
from src.mvc import service, view, controller


# 进入首页
def home():
    controller.main()


# 直连
def direct_connect(tag):
    records = service.get_all()
    ip, username, password = service.get_record_by_tag(tag, records)
    if ip == "":
        view.print_error("qc参数输入有误：标签不存在")
    else:
        service.connect_ssh(ip, username, password)


def main():
    if len(sys.argv) == 1:
        home()
    tag = sys.argv[1]
    if tag == "":
        home()
    else:
        direct_connect(tag)


if __name__ == '__main__':
    main()
