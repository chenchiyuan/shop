# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from interface import StateInterface
from shop.models import Region

INDEX = "INDEX"
AFTER_SUBSCRIBE = "AFTER_SUBSCRIBE"

class StateIndex(StateInterface):
    def to_xml(self):
        region_id = self.meta.get("region_id", 1)
        region = Region.objects.get(id=region_id)
        categories = region.category_set.all()[:8]
        articles = [
            {
                "title": u"%s" % region.name,
                "description": u"%s" %region.description,
                "picurl": "http://cayman.b0.upaiyun.com/71509cef7a4940aea89fa6d512be8715.jpeg!medium",
                "url": ""
                }
        ]
        for category in categories:
            article = {
                "title": category.name,
                "description": "",
                "picurl": "http://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-go-next-icon.png",
                "url": ""
            }
            articles.append(article)
        return self._to_full_text(articles)

    def handle(self, content):
        return INDEX, {"region_id": self.meta.get("region_id", 1)}

class StateAfterSubscribe(StateIndex):
    pass

