#-*- coding: utf-8 -*-

from restful.macro import MACRO


def row2dict(row):
    if type(row) == list:
        return _row2dict4list(row)
    else:
        return _row2dict(row)


def _row2dict(row):
    d = dict()
    for k, v in row.items():
        d[k] = v
    return d


def _row2dict4list(row_list):
    d_list = []
    for row in row_list:
        d = row2dict(row)
        d_list.append(d)
    return d_list


def get_offset_limit(self, max_count=MACRO.DEFAULT_MAX_COUNT):
    offset = int(self.get_argument('offset', MACRO.ZERO))
    limit = int(self.get_argument('limit', MACRO.DEFAULT_COUNT))
    return offset, _get_limit(limit, max_count)


def _get_limit(limit, max_count):
    """
    限制 list 请求数
    """
    if MACRO.DEFAULT_MIN_COUNT > limit:
        return MACRO.DEFAULT_MIN_COUNT
    if max_count < limit:
        return max_count
    return limit
