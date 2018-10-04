import unittest
import os
import json

from api.connection import create_app
from api.database.config import config

# from ...connection import create_app
from api.database.create_testing_database_tables import CreateTables

from api.database.drop_table import DropTable

from api.controller.auth_api import *

class OrderApiTestCase(unittest.TestCase):

    
    """This class represents the order api test case"""

    def setUp(self):

        """Define test variables and initialize app."""

        self.APP = create_app(config_name="testing")
        self.client = self.APP.test_client
        create_new_tables = CreateTables()
        
        self.user_data = {
            "name":"David Buwembo",
            "username":"Papa",
            "password":"user123",
            "address":"Ntinda",
            "phone_number":"0700160998",
            "user_type":"admin"
        }

        self.customer_user = {
            "name":"Ntale Shadik",
            "username":"shadik",
            "password":"user123",
            "address":"Nakawa",
            "phone_number":"0700167896",
            "user_type":"user"
        }

        self.login_credentials_admin = {
            "username":"Papa",
            "password":"user123"
        }
        self.login_credentials_user = {
            "username":"neli",
            "password":"user123"
        }
        self.order_status =   {
                "order_status":"Processing"
            }

        self.menu = {
            "item_name":"Beans",
            "price":50000,
            "current_items":40
          }
        self.order = {
            "quantity":23 
        }
        self.client().post(
            '/api/v2/auth/signup',content_type='application/json',
             data=json.dumps(self.user_data))
        res = self.client().post('/api/v2/auth/login',content_type='application/json',
         data=json.dumps(
             self.login_credentials_admin
             )
        )
        user = self.client().post('/api/v2/auth/login', content_type='application/json',
         data=json.dumps(self.login_credentials_user)
         )
        self.result = json.loads(res.data.decode())
        
        self.assertTrue(self.result['token_generated'])
        print(self.result,"token data")
        self.result = json.loads(res.data)
        self.result2 = json.loads(user.data)
        self.generated_token = self.result['token_generated']
        self.user_generated_token = self.result2['token_generated']

        self.auth_header = {
        'x-access-token': self.generated_token
        }
        self.user_auth_header = {
        'x-access-token': self.user_generated_token
        }
        
        with self.APP.app_context():
            # create all tables
            create_new_tables.create_tables()

    def tearDown(self):
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
            # cur.execute("SELECT * FROM menu ORDER BY item_id DESC LIMIT 1")
            # get_last_added_menu = cur.fetchall()
            # cur.execute("DELETE  FROM menu WHERE item_id=%s",(get_last_added_menu[0][0], ))
            # cur.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1")
            # get_last_added_order = cur.fetchall()
            # cur.execute("DELETE  FROM orders WHERE  order_id=%s",(get_last_added_order[0][0], ))

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

    def test_add_new_menu(self):
        res = self.client().post('/api/v2/menu',content_type='application/json',
            data=json.dumps(self.menu),headers=self.auth_header)
        self.assertEqual(res.status_code,201)

             
    def test_order_creation(self):

        """Test API  can create an order (POST request)"""

        res = self.client().post(
            '/api/v2/users/orders', 
            content_type='application/json',
            data=json.dumps(
                self.order
            ),
            headers = self.user_auth_header
        )
        result = json.loads(res.data.decode())
        self.assertEqual(result['Message'], "New Customer Order Has Been  Created")
        self.assertEqual(res.status_code, 201)
        
        
    def test_get_all_orders(self):
        res = self.client().get('/api/v2/orders/',content_type='application/json',
            data=json.dumps(self.menu),headers=self.auth_header)
        self.assertEqual(res.status_code,200)

    def test_get_single_order(self):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM orders ORDER BY item_id DESC LIMIT 1")
        last_order_item = cur.fetchall()
        order_id = last_order_item[0][0]
        get_string = str(order_id)
        res = self.client().get('/api/v2/orders/'+get_string,content_type='application/json',
            headers=self.auth_header)
        self.assertEqual(res.status_code,200)

    def test_update_order(self):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM orders ORDER BY item_id DESC LIMIT 1")
        last_order_item = cur.fetchall()
        order_id = last_order_item[0][0]
        get_string = str(order_id)
        result = self.client().put(
        '/api/v2/orders/'+get_string, content_type='application/json',
        data=json.dumps(
          self.order_status
        ),
        headers=self.auth_header
        )
        self.assertEquals(result.status_code,200)
        # get updated order
        order = self.client().get('/api/v2/orders/'+get_string,content_type='application/json',
            headers=self.auth_header)
        self.assertEqual(order.status_code,200)
        #get json data
        # json_data = order.data
        # self.assertEqual(json_data[0][5],"Decline")

    def test_get_history_by_user(self):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM users ORDER BY user_id DESC LIMIT 1")
        last_user_in_table = cur.fetchall()
        user_id = last_user_in_table[0][0]
        get_string = str(user_id)
        res = self.client().get('/api/v2/users/orders/'+get_string,content_type='application/json',
            headers=self.user_auth_header)
        self.assertEqual(res.status_code,200)


        

