from app.app import app

test_client = app.test_client

test_user = {
    "username": "test",
    "password": "test"
}
test_client.post("/signup", json=test_user)
access_token = test_client.post("/auth", json=test_user).json()["access-token"]

def test_user():

    signup_res = test_client.post("/signup", json=test_user)
    assert signup_res.status_code == 201
    assert signup_res.json() is not None
    assert signup_res.json()["message"] == "User test created!"

    signup_res = test_client.post("/signup", json=test_user)
    assert signup_res.status_code == 400
    assert signup_res.json() is not None
    assert signup_res.json()["message"] == "User test already exists, please choose another username!"

    login_res = test_client.post("/auth", json=test_user)
    assert login_res.status_code == 200
    assert login_res.json() is not None
    assert login_res.json()["access-token"] != ""
    
    print("Valid casesTimeline query test passed!")
