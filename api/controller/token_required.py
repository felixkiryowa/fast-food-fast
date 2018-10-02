import jwt
import psycopg2
from flask import request
from flask import jsonify
from functools import wraps 
from api.database.config import config
from flask import current_app

def token_required(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}),401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username=%s",(data['username'], ))
            current_user = cur.fetchall()
        except:
            return jsonify({'message':'Token is invalid!'}),401
        return f(self, current_user, *args, **kwargs)
    return decorated