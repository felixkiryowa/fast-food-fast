import psycopg2

from config import config
import psycopg2
class DropTable(object):


    def drop_last_user_added(self):

        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            # create table one by one
            cur.execute("SELECT * FROM users ORDER BY user_id DESC LIMIT 1")
            last_user = cur.fetchall()
            cur.execute("DELETE * FROM users WHERE user_id=%s",(last_user[0][0], ))
            conn.commit()

            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def drop_tables(self):
        
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

# drop_the_tables = DropTable()
# if __name__ ==  '__main__':
#     drop_the_tables.drop_tables()


def remove_created_user(self):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute("SELECT * FROM users ORDER BY user_id DESC LIMIT 1")
        last_user = cur.fetchall()
        cur.execute("DELETE  FROM users WHERE user_id=%s",(last_user[0][0], ))
        conn.commit()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def remove_menu_added(self):
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute("SELECT * FROM menu ORDER BY item_id DESC LIMIT 1")
        get_last_added_menu = cur.fetchall()
        cur.execute("DELETE  FROM menu WHERE item_id=%s",(get_last_added_menu[0][0], ))
        conn.commit()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def remove_added_user():
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1")
        get_last_added_order = cur.fetchall()
        cur.execute("DELETE  FROM orders WHERE  order_id=%s",(get_last_added_order[0][0], ))
        conn.commit()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()