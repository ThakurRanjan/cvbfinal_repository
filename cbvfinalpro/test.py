import request
base_url = 'http://127.0.0.1:8000/'
endpoint_url = 'api/berr'
final_url = base_url + endpoint_url

pdata =  {
        "id": 3,
        "name": "Elephant",
        "teste": "Good",
        "color": "Green",
        "price": 300
    }

resp = request.get('http://127.0.0.1:8000/')