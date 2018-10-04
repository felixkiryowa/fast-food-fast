"""
This Module runs flask application

"""
import os


from api.connection import create_app

from api.database.create_tables import DatabaseTables

db = DatabaseTables()



if os.getenv("APP_SETTINGS") == "testing":
    config_name = "testing"
elif os.getenv("APP_SETTINGS") == "production":
    config_name = "production"
config_name = "development"

APP = create_app(config_name)
db.create_tables()
if __name__ == '__main__':
    
    APP.run(debug=True)
