import requests
import json

def get_request(link, param):
    return (requests.get(link, params=param)).json()



