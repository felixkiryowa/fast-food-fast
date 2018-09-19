"""
This module defines api views

"""
from flask import json
from flask import jsonify
from flask import request
from flask import Response
from flask.views import MethodView
from .orders import Orders


class ManageOrders(MethodView):
    """Class to define all the api end points"""
    order1 = Orders(
        1, [{"item_id":1, "item_name":"pizza", "price":40000, "quantity":1}],
        "none", 23
    )
    order2 = Orders(
        2, [{"item_id":1, "item_name":"fresh juice", "price":20000, "quantity":2}],
        "none", 45
    )
    order3 = Orders(
        3, [{"item_id":1, "item_name":"fried fish", "price":30000, "quantity":3}],
        "none", 12
    )
    orders = [order1, order2, order3]

    def post(self):
        """funtion to place a new order"""
        posted_data = request.get_json()
        if('order_items' in posted_data and 'user_id' in posted_data):
            order = Orders(
                len(self.orders) + 1, request.json['order_items'],
                None, request.json['user_id']
            )
            self.orders.append(order)
            response = Response(json.dumps(order.__dict__), 201, mimetype="application/json")
            response.headers['location'] = "/api/v1/orders/" + str(order.__dict__['order_id'])
            return response
            # jsonify(order.__dict__)
        else:
            order_object = "{'order_items':[{'item_id': 7,item_name': 'pop corns','price':30000,'quantity': 6}],'user_id': 23}"
            bad_order_object = {
            "error": "Bad Order Object",
            "help of the correct order object format":order_object
            }
            response = Response(json.dumps(bad_order_object), status=400, mimetype="appliation/json")
            return response
    def get(self, order_id):
        """function to get a single order or to get all the orders"""
        if order_id is None:
            # return a list of orders
            return jsonify({'all orders':[order.__dict__ for order in self.orders]})
        else:
            return manage_order.validate_get_specific_order(order_id)
    def put(self, order_id):
        """function to update a specific  order"""
        # update a specific order
        if isinstance(order_id, int):
            return manage_order.refactor_put_specific_order(order_id)
        else:
            raise TypeError(
                'The route parameter to update a specific \
                order status cannot be a String'
            )
    def validate_get_specific_order(self, id):
        """
        function to validate get order id
        """
        message = {'Message':'No Order Found with Specified Route Parameter Id'}
        response = Response(json.dumps(message), status=404, mimetype="appliation/json")
        if isinstance(id, int):
            if not isinstance(id, bool):
                if not id < 0:  
                    for order in self.orders:
                        if order.__dict__['order_id'] == id:
                            return jsonify({'order':order.__dict__}) 
                    return response        
                else:
                    raise ValueError('The route parameter can not be a number less than zero')
            else:
                raise TypeError('The route parameter cannot be a boolean')
        else:
            raise TypeError('The route parameter cannot be a String')
    
    def refactor_put_specific_order(self , id):
        message = {'Message':'No Order Found with Specified Route Parameter Id'}
        response = Response(json.dumps(message), status=404, mimetype="appliation/json")
        """
        function to validate update order Id
        """
        if not isinstance(id, bool):
            if not id < 0:
                get_spefic_order = [
                    order.__dict__ for order in self.orders
                    if order.__dict__["order_id"] == id
                ]
                if not get_spefic_order:
                    return response
                for order in self.orders:
                    if order.__dict__["order_id"] == id:
                        order_json = request.get_json()
                        order.__dict__['order_status'] = order_json['order_status']
                return jsonify({'orders':[order.__dict__ for order in self.orders]})
            else:
                raise ValueError(
                    'The route parameter to update a specific\
                    order status cannot be an interger less than a zero'
                )
        else:
            raise TypeError(
                'The route parameter to update a specific\
                order status cannot be a boolean'
            )

manage_order = ManageOrders()