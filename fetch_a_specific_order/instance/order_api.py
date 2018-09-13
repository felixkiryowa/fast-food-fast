"""
This module defines api views

"""
from flask import jsonify
from flask import request
from flask.views import MethodView
from orders import Orders


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

    def get(self, order_id):
        """function to get a single order or to get all the orders"""
        if order_id is None:
            # return a list of orders
            return jsonify({'all orders':[order.__dict__ for order in self.orders]})
        if isinstance(order_id, int):
            if not order_id < 0:
                if not isinstance(order_id, bool):
                    specific_order = [
                        order.__dict__ for order in self.orders
                        if order.__dict__["order_id"] == order_id
                    ]
                    if not specific_order:
                        return jsonify({'Message':'No Order Found with Specified Route Parameter'})
                        # raise ValueError('No Order Found with Specified Route Parameter')
                    return jsonify({'order':specific_order[0]})
                else:
                    raise TypeError('The route parameter cannot be a boolean')
            else:
                raise ValueError('The route parameter can not be a number less than zero')
        else:
            raise TypeError('The route parameter cannot be a String')

    
       

   