"""
This module contains test for the API end points
"""
import pytest
from flask import json
from instance.order_api import ManageOrders
from run import APP


APP = APP
CLIENT = APP.test_client
ORDER = ManageOrders()

def test_get_all_orders():
    """
    function to test get all orders API end point
    """
    result = CLIENT().get('/api/v1/order/')
    assert result.status_code == 200

def test_if_parameter_passed_to_function_is_a_string():
    """
    function to test get a specific  order API end point\
    such that a string is not passed as a route parameter
    """
    with pytest.raises(TypeError):
        ORDER.get("five")

def test_if_parameter_passed_is_a_number_less_than_a_zero():
    """
    function to test get a specific  order API end point\
    such that an integer less than Zero is not passed as a route parameter
    """
    with pytest.raises(ValueError):
        ORDER.get(-1)
def test_if_parameter_passed_is_a_boolean():
    """function to test get a specific  order API end point\
    such that a boolean is not passed as a route parameter
    """
    with pytest.raises(TypeError):
        ORDER.get(True)
def test_if_data_posted_is_in_form_of_json():
    """
    function to test if data posted to the place order API is in form of Json
    """
    result = CLIENT().post(
        '/api/v1/order/add', content_type='application/json',
        data=json.dumps(
            {
                "order_items": [
                    {
                        "item_id": 8,
                        "item_name": "Chips and Chicken",
                        "price": 50000,
                        "quantity": 3
                    }
                ],
                "user_id": 13
            }
        )
    )
    assert result.status_code == 200

#Tests for updating the order status
def test_update_specific_order():
    """function to test whether data passed to the update end point is \
    in form of a JSON format
    """
    result = CLIENT().put(
        '/api/v1/order/2', content_type='application/json',
        data=json.dumps(
            {
                "order_status":"Accepted"
            }
        )
    )
    assert result.status_code == 200

def test_if_parameter_passed_to_the_put_function_is_a_string():
    """
    function to test get a specific  order API end point\
    such that a string is not passed as a route parameter
    """
    with pytest.raises(TypeError):
        ORDER.put("ten")

def test_if_parameter_passed_to_the_put_function_is_a_number_less_than_a_zero():
    """
    function to test get a specific  order API end point\
    such that an integer less than Zero is not passed as a route parameter
    """
    with pytest.raises(ValueError):
        ORDER.put(-1)
def test_if_parameter_passed_to_the_put_function_is_a_boolean():
    """function to test get a specific  order API end point\
    such that a boolean is not passed as a route parameter
    """
    with pytest.raises(TypeError):
        ORDER.put(True)
        