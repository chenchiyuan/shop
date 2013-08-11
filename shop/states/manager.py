# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.states.states import StateIndex, INDEX

class StateManager(object):
    mapping = {
        INDEX: StateIndex
    }

    @classmethod
    def get_user_state(cls, from_user_name, to_user_name, state="index", meta={}):
        return cls.get_state(from_user_name, to_user_name, state=state, meta=meta)

    @classmethod
    def get_state(cls, from_user_name, to_user_name, state="index", meta={}):
        cls_name = cls.mapping.get(state, StateIndex)
        if not meta:
            return cls_name.initial(from_user_name, to_user_name, meta=meta)
        else:
            return cls_name(from_user_name, to_user_name, meta)