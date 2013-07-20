# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

import hashlib
import xml.etree.ElementTree as ET
import time

class WeiXin(object):
    def __init__(self, token=None, timestamp=None, nonce=None, signature=None, echostr=None, xml_body=None):
        self.token = token
        self.timestamp = timestamp
        self.nonce = nonce
        self.signature = signature
        self.echostr = echostr

        self.xml_body = xml_body

    @classmethod
    def on_connect(cls, token=None, timestamp=None, nonce=None, signature=None, echostr=None):
        obj = WeiXin(token=token,
            timestamp=timestamp,
            nonce=nonce,
            signature=signature,
            echostr=echostr)
        return obj

    @classmethod
    def on_message(cls, xml_body):
        obj = WeiXin(xml_body=xml_body)
        return obj

    def to_json(self):
        '''http://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.XML
        '''
        j = {}
        root = ET.fromstring(self.xml_body)
        for child in root:
            if child.tag == 'CreateTime':
                value = long(child.text)
            else:
                value = child.text
            j[child.tag] = value
        return j

    def _to_tag(self, k):
        return ''.join([w.capitalize() for w in k.split('_')])

    def _cdata(self, data):
        '''http://stackoverflow.com/questions/174890/how-to-output-cdata-using-elementtree
        '''
        if type(data) is str:
            return '<![CDATA[%s]]>' % data.replace(']]>', ']]]]><![CDATA[>')
        return data

    def to_text(self, **kwargs):
        kwargs['create_time'] = time.time()
        kwargs['msg_type'] = "text"
        kwargs['func_flag'] = "0"

        xml = '<xml>'
        def cmp(x, y):
            ''' WeiXin need ordered elements?
            '''
            orderd = ['to_user_name', 'from_user_name', 'create_time', 'msg_type', 'content', 'func_flag']
            try:
                ix = orderd.index(x)
            except ValueError:
                return 1
            try:
                iy = orderd.index(y)
            except ValueError:
                return -1
            return ix - iy
        for k in sorted(kwargs.iterkeys(), cmp):
            v = kwargs[k]
            tag = self._to_tag(k)
            xml += '<%s>%s</%s>' % (tag, self._cdata(v), tag)
        xml += '</xml>'
        return xml

    def to_pic_text(self, to_user_name, from_user_name, articles, msg_type="news"):
        """
            articles = [
                {
                    title,
                    description,
                    picurl,
                    url
                }
            ]
        """
        create_time = time.time()
        article_count = len(articles)
        xml = '<xml>'
        xml += '<ToUserName>%s</ToUserName>' %self._cdata(to_user_name)
        xml += '<FromUserName>%s</FromUserName>' %self._cdata(from_user_name)
        xml += '<CreateTime>%d</CreateTime>' %create_time
        xml += '<MsgType>%s</MsgType>' %self._cdata(msg_type)
        xml += '<ArticleCount>%d</ArticleCount>' %article_count
        xml += '<Articles>'
        for item in articles:
            title = item.get("title", "")
            description = item.get("description", "")
            picurl = item.get("picurl", "")
            url = item.get("url", "")
            data = "<item><Title>%s</Title><Description>%s</Description><PicUrl>%s</PicUrl><Url>%s</Url></item>" \
                   %(self._cdata(title), self._cdata(description), self._cdata(picurl), self._cdata(url))
            xml += data
        xml += '</Articles>'
        xml += '<FuncFlag>1</FuncFlag></xml>'
        return xml

    def validate(self):
        params = {}
        params['token'] = self.token
        params['timestamp'] = self.timestamp
        params['nonce'] = self.nonce

        signature = self.signature
        # 不需要判断echostr，因为每个POST请求不会发echostr，只有第一次Get请求会发echostr
        # echostr = self.echostr

        if self.is_not_none(params):
            _signature = self._signature(params)
            if _signature == signature:
                return True
        return False

    def is_not_none(self, params):
        for k, v in params.items():
            if v is None:
                return False
        return True

    def _signature(self, params):
        '''http://docs.python.org/2/library/hashlib.html
        '''
        a = sorted([v for k, v in params.items()])
        s = ''.join(a)
        return hashlib.sha1(s).hexdigest()