import platform


# 配置类
class Config:
    # 操作系统类型
    __os_type = ""

    def __init__(self):
        system = platform.system()
        if system == "Linux":
            self.set_os_type("Linux")
        elif system == "Windows":
            version = platform.win32_ver()[0]
            if version == "7":
                self.set_os_type("Windows7")
            elif version == "10":
                self.set_os_type("Windows10")

    def get_os_type(self):
        return self.__os_type

    def set_os_type(self, os_type):
        self.__os_type = os_type

    def is_linux(self):
        return self.get_os_type() == "Linux"

    def is_win7(self):
        return self.get_os_type() == "Windows7"

    def is_win10(self):
        return self.get_os_type() == "Windows10"

    def is_win(self):
        return self.is_win7() or self.is_win10()
