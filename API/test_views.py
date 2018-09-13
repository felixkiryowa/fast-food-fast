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


