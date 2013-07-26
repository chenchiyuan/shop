# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.models import WeiXin
from shop.models import User
from shop import const

class Third(object):
    mapping = {
        "weixin": WeiXin,
    }
    @classmethod
    def get_third(cls, third_from, token):
        model = cls.mapping.get(third_from)
        if not model:
            raise Exception("没有第三方")

        return model.get_by_unique(token=token)

    @classmethod
    def create_user(cls, third_from, token):
        model = cls.mapping.get(third_from)
        if not model:
            raise Exception("没有第三方")

        third = const.THIRD_FROM_DICT.get(third_from, const.LOCAL)
        user = User.objects.create_user(token=token, third_from=third)

        m = model(token=token, user=user)
        m.save()
        return user