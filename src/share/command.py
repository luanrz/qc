def read_input():
    return input("请输入指令:")


def get_command(user_input):
    return user_input.split(" ")[0]


def get_arguments(user_input):
    return user_input.split(" ")[1:]


def is_add(user_input):
    command = get_command(user_input)
    return command == "a" or command == "add"


def is_delete(user_input):
    command = get_command(user_input)
    return command == "d" or command == "delete"


def is_update(user_input):
    command = get_command(user_input)
    return command == "u" or command == "update"


def is_help(user_input):
    return user_input == "h" or user_input == "help"


def is_quit(user_input):
    return user_input == "q" or user_input == "quit"


def is_clear_print(user_input):
    return user_input == "c" or user_input == "clear"


def is_no(no, records):
    return no.isdigit() and len(records) >= int(no) > 0


def is_tag(tag, records):
    for record in records:
        if record["tag"] == tag:
            return True
    return False


def is_command(command):
    return is_add(command) or is_delete(command) or is_update(command) or is_help(command) or is_quit(command)


# 检查add参数
# 如果正确，返回参数列表
# 如果错误，返回错误信息
# tag全局唯一;tag不能是命令关键字;与序号重复的tag将无效
def check_add_argument(arguments, records):
    length = len(arguments)
    if length != 0 and length != 4:
        return False, "add参数长度有误"
    tag = arguments[3]
    if is_command(tag):
        return False, "标签 [ " + tag + " ] 不能是关键字"
    if is_no(tag, records):
        return False, "标签 [ " + tag + " ] 不能与序号一致"
    if is_tag(tag, records):
        return False, "标签 [ " + tag + " ] 不能重复"
    return True, arguments


# 检查delete参数
# 如果正确，返回参数列表
# 如果错误，返回错误信息
def check_delete_argument(arguments, records):
    arguments_length = len(arguments)
    if arguments_length > len(records):
        return False, "delete参数太多"
    for argument in arguments:
        if not (is_no(argument, records) or is_tag(argument, records)):
            return False, "参数 [ " + argument + " ] 有误"
    # 参数查重
    duplicate_removal_length = len(set(arguments))
    if duplicate_removal_length < arguments_length:
        return False, "参数重复"
    # 参数排序
    arguments.sort(reverse=True)
    return True, arguments


# 接受用户输入add的参数
# （add参数为空时执行）
def input_add_argument():
    ip = input("请输入服务器IP：")
    username = input("请输入用户名：")
    password = input("请输入密码：")
    tag = input("请输入标签：")
    return ip, username, password, tag


# 接受用户输入delete的参数
# （delete参数为空时执行）
def input_delete_argument():
    return input("请输入序号或标签(多个参数以空格分开)：")
