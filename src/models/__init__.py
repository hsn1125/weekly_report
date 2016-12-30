#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask

Base = declarative_base()

class DB:
    session = None
    
    @classmethod
    def init_db(cls, app: Flask):
        """
        データベース設定
        :param app: Flask
        """
        DATABASE = 'mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}'.format(
            user=app.config["DB_USER"],
            password=app.config["DB_PASS"],
            hostname=app.config["DB_HOST"],
            port=app.config["DB_PORT"],
            database=app.config["DATABASE_NAME"])
        
        engine = create_engine(DATABASE, encoding='utf-8')
        
        cls.session = scoped_session(sessionmaker(autocommit=False,
                                                 autoflush=False,
                                                 bind=engine))
        Base.query = cls.session.query_property()
