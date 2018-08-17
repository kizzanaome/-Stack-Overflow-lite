class BaseConfig(object):
    """common configuratins that are common accros all environment"""
    DEBUG = True
    CSRF_ENABLED =True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
   
    Testing =True

class ProductionConfig(BaseConfig):

    DEBUG=False
    Testing =False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


