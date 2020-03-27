# -*- coding: utf-8 -*-
from flask import Flask, render_template
from controller import api, config

app = Flask(__name__)
app.secret_key = config.SESSION_SECRET

@app.route('/')
def index():
	return api.index()

@app.route('/login', methods=['POST', 'GET'])
def login():
	return api.login()

@app.route('/reg', methods=['POST', 'GET'])
def register():
	return api.register()