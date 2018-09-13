import pytest
from instance.order_api import ManageOrders
from flask import json
from run import APP

app = APP
client = app.test_client
order = ManageOrders()

def test_get_all_orders():
    result = client().get('/api/v1/order/')
    assert result.status_code == 200

def test_if_parameter_passed_to_function_is_a_string():
    with pytest.raises(TypeError):
        order.get("five")

def test_if_parameter_passed_is_a_number_less_than_a_zero():
    with pytest.raises(ValueError):
        order.get(-1)
def test_if_parameter_passed_is_a_boolean():
    with pytest.raises(TypeError):
        order.get(True)
def test_if_data_posted_is_in_form_of_json():
    result = client().post('/api/v1/order/add', content_type='application/json',
    data =  json.dumps({
	
        "order_items": [
            {
                "item_id": 8,
                "item_name": "Chips and Chicken",
                "price": 50000,
                "quantity": 3
            }
        ],
        "user_id": 13
    }) 
)

    assert result.status_code == 200

#Tests for updating the order status
def test_update_specific_order():
    result = client().put('/api/v1/order/2', content_type='application/json', 
    data = json.dumps({
       "order_status":"Accepted" 
    }))
    assert result.status_code == 200

def test_if_parameter_passed_to_the_put_function_is_a_string():
    with pytest.raises(TypeError):
        order.put("ten")

def test_if_parameter_passed_to_the_put_function_is_a_number_less_than_a_zero():
    with pytest.raises(ValueError):
        order.put(-1)
def test_if_parameter_passed_to_the_put_function_is_a_boolean():
    with pytest.raises(TypeError):
        order.put(True)






