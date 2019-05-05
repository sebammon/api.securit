class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    JWT_SECRET_KEY = '45b88880373763126c5b53fc89720ec3'
    MONGO_URI = 'mongodb://localhost:27017/securit'