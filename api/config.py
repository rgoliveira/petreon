class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgres://postgres@db/postgres"
    ERROR_404_HELP          = False # avoid flask-restful hinting uri's
    DEBUG                   = True
    TESTING                 = False

class DevelopmentConfig(BaseConfig):
    DEBUG   = True
    TESTING = True

class TestingConfig(BaseConfig):
    DEBUG   = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG   = False
    TESTING = False

