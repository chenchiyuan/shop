# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.weixin.weixin import WeiXin

class StateInterface(object):
    def __getattr__(self, item):
        try:
            return super(StateInterface, self).__getattribute__(item)
        except:
            return ""

    def __init__(self, from_user_name, to_user_name, **kwargs):
        self.from_user_name = from_user_name
        self.to_user_name = to_user_name
        self.__dict__.update(**kwargs)

    @classmethod
    def initial(cls, from_user_name, to_user_name, **kwargs):
        return cls(from_user_name, to_user_name, **kwargs)

    def to_xml(self):
        content = self.content
        return self._to_wx_text(content)

    def _to_wx_text(self, content=""):
        wx = WeiXin()
        xml = wx.to_text(from_user_name=self.from_user_name, to_user_name=self.to_user_name, content=content)
        return xml

    def _to_full_text(self, articles):
        wx = WeiXin()
        xml = wx.to_pic_text(from_user_name=self.from_user_name, to_user_name=self.to_user_name,
            articles=articles)
        return xml

    def handle(self, content):
        # 根据输入参数返回下一个状态和元数据
        raise NotImplemented