import json

from src.share.resources_util import ResourceUtil


def get_all():
    return json.loads(ResourceUtil.load_data())


def update_all(content):
    ResourceUtil.update_data(content)
