import requests

def send_text(prompt, API_ENDPOINT):
    message = {"prompt": prompt}
    response = requests.post(API_ENDPOINT, json=message)
    return response