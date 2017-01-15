import os
from models import db
from flask import Flask

application = Flask(__name__)

# コンフィグファイルの設定
from config import get_config
application.config.from_object(get_config(os.environ.get("WR_ENV")))

# テンプレートフォルダを変更
application.template_folder = '../templates'

# 静的ファイルの格納フォルダを変更
application.static_folder = "../static"

# DB設定
application.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}'.format(
    user=application.config["DB_USER"],
    password=application.config["DB_PASS"],
    hostname=application.config["DB_HOST"],
    port=application.config["DB_PORT"],
    database=application.config["DATABASE_NAME"])
db.init_app(application)

# APIの追加
# ※APIが追加になった場合は修正をお願いします。
from views import sample
modules = list()
modules.append(sample.api)

for module in modules:
    application.register_blueprint(module)


@application.before_first_request
def init():
    db.create_all()
