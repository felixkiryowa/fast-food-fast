import os

from configparser import ConfigParser 

database_connection_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testing_db.ini')
def config_test_db(filename=database_connection_path, section='postgresqldatabase'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db