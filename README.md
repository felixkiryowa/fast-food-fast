#TRAVIS 

[![Build Status](https://travis-ci.org/felixkiryowa/fast-food-fast.svg?branch=develop)](https://travis-ci.org/felixkiryowa/fast-food-fast)

#COVERALLS

[![Coverage Status](https://coveralls.io/repos/github/felixkiryowa/fast-food-fast/badge.svg?branch=develop)](https://coveralls.io/github/felixkiryowa/fast-food-fast?branch=develop)

#CODE CLIMATE

[![Maintainability](https://api.codeclimate.com/v1/badges/69009c49be9bd4b59267/maintainability)](https://codeclimate.com/github/felixkiryowa/fast-food-fast/maintainability)

Name of project  : Fast-Food-Fast API endpoints

Project Overview
Fast-Food-Fast API is a project thats to be consumed by fast-food-fast website users ,that is the customers and the administrators.The customers will be able to post their orders at any point in time ,while thhe administrator will be able to change the order status of an order,view all orders,get one order incase they want to review it in details.The API has been entirely developed using python-flask framework and tested using Postman

How does one go about using it live or within their own project?

End point to get all orders
URL
https://fsfapi.herokuapp.com/api/v1/orders
METHOD
GET
SUCCESS RESPONSE:
Code: 200 OK
Content:
{
    "all orders": [
        {
            "order_id": 1,
            "order_items": [
                {
                    "item_id": 4,
                    "item_name": "Juice",
                    "price": 4000,
                    "quantity": 1
                }
            ],
            "order_status": null,
            "user_id": 23
        },
        {
            "order_id": 2,
            "order_items": [
                {
                    "item_id": 4,
                    "item_name": "chicken",
                    "price": 4000,
                    "quantity": 1
                }
            ],
            "order_status": null,
            "user_id": 23
        }
    ]
}
Error Response:
Code: 404 NOT FOUND


End point to get a specific order
URL
https://fsfapi.herokuapp.com/api/v1/orders/1
METHOD
GET
SUCCESS RESPONSE:
Code: 200 OK
Content:
{
    "order": {
        "order_id": 1,
        "order_items": [
            {
                "item_id": 4,
                "item_name": "Juice",
                "price": 4000,
                "quantity": 1
            }
        ],
        "order_status": null,
        "user_id": 23
    }
}
Error Response:
Code: 404 NOT FOUND
Content:
{
    "Message": "No Order Found with Specified Order Id"
}


End point to update a specific order status
URL
https://fsfapi.herokuapp.com/api/v1/orders/1
METHOD
PUT
SUCCESS RESPONSE:
Code: 200 OK
Content:
{
    "order": {
        "order_id": 1,
        "order_items": [
            {
                "item_id": 4,
                "item_name": "Juice",
                "price": 4000,
                "quantity": 1
            }
        ],
        "order_status":"Accepted",
        "user_id": 23
    }
}
Error Response:
Code: 404 NOT FOUND
Content:
{
    "Message": "No Order Found with Specified Order Id"
}


End point to Post  a given order by the user

URL
https://fsfapi.herokuapp.com/api/v1/orders/1
METHOD
POST
SUCCESS RESPONSE:
Code: 201 CREATED
Content:
{
    "order_id": 2,
    "order_items": [
        {
            "item_id": 4,
            "item_name": "chicken",
            "price": 4000,
            "quantity": 1
        }
    ],
    "order_status": null,
    "user_id": 23
}
Error Response:
Code: 404 NOT FOUND
Content:


