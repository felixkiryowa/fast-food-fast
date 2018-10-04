import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET="thisissecret"
    DATABASE_URI="postgresql://francis:atagenda1@localhost:5432/Fast_food_fast"


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    DATABASE_URI="postgresql://francis:atagenda1@localhost:5432/Fast_food_fast"
    SECRET="thisissecret"


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_URI = "postgresql://francis:atagenda1@localhost:5432/Fast_food_fast_testing"
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    DATABASE_URI = "postgres://jygaheoszazkaj:722a81b5a880b68d007828e45f57fbf98d71ee34b8b0ae3f10489920ad20a718@ec2-23-23-80-20.compute-1.amazonaws.com:5432/d41sarrnhuctiv"
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
