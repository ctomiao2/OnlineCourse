# -*- coding: utf-8 -*-
# desc: database上层CURD接口, 外部直接调用
import utils.Singleton as Singleton

class DBMgr(object):
	__metaclass__ = Singleton.Singleton