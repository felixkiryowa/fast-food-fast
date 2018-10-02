import unittest
import os
import json

from api.connection import create_app

# from ...connection import create_app
from api.database.create_testing_database_tables import CreateTables

from werkzeug.security import generate_password_hash

from api.controller.auth_api import *

class OrderApiTestCase(unittest.TestCase):


    
    """This class represents the order api test case"""

    def setUp(self):

        """Define test variables and initialize app."""

        self.APP = create_app(config_name="testing")
        self.client = self.APP.test_client
        create_new_tables = CreateTables()
        # This is the user test json data with a predefined username and password
        hashed_password = generate_password_hash('user@123', method='sha256')
        self.user_data = {
            "name":"Ntale Shadik",
            "username":"Papa",
            "password":"user123",
            "address":"Ntinda",
            "phone_number":"0700160998"
        }

        self.login_credentials = {
            "username":"Papa",
            "password":"user123"
        }

        self.menu = {
                    "item_name":"Chapatis",
                    "price":50000,
                    "current_items":40
        }

        with self.APP.app_context():
            # create all tables
            create_new_tables.create_tables()
        """Test user registration works correcty."""

        self.client().post('/api/v2/auth/signup',content_type='application/json', data=json.dumps(self.user_data))
        res = self.client().post('/api/v2/auth/login',content_type='application/json', data=json.dumps(self.login_credentials))
        # get the results returned in json format
        self.result = json.loads(res.data.decode())['token_generated']
        # self.result = json.loads(res.data)
        # self.generated_token = self.result['']

        self.auth_header = {
        'x-access-token': self.generated_token
        }

        # assert that the request contains a success message and a 201 status code
        # self.assertEqual(result['Message'], "You registered successfully.")
        # self.assertEqual(res.status_code, 201)
        

    # def tearDown(self):


    def test_add_new_menu(self):
        res = self.client().post('/api/v2/menu',content_type='application/json',
            data=json.dumps(self.menu),headers=self.auth_header)
        self.assertEqual(res.status_code,201)


        

      
        
    
    # def  test_add_menu_items(self):
    #     """Test API can add a new menu item """
    #     res = self.client().post(
    #     '/api/v2/orders/', 
    #     content_type='application/json',
    #     data=json.dumps(
    #         {
    #         "item_name":"Chapatis",
    #         "price":50000,
    #         "current_items":40
    #       }
    #      )
    #     )
        
    #     self.assertEqual(res.status_code, 201)
        

             
    # def test_order_creation(self):

    #     """Test API  can create an order (POST request)"""

    #     res = self.client().post(
    #         '/api/v2/orders/', 
    #         content_type='application/json',
    #         data=json.dumps(
    #             {
    #               "user_id":2,
    #               "item_id":6,
    #               "quantity":23 
    #           }
    #         )
    #     )
        
    #     self.assertEqual(res.status_code, 201)
        

