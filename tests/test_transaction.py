from app.app import app

test_client = app.test_client

test_user = {
    "username": "test",
    "password": "test"
}
test_client.post("/signup", json=test_user)
access_token = test_client.post("/auth", json=test_user).json()["access-token"]

def test_process_payment():

    json_array = [{
        "amount": 550.5
    },
    {
        "amount": 150.0
    },
    {
        "amount": 15
    }]
    
    for json in json_array:
        response = test_client.post("/transaction", headers={"Authorization": "Bearer {0}".format(access_token)}, json=json)
        assert response.status_code == 200
        assert response.json() is not None
        assert response.json()["message"] == "Paymenty is processed"

    response = test_client.post("/transaction", headers={"Authorization": "Bearer "}, json={"amount": 100})
    assert response.status_code == 400
    assert response.json() is not None
    assert response.json()["message"] == "The request is Invalid"

    response = test_client.post("/transaction", headers={"Authorization": "Bearer {0}".format(access_token)}, json={"amount": -10})
    assert response.status_code == 400
    assert response.json() is not None
    assert response.json()["message"] == "The request is Invalid"
    
    print("Valid casesTimeline query test passed!")
