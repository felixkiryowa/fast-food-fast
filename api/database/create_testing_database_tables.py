import psycopg2

from testing_db_config import config

class CreateTables(object):


    def create_tables(self):

        """ create tables in the PostgreSQL test database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users  (
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(200) NOT NULL UNIQUE,
                username VARCHAR(255) NOT NULL, 
                password VARCHAR(255) NOT NULL,
                address VARCHAR(255) NULL,
                phone_number VARCHAR(200) NULL,
                admin BOOLEAN  DEFAULT FALSE
            )"""
            ,
            """
            CREATE TABLE IF NOT EXISTS menu (
                    item_id SERIAL PRIMARY KEY,
                    item_name VARCHAR(255) NOT NULL,
                    price BIGINT NOT NULL,
                    current_items BIGINT NOT NULL
            )
            """
            ,
            """
            CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                item_id INTEGER NOT NULL,
                price BIGINT NOT NULL,
                quantity INTEGER NOT NULL,
                order_status VARCHAR(100)  DEFAULT 'new order',
                created_at TIMESTAMP DEFAULT NOW(),
                FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (item_id)
                    REFERENCES menu (item_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            )
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # create table one by one
            for command in commands:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


def drop_tables():
    
    """ create tables in the PostgreSQL database"""
    command = (
        """
         DROP TABLE IF EXISTS users,orders,menu CASCADE
        """
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()