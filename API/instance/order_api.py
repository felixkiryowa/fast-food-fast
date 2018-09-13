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

    def get(self):
        """function to get a single order or to get all the orders"""
        return jsonify({'all orders':[order.__dict__ for order in self.orders]})
       

   