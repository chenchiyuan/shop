# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from markdown import markdown as _markdown

def datetime_format(datetime):
    format = "%H:%M %Y年%m月%d日".encode("utf-8")
    return datetime.strftime(format)

def markdown(content, headers=""):
    if not headers:
        headers = [
            """<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">""",
            """<meta http-equiv="content-type" content="text/html; charset=UTF-8" />""",
            """<link href="/static/css/shop.css" rel="stylesheet" media="screen">""",
            """<link href="/static/css/jquery.mobile-1.3.1.min.css" rel="stylesheet" media="screen">"""
        ]

    content_md = _markdown(content)

    head = "<head>"
    for header in headers:
        head += header
    head += "</head>"

    result = "<html>%s<body>%s</body></html>" %(head, content_md)
    return result