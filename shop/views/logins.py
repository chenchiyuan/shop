# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop import const
from django.contrib.auth import authenticate, login
from shop.helper.thirds import Third
from django.http import HttpResponseRedirect, HttpResponseForbidden

def auto_login(request):
    third_from = request.GET.get("third_from", "weixin")
    token = request.GET.get("token", "")
    next = request.GET.get("next", "")

    user = authenticate(token=token, third_from=third_from)
    if not user:
        Third.create_user(third_from, token)
        user = authenticate(token=token, third_from=third_from)
    if user.is_active:
        login(request, user)
        return HttpResponseRedirect(next)
    else:
        return HttpResponseForbidden()