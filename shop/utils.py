# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

def datetime_format(datetime):
    format = "%H:%M %Y年%m月%d日".encode("utf-8")
    return datetime.strftime(format)