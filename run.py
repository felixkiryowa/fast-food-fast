"""
This Module runs flask application by the server

"""
import os

from api.connection import create_app


config_name = "development"
APP = create_app(config_name)

if __name__ == '__main__':
    
    APP.run(debug=True)
