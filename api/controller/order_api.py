"""
This module defines api views

"""
import psycopg2
import datetime
import jwt
from database.config import config
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from werkzeug.security import generate_password_hash ,check_password_hash

from flask import json
from flask import Response
from flask.views import MethodView
from connection import APP
from token_required import  token_required


class Orders(MethodView):
    """Class to define all the api end points"""
    
    def  post(self):
      
        """ insert a new order into the orders table """
        new_order = request.get_json()

        sql = """INSERT INTO orders(user_id,item_id,price,quantity)
                VALUES(%s,%s,%s,%s) RETURNING order_id;"""
        return manage_orders.execute_add_order_query(
            sql, new_order['user_id'], new_order['item_id'], new_order['quantity']
        )
    

    def execute_add_order_query(self, sql, user_id, item_id, quantity):
        conn = None

        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            #select a menu item with a specific id
            cur.execute("SELECT * FROM menu WHERE item_id=%s",(item_id, ))
            menu_item = cur.fetchall()
            item_price = menu_item[0][2]
            order_price = int(item_price) * quantity
            # execute the INSERT statement
            cur.execute(sql, (user_id, item_id, order_price, quantity,))
            # commit the changes to the database
            conn.commit()
            return jsonify({'Message':'New Customer Order Has Been  Created'})
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        

manage_orders = Orders()