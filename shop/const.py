# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.conf import settings

# URL PATTERNS
URL_SHOP_ID = "(?P<shop_id>[0-9]+)"
URL_CATEGORY_ID = "(?P<category_id>[0-9]+)"
URL_REGION_ID = "(?P<region_id>[0-9]+)"
URL_NOTICE_ID = "(?P<notice_id>[0-9]+)"
URL_ID = "(?P<id>[0-9]+)"

# DB LENGTH

DB_NAME_LENGTH = 64
DB_PHONE_LENGTH = 16
DB_ADDRESS_LENGTH = 128
DB_MESSAGE_LENGTH = 512
DB_NOTICE_LENGTH = 1024

LOCAL = 0
WEIXIN = 1
WEIBO = 2

THIRD_FROM_DICT = {
    "weixin": WEIXIN,
    "weibo": WEIBO,
    "local": LOCAL
}

THIRD_FROM_CHOICES = (
    (LOCAL, "本地"),
    (WEIXIN, "微信"),
    (WEIBO, "微博")
)

ORDER_FAIL = 0
ORDER_CREATED = 1
ORDER_SENT = 2
ORDER_SUCCESS = 3

ORDER_STATUS_CHOICES = {
    (ORDER_FAIL, "失败"),
    (ORDER_CREATED, "创建"),
    (ORDER_SENT, "已发送"),
    (ORDER_SUCCESS, "成功")
}

USER_STATE = lambda user_key: "SHOP:USER:STATE:%s" %user_key

SHOP_PICTURE_DEFAULT = "http://%s/static/assets/community/%s" %(settings.DOMAIN_NAME, "shop_default.png")
PRODUCT_PICTURE_DEFAULT = "http://%s/static/assets/community/%s" %(settings.DOMAIN_NAME, "item_default.png")
ARROW_IMAGE = ""#"http://%s/static/assets/community/%s" %(settings.DOMAIN_NAME, "arrow.png")

def auto_login_url(url, token, third_from="weixin"):
    return "http://%s/login/auto/?token=%s&third_from=%s&next=%s" %(settings.DOMAIN_NAME, token, third_from, url)
