# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from shop.models import Notice

class NoticeListView(TemplateView):
    template_name = "shop/notices.html"

    def get_context_data(self, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)
        region_id = kwargs.get("region_id", 1)
        notices = Notice.objects.filter(region_id=region_id)
        context['notices'] = notices
        return context

class NoticeDetailView(View):
    def get(self, request, *args, **kwargs):
        notice_id = kwargs.get("id", 1)
        notice = Notice.objects.get(id=notice_id)
        return HttpResponse(notice.content)
