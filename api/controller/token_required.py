import jwt
import psycopg2
from flask import request
from flask import jsonify
from functools import wraps 
from database.config import config
from connection import secret_key

def token_required(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}),401
        try:
            data = jwt.decode(token, secret_key)
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=%s",(data['username'], ))
            current_user = cur.fetchall()
        except:
            return jsonify({'message':'Token is invalid!'}),401
        return f(self, current_user, *args, **kwargs)
    return decorated