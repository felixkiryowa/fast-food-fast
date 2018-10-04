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
from api.models.users import Users
from flask import current_app
# from api.validator.validate import  submit_empty_string
from api.validator.validate  import Validate
from flask import Response



class AuthorizeUsers(MethodView):
    """Class to define all the api end points"""
    
    def  post(self):
        
        rule = request.url_rule
        could_not_verify = {
            "Message":"Could not verify!"
        }
        if 'signup' in rule.rule:
            new_user_data = request.get_json()
            if('name' in new_user_data and  'username' in new_user_data 
                and 'password' in new_user_data and
                'address' in new_user_data and 'phone_number' in new_user_data and 'user_type' in new_user_data ):
                manage_users.validate_sign_up(
                   new_user_data,
                   new_user_data['name'],new_user_data['username'],new_user_data['password'],
                   new_user_data['address'],new_user_data['phone_number'],new_user_data['user_type']
                )
                
                hashed_password = generate_password_hash(new_user_data['password'], method='sha256')

                """ insert a new user into the users table """

                sql = """INSERT INTO users(name,username,password,address,phone_number,user_type)
                        VALUES(%s,%s,%s,%s,%s,%s) RETURNING user_id;"""
                return manage_users.execute_add_user_query(sql,
                    new_user_data['name'],new_user_data['username'],hashed_password, 
                    new_user_data['address'],new_user_data['phone_number'],new_user_data['user_type']
                )

            user_auth_object = "{'name':'francis kiryowa',username': 'kiryowa22','password': 'user123','address':'Makerere','phone_number':0789906754,'user_type':'admin/user'}"
            bad_sigining_object = {
            "error": "Bad Order Object",
            "help of the correct auth object format":user_auth_object
            }
            response = Response(
                json.dumps(bad_sigining_object),
                status=400, mimetype="appliation/json"
                )
            return response
        #execute this block of code if its a login route
        user_object = request.get_json()

        if('username' in user_object and 'password' in user_object):
            return manage_users.validate_u_and_p(user_object,user_object['username'],user_object['password'])
            return manage_users.execute_user_login_auth(user_object['username'], user_object['password'], could_not_verify)
        else:
            user_auth_object = "{'username': 'kiryowa22','password': 'user123'}"
            bad_auth_object = {
            "error": "Bad Order Object",
            "help of the correct auth object format":user_auth_object
            }
            response = Response(
                json.dumps(bad_auth_object),
                status=400, mimetype="appliation/json"
                )
            return response
            # return jsonify({"Message" : "Username and Password Required"}),401
            
    def validate_u_and_p(self,user_object, username,password):
        if user_object['username'] == None  or  user_object['password'] == None:
            return jsonify({"Message" : "Username and Password  can not be empty!"}),401
        if not isinstance(user_object['username'],str) or not isinstance(user_object['password'],str):
            return jsonify({"Message" : "Username and Password  can not be an Interger/Boolean other than a string"}),401
        if isinstance(user_object['username'],int)  or isinstance(user_object['username'],int):
            return jsonify({"Message" : "Username and Password  can not be an integer!"}),401

    def validate_sign_up(self,signing_object,name, username, password, address, phone_number,user_type):
        if (signing_object['name'] == None  or signing_object['username'] == None or
            signing_object['password'] == None or signing_object['address'] == None or
            signing_object['phone_number'] == None or signing_object['user_type'] == None) :
            return jsonify({"Message" : "One or More of required But  Not Provided"}),400
        # if not isinstance(user_object['username'],str) or not isinstance(user_object['password'],str):
        #     return jsonify({"Message" : "Username and Password  can not be an Interger/Boolean other than a string"}),401
        # if isinstance(user_object['username'],int)  or isinstance(user_object['username'],int):
        #     return jsonify({"Message" : "Username and Password  can not be an integer!"}),401

                         
        
    def execute_user_login_auth(self, username, password,error_message):

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=%s",(username, ))
            specific_user = cur.fetchall()
            user_exist = cur.rowcount
            if user_exist == 0:
                return jsonify({"Message":error_message}),401
            user_password = specific_user[0][3]
            if check_password_hash(user_password, password):
                user_username = specific_user[0][2]
                token = jwt.encode({'username':user_username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},current_app.config['SECRET_KEY'])
                cur.close()
                # return jsonify({'token_generated':token.decode('UTF-8')}) 
                return jsonify({'token_generated':token.decode('UTF-8')}),200
            return jsonify({"Message":error_message}),401
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    
    def execute_add_user_query(self,sql,name,username,password,address,phone_number,user_type):
        conn = None
        # user_id = None
        try:
            
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (name, username, password, address, phone_number,user_type, ))
            # commit the changes to the database
            conn.commit()
            return jsonify({'Message':'You registered successfully.'}),201
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        

manage_users = AuthorizeUsers()