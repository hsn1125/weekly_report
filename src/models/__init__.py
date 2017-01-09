from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = db.Model
Column = db.Column
ForeignKey = db.ForeignKey
Index = db.Index

SmallInteger, Integer, Float = db.SmallInteger, db.Integer, db.Float
String, Text = db.String, db.Text
Date, DateTime = db.Date, db.DateTime
LargeBinary = db.LargeBinary

relationship, backref = db.relationship, db.backref

# テーブルが追加になった場合は修正をお願いします。
from models.user import User
