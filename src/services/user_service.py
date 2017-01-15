from models import db
from models.user import User


class UserService:

    def __init__(self):
        pass

    def get_user_list(self) -> dict:
        """
        全ユーザリストを取得
        :return: {id: name}
        """
        users = User.query.all()
        user_list = dict()
        for user in users:
            user_list[user.id] = user.name
        return user_list

    def add_user(self, name: str):
        """
        ユーザの追加
        :param str name: user name
        :return:
        """
        user = User(name)
        db.session.add(user)
        db.session.flush()
