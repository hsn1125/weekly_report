#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from jinja2 import FileSystemLoader

application = Flask(__name__)

# コンフィグファイルの設定
from config import get_config
application.config.from_object(get_config(os.environ.get("WR_ENV")))

# テンプレートフォルダを変更
application.template_folder = '../templates'

# DB設定
from models import DB
DB.init_db(application)

# APIの追加
# ※APIが追加になった場合は修正をお願いします。
from views import sample
modules = list()
modules.append(sample.api)

for module in modules:
    application.register_blueprint(module)
