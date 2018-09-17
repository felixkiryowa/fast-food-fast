"""
This module defines api views

"""
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
            response = Response("", 201, mimetype="application/json")
            response.headers['Location'] = "/api/v1/orders/" + str(order.__dict__['order_id'])
            return jsonify(order.__dict__)
        else:

            bad_object = {
            "error": "Invalid book object",
            "help_string":
                "Request format should be {'order_items': 'Tha cat in the hat',"
                "'price': '7.99','isbn': 12319881212 }"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="appliation/json")
            return response

    def get(self, order_id):
        """function to get a single order or to get all the orders"""
        if order_id is None:
            # return a list of orders
            return jsonify({'all orders':[order.__dict__ for order in self.orders]})
        if isinstance(order_id, int):
            if not isinstance(order_id, bool):
                if not order_id < 0:  
                    for order in self.orders:
                        if order.__dict__['order_id'] == order_id:
                            return jsonify({'order':order.__dict__}) 
                        return jsonify({'Message':'No Order Found with Specified Route Parameter'})         
                else:
                    raise ValueError('The route parameter can not be a number less than zero')
            else:
                raise TypeError('The route parameter cannot be a boolean')
        else:
            raise TypeError('The route parameter cannot be a String')
    def put(self, order_id):
        """function to update a specific  order"""
        # update a specific order
        if isinstance(order_id, int):
            if not isinstance(order_id, bool):
                if not order_id < 0:
                    get_spefic_order = [
                        order.__dict__ for order in self.orders
                        if order.__dict__["order_id"] == order_id
                    ]
                    if not get_spefic_order:
                        return jsonify({'Message':'No Order Found with Specified Route Parameter'})
                    for order in self.orders:
                        if order.__dict__["order_id"] == order_id:
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
        else:
            raise TypeError(
                'The route parameter to update a specific \
                order status cannot be a String'
            )
    