# -*- coding : utf-8 -*-
# Version    : python3
# Date       : 2019-1-9 10:54:34
# Author     : cc
# Description:

import os
from common.Log import log


class Parse(object):
    """ 配置表文件解析的统一处理 """

    def __init__(self, filename):
        # 标识起始行数
        self.headline = 0
        self.filename = filename
        log(u"{}文件解析的格式为{}".format(self.filename, self.__class__.__name__), "INFO")

    def __new__(cls, filename):
        if not os.path.exists(filename):
            log(u"{}文件不存在".format(filename), "ERROR")
            return None
        else:
            return object.__new__(cls)

    def add_attr(self, data_dict):
        """ 将字典的key和value添加为属性，便于访问 """
        for key, value in data_dict.items():
            setattr(self, str(key), value)
