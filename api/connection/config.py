
class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET="thisissecret"
    DATABASE_URI="postgresql://francis:atagenda1@localhost:5432/Fast_food_fast"


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    SECRET="thisissecret"


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URI = 'postgresql://francis:atagenda1@localhost:5432/Fast_food_fast_testing'
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
