# -*- coding: utf-8 -*-
import utils.log as log

class TestBase(object):

	def run(self):
		pass

class LogTest(TestBase):

	def run(self):
		log.info('jack', 'TEST-TAG', 'TEST-CONENT')
		log.info('jack', 'TEST-TAG', 'TEST-CONENT, name=%s, old=%s', 'jobx', 12)
		log.error('jack', 'TEST-TAG', 'TEST-CONENT')
		log.error('jack', 'TEST-TAG', 'TEST-CONENT, name=%s, old=%s', 'jobx', 12)
		print 'LogTest PASS...'
