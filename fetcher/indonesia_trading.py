import requests
import json
from fetcher.common import *
from fetcher.request import *
from model.indonesia_trading import *


def call_trading_view_indonesia_trading():
    json_data = json.dumps(request_indonesia_trading)

    # Send a POST request to the API with the JSON data
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    response_data = response.json()

    mapping = get_mapping(columns, mapper_indonesia_trading, request_indonesia_trading["columns"], response_data['data'])
    save_entire_world_data(mapping)





