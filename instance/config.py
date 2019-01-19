from typing import Optional
import os

class Config(object):
    DEBUG: bool = False
    CSRF_ENABLED: bool = True
    SECRET: Optional[str] = os.getenv('SECRET')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'stagin': StagingConfig,
    'production': ProductionConfig,
}
