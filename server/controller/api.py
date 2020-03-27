# -*- coding: utf-8 -*-
# desc: REST api handler
from flask import request, redirect, url_for, make_response, render_template, session
import config
import hashlib
import utils.log as log
import db.mysql.MySQLHelper as MySQLHelper

def verify_login(user_name, psw):
	if not user_name or not psw:
		return False
	key = '%s_%s_%s' % (user_name, psw, config.MD5_KEY)
	crypt_psw = hashlib.md5(key.encode()).hexdigest()
	log.info(user_name, 'api::verify_login', 'psw=%s, crypt_psw=%s', psw, crypt_psw)
	return True

def index():
	# 已登录
	if 'user_name' in session:
		return render_template('index.html')
	else:
		return redirect(url_for('login'))

def register():
	# 已登录
	if 'user_name' in session:
		return render_template('index.html')
	elif request.method == "GET":
		return render_template('reg.html')
	else:
		# TODO
		session['user_name'] = request.form['user_name']
		return redirect(url_for('index'))

def login():
	if request.method == "POST":
		if verify_login(request.form['user_name'], request.form['password']):
			session['user_name'] = request.form['user_name']
			#resp = make_response(render_template('index.html'))
			#resp.set_cookie('user_name', request.form['user_name'])
			#resp.set_cookie('password', request.form['password'])
			return redirect(url_for('index'))
		else:
			return render_template('login.html', user_name=user_name, password=psw, error=True)
	else:
		user_name = request.cookies.get('user_name')
		psw = request.cookies.get('password')
		return render_template('login.html', user_name=user_name, password=psw)

def logout():
	pass