class Validate(object):

    def validate_u_and_p(username,password):
        if user_object['username'] == None  or  user_object['password'] == None:
            return jsonify({"Message" : "Username and Password  can not be empty!"}),401
        if not isinstance(user_object['username'],str) or not isinstance(user_object['password'],str):
            return jsonify({"Message" : "Username and Password  can not be an Interger/Boolean or \
                any other data type"}),401
        if isinstance(user_object['username'],int)  or isinstance(user_object['username'],int):
            return jsonify({"Message" : "Username and Password  can not be an integer!"}),401