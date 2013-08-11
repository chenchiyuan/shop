# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from weixin import WeiXin
from shop.states import State

class WeiXinReceiver(object):
    @classmethod
    def get_state(cls, post_data):
        w = WeiXin.on_message(post_data)
        json_data = w.to_json()
        msg_type = json_data.get("MsgType", "")
        handler = getattr(cls, msg_type, cls.text)
        return handler(**json_data)

    @classmethod
    def event(cls, FromUserName, ToUserName, **kwargs):
        state = State.after_subscribe(to_user_name=FromUserName, from_user_name=ToUserName)
        return state

    @classmethod
    def text(cls, FromUserName, ToUserName, **kwargs):
        state = State(to_user_name=FromUserName, from_user_name=ToUserName)
        state.handle(kwargs.get("Content", ""))
        return state