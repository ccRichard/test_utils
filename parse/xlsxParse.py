# -*- coding : utf-8 -*-
# Version    : python3
# Date       : 2019-1-28 19:25:19
# Author     : cc
# Description:

import xlrd
from parse.Parse import Parse


class XlsxParse(Parse):
    """ 解析excel文件，索引key是分页名和表头拼接起来的，例如：sheet1_id """

    def __init__(self, filename):
        super(XlsxParse, self).__init__(filename)
        self.headline = 2
        self.parse()

    def parse(self):
        """ 解析xlsx文件"""
        sheet_dict = dict()

        xs = xlrd.open_workbook(self.filename)
        sheets = xs.sheet_names()

        # 遍历所有页签
        for sheet in sheets:
            # table_dict = dict()
            sheet_data = xs.sheet_by_name(sheet)
            # 舍弃空的sheet数据
            if sheet_data.nrows < 1:
                continue
            # 取第一行作为表头索引
            head_len = sheet_data.row_len(0)

            # 根据表头取出每列数据
            for i in range(0, head_len):
                values = sheet_data.col_values(i)

                # 遍历处理下一些特殊的字段值
                for j in range(0, len(values)):

                    # xlrd会将int转为float，这里转回来
                    if isinstance(values[j], float) and str(values[j]).split(".")[-1] == "0":
                        values[j] = int(values[j])

                    # 将"1001,1002,1003"这样的复合值转为list
                    if isinstance(values[j], str) and values[j].find(",") >= 0:
                        values[j] = values[j].split(",")

                # 将sheet和[非空]表头合并作为字典key值
                if values[0] != "":
                    arr_key = sheet + "_" + str(values[0])
                    sheet_dict[arr_key] = values[1:]
                # table_dict[values[0]] = values[1:]
            # sheet_dict[sheet] = table_dict

        # 根据data_dict的内容为类重新添加属性
        super(XlsxParse, self).add_attr(sheet_dict)
