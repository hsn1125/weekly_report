#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template
from services.user_service import UserService

api = Blueprint('sample', __name__, url_prefix="/sample")

@api.route('/')	
def index():
	"""
	ユーザ一覧表示
	"""
	users = UserService().get_user_list()
	return render_template('sample.html', users=users)
