class Config(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'