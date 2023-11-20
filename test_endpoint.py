import pytest
import requests as re
import uuid
import json

url = "https://reqres.in/"
def test_can_call_endpoint():
    url_response=re.get(url)
    assert url_response.status_code == 200
"********************************************************************************************************************"
def test_fetch_users_list():
    resource_list = {
        "page": 2,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {
                "id": 7,
                "email": "michael.lawson@reqres.in",
                "first_name": "Michael",
                "last_name": "Lawson",
                "avatar": "https://reqres.in/img/faces/7-image.jpg"
            },
            {
                "id": 8,
                "email": "lindsay.ferguson@reqres.in",
                "first_name": "Lindsay",
                "last_name": "Ferguson",
                "avatar": "https://reqres.in/img/faces/8-image.jpg"
            },
            {
                "id": 9,
                "email": "tobias.funke@reqres.in",
                "first_name": "Tobias",
                "last_name": "Funke",
                "avatar": "https://reqres.in/img/faces/9-image.jpg"
            },
            {
                "id": 10,
                "email": "byron.fields@reqres.in",
                "first_name": "Byron",
                "last_name": "Fields",
                "avatar": "https://reqres.in/img/faces/10-image.jpg"
            },
            {
                "id": 11,
                "email": "george.edwards@reqres.in",
                "first_name": "George",
                "last_name": "Edwards",
                "avatar": "https://reqres.in/img/faces/11-image.jpg"
            },
            {
                "id": 12,
                "email": "rachel.howell@reqres.in",
                "first_name": "Rachel",
                "last_name": "Howell",
                "avatar": "https://reqres.in/img/faces/12-image.jpg"
            }
        ],
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    header = {
        "content-type": 'application/json'
    }
    params = {
        "page": 3,
        "per_page": 2
    }
    response = re.get(url=url + "api/users", params=params, headers=header)
    assert response.status_code == 200
    assert response.json() == resource_list

"********************************************************************************************************************"
def test_fetch_single_user():
    params = {
        "id": 2
    }
    payload={
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
    response = re.get(url=url + "api/users/",params=params)
    assert response.status_code == 200
    #users=json.dumps(response.json(),indent=4)
    users = response.json()
    #user_id= [x['id'] for x in users['data']]
    assert users['data']['id'] == payload['data']['id']
    assert users['data']['first_name'] == "Jude"

def test_fetch_single_user_not_found():
    params = {
        "id": 23
    }
    response = re.get(url=url + "api/users/",params=params)
    assert response.status_code == 404
    #print(json.dumps(response.json(), indent=4))


def test_create_user():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    updated_user_response = re.post(url=url + "api/users", json=user_data)
    assert updated_user_response.status_code == 201
    #print(json.dumps(updated_user_response.json(), indent=4))


def test_create_user():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    created_user_data={
    "name": "morpheus",
    "job": "leader",
    "id": "603",
    "createdAt": "2023-11-19T21:41:57.144Z"
}
    updated_user_response = re.post(url=url + "api/users", json=user_data)
    assert updated_user_response.status_code == 201
    updated_user=updated_user_response.json()
    assert  updated_user["job"] == "Joker"
    #print(json.dumps(updated_user_response.json(), indent=4))

def test_delete_user_id():
    params = {
        "id": 2
    }

    delete_user_response = re.delete(url=url + "api/users/", params=params)
    assert delete_user_response.status_code == 204
    # print(json.dumps(delete_user_response.json(),indent=4))


"********************************************************************************************************************"


# Testing for successful and Unsuccessful Registration
def test_register():
    params = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    register_succ_response = re.post(url=url + "api/register", json=params)
    assert register_succ_response.status_code == 200
    assert register_succ_response.json() == {
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }
    # print(json.dumps(register_succ_response.json(),indent=4))


def test_register_fail():
    params = {
        "email": "sydney@fife"
    }

    failed_register_response = re.post(url=url + "api/register", json=params)
    assert failed_register_response.status_code == 400
    assert failed_register_response.json() == {
        "error": "Missing password"
    }
    #print(json.dumps(failed_register_response.json(), indent=4))
    #print('Unsuccessful Registration!!')


# Testing for successful and Unsuccessful Login
def test_successful_login():
    registered_user = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    login_succ_response = re.post(url=url + "api/login", json=registered_user)
    assert login_succ_response.status_code == 200
    assert login_succ_response.json() == {
        "token": "QpwL5tke4Pnpja7X4"
    }
    # print(json.dumps(login_succ_response.json(),indent=4))


def test_login_fail():
    params = {
        "email": "peter@klaven"
    }

    failed_login_response = re.post(url=url + "api/login", json=params)
    assert failed_login_response.status_code == 400
    assert failed_login_response.json() == {
        "error": "Missing password"
    }
    # print(json.dumps(failed_login_response.json(),indent=4))

"********************************************************************************************************************"
''' Delayed Response'''

def test_delayed_response():
    params = {
        "page": 2
    }

    delayed_response = re.get(url=url + "api/users", params=params)
    assert delayed_response.status_code == 200


"********************************************************************************************************************"
