
class Config:
    DEBUG = True
    
    # サーバ設定
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 8080
    
    # データベース設定
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_USER = "user"
    DB_PASS = "password"
    DATABASE_NAME = "weekly_report"
    
    # flask-sqlalchemyの設定
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
