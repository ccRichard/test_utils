# -*- coding : utf-8 -*-
# Version    : python3
# Date       : 2019-1-9 17:34:53
# Author     : cc
# Description:

import os
from configparser import ConfigParser
from common.Common import split_path


class Config(object):
    """ 解析配置文件 """

    def __init__(self, filename):
        path_dir = os.path.split(filename)[0]
        # 因为测试用例可能有多层级目录，所以要多遍历几层
        f_path = split_path(path_dir)
        f_find = False
        for i in range(len(f_path), 0, -1):
            path = os.path.join(os.path.join(*f_path[0:i]), "test.conf")
            if os.path.exists(path):
                self.path = path
                f_find = True
                break

        # 因为测试用例可能有多层级目录，所以要多遍历几层
        if not f_find:
            print("{}文件没有对应的test.conf文件。".format(filename))

        else:
            cfg = ConfigParser()
            cfg.read(self.path, encoding="utf8")
            for section in cfg.sections():
                for key, value in cfg.items(section):
                    setattr(self, key, value)

    # 更新运行情况
    def update_operation(self, dict_data):
        cfg = ConfigParser()
        cfg.read(self.path, encoding="utf8")
        for key, value in dict_data.items():
            cfg.set("operation", key, value)
            cfg.write(open(self.path, "w", encoding="utf8"))


if __name__ == "__main__":
    a = "a, b"
    b = "e:/1/2/3/4.txt"

