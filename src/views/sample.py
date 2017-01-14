from flask import (Blueprint, request, render_template, abort, current_app, redirect, url_for)
from models import db
from services.user_service import UserService

api = Blueprint('sample', __name__, url_prefix="/sample")


@api.route('/')
def index():
    """
    ユーザ一覧表示
    """
    users = UserService().get_user_list()
    return render_template('sample.html', users=users)


@api.route('/add', methods=['POST'])
def user_add():
    """
    ユーザ追加
    """
    # パラメータ取得
    name = request.form.get("name")

    # ユーザ名の指定がなかった場合はエラー
    if not name:
        current_app.logger.warning("not input name")
        return abort(400)
    try:
        # ユーザ情報の追加
        UserService().add_user(name)
        db.session().commit()
        return redirect(url_for("sample.index"))
    except Exception as e:
        current_app.logger.warning(e)
        db.session.rollback()
        return abort(500)
