import json
from src.mvc import dao
from src.share import command
from src.share.ssh import ssh


# 查询所有记录
def get_all():
    return dao.get_all()


# 查询帮助文档
def get_help_doc_content():
    return """
    连接：[<no> | <tag> ]
    增加：[ a | add ] [<ip>] [<username>] [<password>] [<tag>]
    删除：[ d | delete ] [ <no> | <tag> ]
    帮助：[ h | help ]
    退出：[ q | quit ]
    清屏：[ c | clear ]
    """


# 根据序号或标签找到指定记录
def get_record(user_input, records):
    if command.is_no(user_input, records):
        return get_record_by_no(int(user_input), records)
    else:
        return get_record_by_tag(user_input, records)


# 根据序号找到指定记录
def get_record_by_no(no, records):
    no = no - 1
    ip = records[no]["ip"]
    username = records[no]["username"]
    password = records[no]["password"]
    return ip, username, password


# 根据标签找到指定记录
def get_record_by_tag(tag, records):
    no = get_no_by_tag(tag, records)
    if no > 0:
        return get_record_by_no(no, records)
    return "", "", ""


# 根据标签找到对应序号
def get_no_by_tag(tag, records):
    for i in range(len(records)):
        if records[i]["tag"] == tag:
            return i + 1
    return -1


# 连接终端
def connect_ssh(ip, username, password):
    ssh.connect(ip, username, password)


# 增加记录
def add_record(arguments, records):
    record = {"ip": arguments[0], "username": arguments[1], "password": arguments[2], "tag": arguments[3]}
    records.append(record)
    dao.update_all(json.dumps(records))


# 删除记录集
def delete_records(arguments, records):
    for argument in arguments:
        no = -1
        if command.is_no(argument, records):
            no = int(argument)
        if command.is_tag(argument, records):
            no = get_no_by_tag(argument, records)
        if no == -1:
            return False, "参数" + argument + "有误"
        else:
            del records[no - 1]
    dao.update_all(json.dumps(records))
    return True, len(arguments)
