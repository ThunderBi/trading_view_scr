import requests
import json
import time
from fetcher.common import *
from fetcher.request import *
from model.entire_world import *
import logging

logging.basicConfig(filename='trading_view_errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def call_trading_view():
    batch_size = 1000
    total_batches = 2

    for i in range(total_batches):
        logging.info("Running batch {}".format(i))
        start = i * batch_size
        end = start + batch_size

        request_entire_world["range"] = [start, end]

        json_data = json.dumps(request_entire_world)
        try:
            response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
            response.raise_for_status()

            response_data = response.json()

            entire_world = get_mapping(columns, mapper_entire_world, request_entire_world["columns"],
                                       response_data['data'])
            save_entire_world_data(entire_world)
        except requests.exceptions.RequestException as e:
            error_message = f"Error with batch {i + 1}: {response.status_code} - {str(e)}"
            logging.error(error_message)
        except Exception as e:
            logging.error(f"An unexpected error occurred in batch {i + 1}: {str(e)}")

