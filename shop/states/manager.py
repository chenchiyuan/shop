# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.const import USER_STATE
from shop.states.states import StateIndex, INDEX
from utils.cache import cache

class StateManager(object):
    mapping = {
        INDEX: StateIndex
    }

    @classmethod
    def get_user_state(cls, from_user_name, to_user_name, state="index", meta={}):
        info = cache.get(USER_STATE(to_user_name))
        if not info:
            return cls.get_state(from_user_name, to_user_name, state=state, meta=meta)
        else:
            return cls.get_state(from_user_name, to_user_name, **info)

    @classmethod
    def set_user_state(cls, to_user_name, state="index", meta={}):
        info = {
            "state": state,
            "meta": meta,
            }
        return cache.set(USER_STATE(to_user_name), info)

    @classmethod
    def clear_user_state(cls, to_user_name):
        return cache.delete(USER_STATE(to_user_name))

    @classmethod
    def get_state(cls, from_user_name, to_user_name, state="index", meta={}):
        cls_name = cls.mapping.get(state, StateIndex)
        if not meta:
            return cls_name.initial(from_user_name, to_user_name, meta=meta)
        else:
            return cls_name(from_user_name, to_user_name, meta)