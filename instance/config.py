class BaseConfig(object):
    """common configuratins that are common accros all environment"""
    DEBUG = True
    CSRF_ENABLED =True

class DevelopmentConfig(BaseConfig):
    """development configurations
       setting Testing to True activates the testing mode of Flask extensions. 
    """
    DEBUG = True
     

    Testing =True

class ProductionConfig(BaseConfig):

    """
    Production configurations

    """

    DEBUG=False
    Testing =False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


