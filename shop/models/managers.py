# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.contrib.auth.models import BaseUserManager
from shop import const

class UserManager(BaseUserManager):
    def create_user(self, token, third_from=const.LOCAL, password=None, **kwargs):
        if not token:
            raise ValueError("需要有Token")


        user = self.model(token = token,
            third_from = third_from,
            **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, token, third_from=const.LOCAL, password=None):
        user = self.create_user(token, third_from=third_from, password=password,
            is_admin=True, is_staff=True, is_superuser=True)
        return user