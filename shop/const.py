# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

# URL PATTERNS
URL_SHOP_ID = "(?P<shop_id>[0-9]+)"
URL_CATEGORY_ID = "(?P<category_id>[0-9]+)"
URL_REGION_ID = "(?P<region_id>[0-9]+)"
URL_ID = "(?P<id>[0-9]+)"

# DB LENGTH

DB_NAME_LENGTH = 64
DB_PHONE_LENGTH = 16
DB_ADDRESS_LENGTH = 128
DB_NOTICE_LENGTH = 1024

# CHOICES
GE = 0
TING = 1
BAO = 2
DAI = 3

UNIT_CHOICES = (
    (GE, "个"),
    (TING, "厅"),
    (BAO, "包"),
    (DAI, "袋")
)

USER_STATE = lambda user_key: "SHOP:USER:STATE:%s" %user_key