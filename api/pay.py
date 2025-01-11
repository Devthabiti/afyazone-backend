import requests

# URL of the API endpoint
url = "https://api.zeno.africa"

# Data to send for creating the order
order_data = {
    'create_order': 1,
    'buyer_email': 'a@gmail.com',
    'buyer_name': 'zuku',
    'buyer_phone': '0659242027',
    'amount': 1000,
    'account_id': 'zp44340',
    'api_key': 'ded13c0d740c577f9c44a3f8e2759ea3',
    'secret_key': 'b897d25736d5e2a1947aebc9a6a0bb87cf66a60904fabdd81a20a323cff4b723'
}

try:
    # Send POST request to create the order
    response = requests.post(url, data=order_data)
    
    # Print the response
    print(response.text)

except requests.RequestException as e:
    # Log errors to a file
     print(e)