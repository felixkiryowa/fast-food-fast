import flask
from api.app.views import OrderApiUrls

from api.instance.config import app_config

from api.database.config import config


def create_app(config_name):
    
    APP = flask.Flask(__name__)
    APP.config.from_object(app_config[config_name])
    APP.config.from_pyfile('config.py')
    APP.config['SECRET_KEY'] = 'thisissecret'
    OrderApiUrls.get_all_urls(APP)

    return APP
