class Config(object):
    SECRET_KEY = open('utils/secret_key.txt').readline()[:-1]
    DEBUG = True
    STATIC_FOLDER = 'static'
