class Config(object):
    SECRET_KEY = open('secret_key.txt').readline()[:-1]
    DEBUG = True
    STATIC_FOLDER = 'static'
