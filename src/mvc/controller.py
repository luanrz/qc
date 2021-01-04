from src.mvc import view, service
from src.share import command


def clear_print(records):
    view.clear_screen()
    view.print_table(records)


def main():
    records = service.get_all()
    clear_print(records)
    user_input = command.read_input()
    while not (command.is_quit(user_input)):
        # 连接终端
        if command.is_no(user_input, records) or command.is_tag(user_input, records):
            ip, username, password = service.get_record(user_input, records)
            view.clear_screen()
            view.print_success("即将进入" + username + "@" + ip)
            service.connect_ssh(ip, username, password)
            clear_print(records)
            view.print_error("终端连接已断开！")
        # 增加记录
        elif command.is_add(user_input):
            arguments = command.get_arguments(user_input)
            if len(arguments) == 0:
                arguments = command.input_add_argument()
            is_checked, arguments = command.check_add_argument(arguments, records)
            if is_checked:
                service.add_record(arguments, records)
                clear_print(records)
                view.print_success(
                    "记录 [ ip:" + arguments[0] + ", username:" + arguments[1] + ", tag:" + arguments[3] + " ] 增加成功")
            else:
                clear_print(records)
                view.print_error(arguments)
        # 删除记录
        elif command.is_delete(user_input):
            arguments = command.get_arguments(user_input)
            if len(arguments) == 0:
                arguments = command.input_delete_argument()
                arguments = arguments.split(" ")
            is_checked, arguments = command.check_delete_argument(arguments, records)
            if is_checked:
                is_delete, result = service.delete_records(arguments, records)
                if is_delete:
                    clear_print(records)
                    view.print_success("成功删除" + str(result) + "条纪录")
                else:
                    clear_print(records)
                    view.print_error(result)
            else:
                clear_print(records)
                view.print_error(arguments)
        # 更新记录
        elif command.is_update(user_input):
            pass
        # 帮助文档
        elif command.is_help(user_input):
            clear_print(records)
            view.print_info(service.get_help_doc_content())
        # 清空屏幕并重新显示主界面
        elif command.is_clear_print(user_input):
            clear_print(records)
        else:
            clear_print(records)
            view.print_error("您的输入有误（输入h查看帮助文档）")
        user_input = command.read_input()


if __name__ == '__main__':
    main()
