"""
This Module runs flask application

"""
import os


from api.connection import create_app

from api.database.create_tables import DatabaseTables

db = DatabaseTables()
config_name = "production"


APP = create_app(config_name)
db.create_tables()
if __name__ == '__main__':
    
    APP.run(debug=True)
