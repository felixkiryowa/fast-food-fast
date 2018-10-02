"""
This module defines api views

"""
import psycopg2
import datetime
import jwt
from api.database.config import config
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from werkzeug.security import generate_password_hash ,check_password_hash
from functools import wraps


from flask import json
from flask import jsonify
from flask import request
from flask import Response
from flask.views import MethodView
# from connection import APP 


class OrderHistory(MethodView):
    """Class to define all the api end points"""
       
        
    def get(self, user_id):

        get_single_order_sql =  """
                    SELECT orders.order_id,menu.item_name,orders.price,orders.quantity,orders.order_status,orders.created_at,users.name,users.address,users.phone_number
                    FROM orders
                    INNER JOIN menu ON orders.item_id = menu.item_id
                    INNER JOIN users ON users.user_id = orders.user_id WHERE orders.user_id=%s
                    ORDER BY orders.order_id;
                """
        return user_order_history.execute_query_get_specific_user_order_history(get_single_order_sql,user_id)
            
        
    def execute_query_get_specific_user_order_history(self, sql, user_id):

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql,(user_id, ))
            specific_order_data = cur.fetchall()
            if not specific_order_data:
                return jsonify({"Message":"No User History Found !!"})
            columns = ('order_id','item_name','price', 'quantity', 'order_status','created_at', 'customer names',
            'address','phone number')
            results = []
            for row in specific_order_data:
                results.append(dict(zip(columns, row)))
            return jsonify({'User Order History':results})
    
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()  

user_order_history = OrderHistory() 
