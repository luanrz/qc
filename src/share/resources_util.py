import os
RESOURCES_PATH = os.environ['HOME'] + "/.qc/"
RESOURCES_DATA = RESOURCES_PATH + "data.json"


# 资源文件读写类
class ResourceUtil:
    @staticmethod
    def read_file(filename):
        with open(filename, 'r', encoding='UTF-8') as f:
            return f.read()

    @staticmethod
    def write_file(filename, content):
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(content)

    @staticmethod
    def load_data():
        if not os.path.exists(RESOURCES_PATH):
            os.makedirs(RESOURCES_PATH)
        if not os.path.exists(RESOURCES_DATA):
            ResourceUtil.write_file(RESOURCES_DATA, "[]")
        return ResourceUtil.read_file(RESOURCES_DATA)

    @staticmethod
    def update_data(content):
        ResourceUtil.write_file(RESOURCES_DATA, content)

