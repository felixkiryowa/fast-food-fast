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
        
    @token_required
    def get(self,current_user, order_id):
        if not current_user[0][6]:
            return jsonify({'Message':'Cannot Perform That Function!'})

        get_single_order_sql =  """
                    SELECT orders.order_id,menu.item_name,orders.price,orders.quantity,orders.order_status,orders.created_at,users.name,users.address,users.phone_number
                    FROM orders
                    INNER JOIN menu ON orders.item_id = menu.item_id
                    INNER JOIN users ON users.user_id = orders.user_id WHERE orders.order_id=%s
                    ORDER BY orders.order_id;
                """
        
        get_all_orders_sql =  """
                    SELECT orders.order_id,menu.item_name,orders.price,orders.quantity,orders.order_status,orders.created_at,users.name,users.address,users.phone_number
                    FROM orders
                    INNER JOIN menu ON orders.item_id = menu.item_id
                    INNER JOIN users ON users.user_id = orders.user_id
                    ORDER BY orders.order_id;
                """
        if order_id is None:
            return manage_orders.execute_query_get_all_orders(get_all_orders_sql)
        return manage_orders.execute_query_get_specific_order(get_single_order_sql,order_id)

    @token_required   
    def put(self, current_user, order_id) :
        if not current_user[0][6]:
            return jsonify({'Message':'Cannot Perform That Function!'})
        get_single_order_sql =  """
                    SELECT orders.order_id,menu.item_name,orders.price,orders.quantity,orders.order_status,users.name,users.address,users.phone_number
                    FROM orders
                    INNER JOIN menu ON orders.item_id = menu.item_id
                    INNER JOIN users ON users.user_id = orders.user_id WHERE orders.order_id=%s
                    ORDER BY orders.order_id;
                """
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM orders WHERE order_id=%s",(order_id, ))
            check_order_exist = cur.rowcount
            if check_order_exist == 0:
                return jsonify({'Messsage':'No Order Found!!'})
            cur.execute("UPDATE orders SET order_status=%s WHERE order_id=%s",(request.json['order_status'], order_id,))
            conn.commit()
            return manage_orders.execute_query_get_specific_order(get_single_order_sql, order_id)
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()    
              
        
    def execute_query_get_all_orders(self, sql):

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql)
            returned_orders_data = cur.fetchall()
            if not returned_orders_data:
                return jsonify({"Message":"No Order Entries Found !!"})
            columns = ('order_id','item_name','price', 'quantity', 'order_status','created_at', 'customer names',
            'address','phone number')
            results = []
            for row in returned_orders_data:
                results.append(dict(zip(columns, row)))
            return jsonify({'All_orders':results})

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()  
        
    def execute_query_get_specific_order(self, sql, order_id):

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql,(order_id, ))
            specific_order_data = cur.fetchall()
            if not specific_order_data:
                return jsonify({"Message":"No Order Found !!"})
            columns = ('order_id','item_name','price', 'quantity', 'order_status', 'created_at', 'customer names',
            'address','phone number')
            results = []
            for row in specific_order_data:
                results.append(dict(zip(columns, row)))
            return jsonify({'Specific_order':results})
    
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()   



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