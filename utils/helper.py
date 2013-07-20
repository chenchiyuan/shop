# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from django.http import QueryDict
from django.core.urlresolvers import reverse
from django.conf import settings
import urlparse
import logging
logger = logging.getLogger(__name__)

def get_full_path(value, with_query=False):
    url = urlparse.urlsplit(value)
    if with_query:
        return urlparse.urlunsplit((0, 0, url[2], url[3], url[4]))
    else:
        return urlparse.urlunsplit((0, 0, url[2], 0, 0))

def get_url_by_conf(conf, args=[], params={}):
    if params:
        q = QueryDict('').copy()
        for key in params:
            value = params[key]
            if isinstance(value, list):
                for item in value:
                    q.update({key: item})
            else:
                q.update({key: value})
        try:
            return u"%s?%s" % (reverse(conf, args=args), q.urlencode())
        except Exception:
            logger.error('URL %s for args %s params %s cannot be found.' % (conf, args, params))
    else:
        return reverse(conf, args=args)

def get_referer_url(request):
    referer_url = request.META.get('HTTP_REFERER', '/')
    host = request.META['HTTP_HOST']

    if referer_url.startswith('http') and host not in referer_url:
        referer_url = '/' # 避免外站直接跳到登录页而发生跳转错误
    elif request.GET.get('next', None):
        referer_url = request.GET.get('next')
    elif get_full_path(referer_url) in ['/user/login/', '/register/']:
        referer_url = '/'
    return referer_url

def get_domain_path(path):
    if not path:
        return "http://%s/" %settings.DOMAIN_NAME
    elif path[0] == "/":
        return "http://%s%s" %(settings.DOMAIN_NAME, path)
    else:
        return "http://%s/%s" %(settings.DOMAIN_NAME, path)
