# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from shop.states.states import StateIndex, StateAfterSubscribe, INDEX, AFTER_SUBSCRIBE

class StateManager(object):
    mapping = {
        INDEX: StateIndex,
        AFTER_SUBSCRIBE: StateAfterSubscribe,
    }

    @classmethod
    def get_user_state(cls, from_user_name, to_user_name, state="index", **kwargs):
        return cls.get_state(from_user_name, to_user_name, state=state, **kwargs)

    @classmethod
    def get_state(cls, from_user_name, to_user_name, state="index", **kwargs):
        cls_name = cls.mapping.get(state, StateIndex)
        if not kwargs:
            return cls_name.initial(from_user_name, to_user_name)
        else:
            return cls_name(from_user_name, to_user_name, **kwargs)