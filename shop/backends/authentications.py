# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.helper.thirds import Third, User

class TokenBackend(object):
    def authenticate(self, token, third_from):
        third = Third.get_third(third_from, token)
        if not third:
            return None
        else:
            return third.user

    def get_user(self, user_id):
        return User.get_by_unique(id=user_id)