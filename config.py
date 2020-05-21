from os import getenv


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:sport1337@localhost/videoLib'
    SQLALCHEMY_DATABASE_URI = getenv('database_url')
    SECRET_KEY = '123456790'
