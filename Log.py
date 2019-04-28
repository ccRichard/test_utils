# -*- coding : utf-8 -*-
# Version    : python3
# Date       : 2019-1-9 18:59:01
# Author     : cc
# Description:

import os
import time
import logging


class Log(object):
    def __init__(self):
        self.path = os.path.join(__file__.split("common")[0], "log", "test.log")

    def write_log(self, message, level="ERROR"):
        """ 定义常用的几种log级别，INFO只打印，WARN和ERROR不但打印还会写入log文件 """
        logger = logging.getLogger("checklog")
        logger.setLevel(logging.INFO)

        # write log handler
        fh = logging.FileHandler(self.path, "a+")
        fh.setLevel(logging.INFO)

        # print log handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # log formatter
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s",\
                                      datefmt="%Y-%m-%d %H:%M:%S")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add handler to logger
        logger.addHandler(fh)
        logger.addHandler(ch)

        if level == "INFO":
            logger.info(message)
        elif level == "WARN":
            logger.warning(message)
        elif level == "Passed":
            logger.info("Test Passed:{}".format(message))
        elif level == "Failed":
            logger.info("Test Failed:{}".format(message))
        else:
            logger.error(message)

        # 输出log后需要释放句柄，否则下次调用logger会重复输出上次的内容
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def backup_log(self):
        """ test.log文件备份，重名时添加上修改时间 """
        if os.path.exists(self.path):
            modify_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(os.stat(self.path).st_mtime))
            new_file = os.path.splitext(self.path)
            new_name = new_file[0] + modify_time + new_file[1]
            if os.path.exists(new_name):
                new_name = new_file[0] + modify_time + "-" + time.time() + new_file[1]

            os.rename(self.path, new_name)


check_log = Log()


def log(message, level="ERROR"):
    """ 给其他地方调用的log接口 """
    check_log.write_log(message, level)

