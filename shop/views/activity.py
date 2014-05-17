# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
import datetime
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from shop.models import Activity, ActivityTime, ActivityAddress
import json
import time


def json_response(json_data, **kwargs):
    data = json.dumps(json_data)
    return HttpResponse(data, content_type='application/json', **kwargs)


class ActivityApiView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ActivityApiView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        activities = Activity.objects.all()
        response_dict = {
            "activities": map(lambda a: a.to_json(), activities)
        }
        return json_response(response_dict)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "")
        owner = request.POST.get("owner", "")
        description = request.POST.get("description", "")
        times = request.POST.get("datetime", "")
        addresses = request.POST.get("address", "")

        activity = Activity(name=name, owner=owner, description=description)
        activity.save()

        for timestamp in times.split(","):
            d = datetime.datetime.fromtimestamp(float(timestamp))
            activity_time = ActivityTime(activity=activity, datetime=d)
            activity_time.save()

        for address in addresses.split(","):
            activity_address = ActivityAddress(activity=activity, address=address)
            activity_address.save()

        return json_response(activity.to_json())


class ActivityTimeVoteView(View):
    def get(self, request, *args, **kwargs):
        activity_time = ActivityTime.objects.get(**kwargs)
        activity_time.vote += 1
        activity_time.save()
        return json_response(activity_time.to_json())


class ActivityAddressVoteView(View):
    def get(self, request, *args, **kwargs):
        activity_address = ActivityAddress.objects.get(**kwargs)
        activity_address.vote += 1
        activity_address.save()
        return json_response(activity_address.to_json())