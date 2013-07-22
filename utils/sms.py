# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf import settings
import requests
import urllib

SECRET_KEY = settings.SMS_SECRET_KEY
ACCESS_KEY = settings.SMS_ACCESS_KEY

def sender(to_user_number, content):
    data = {
        "secretkey": SECRET_KEY,
        "accesskey": ACCESS_KEY,
        "mobile": to_user_number,
        "content": content.encode("utf-8")
    }
    encode_url = urllib.urlencode(data)
    url = "http://sms.bechtech.cn/Api/send/data/json?%s" %encode_url
    res = requests.get(url)
    return res, True