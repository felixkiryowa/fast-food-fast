"""
This Module runs flask application
"""
from instance import APP

from instance.views import GetApiUrls

APP.env = 'development'
APP.testing = True
GetApiUrls.get_all_urls(APP)

if __name__ == '__main__':
    APP.run(debug=True)
