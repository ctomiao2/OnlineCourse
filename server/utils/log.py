# -*- coding: utf-8 -*-
import time

def info(uid, tag, content, *args):
	_write_log('INFO', uid, tag, content, *args)

def error(uid, tag, content, *args):
	_write_log('ERROR', uid, tag, content, *args)

def _write_log(level, uid, tag, content, *args):
	time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	content = content % args
	format_str = '%s [%s]: uid=%s, tag=%s, content=%s' % (time_str, level, uid, tag, content)
	print format_str