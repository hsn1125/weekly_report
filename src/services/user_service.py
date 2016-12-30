#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.user import User
from models import DB

class UserService:
	
    def __init__(self):
        pass
	
    def get_user_list(self) -> dict:
        """
        全ユーザリストを取得
        :return: {id: name}
        """
        users = DB.session().query(User).all()
        user_list = dict()
        for user in users:
            user_list[user.id] = user.name
        return user_list
		
		