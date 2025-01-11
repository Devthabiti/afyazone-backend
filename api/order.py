import requests
import json

# URL of the API endpoint
url = "https://api.zeno.africa/order-status"

def check_order_status(order_id):
    # Data to send for checking the order status
    status_data = {
        'check_status': 1,
        'order_id': order_id,
        'api_key': 'ded13c0d740c577f9c44a3f8e2759ea3',
        'secret_key': 'b897d25736d5e2a1947aebc9a6a0bb87cf66a60904fabdd81a20a323cff4b723'
    }

    try:
        # Send POST request to check the order status
        response = requests.post(url, data=status_data)
        # response.raise_for_status() 
        print(response.text)
        print(response.status_code) # Raise an exception for HTTP errors
        return response.json()  # Return the response as JSON
    except requests.RequestException as e:
        # log_error(f"Error fetching order status: {e}")
        return {
            'success': False,
            'message': 'Error fetching order status'
        }

# def log_error(message):
#     # Function to log errors
#     with open('error_log.txt', 'a') as log_file:
#         log_file.write(f"{message}\n")

# def show_response(response):
#     # Function to display the response
#     print(json.dumps(response, indent=2))

# Order ID to check
order_id = '66c5c6e4eb798'

# Get the order status
# response = check_order_status(order_id)

# # Show the response
# show_response(response)
check_order_status(order_id)