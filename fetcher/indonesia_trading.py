import requests
import json
from fetcher.common import *
from fetcher.request import *
from model.indonesia_trading import *
import logging

logging.basicConfig(filename='logs/trading_view_indonesia.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def process_and_save_data(response_data, db_batch_size):
    entire_world = get_mapping(columns, mapper_indonesia_trading, request_indonesia_trading["columns"],
                               response_data['data'])
    for j in range(0, len(entire_world), db_batch_size):
        db_batch = entire_world[j:j + db_batch_size]
        save_entire_world_data(db_batch)


def call_trading_view_indonesia_trading():
    db_batch_size = 50

    logging.info("Start indonesia_trading ")
    json_data = json.dumps(request_indonesia_trading)
    start_time = datetime.now()

    try:
        response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
        response.raise_for_status()

        runtime = datetime.now() - start_time
        logging.info("Running indonesia_trading Done Call Trading view on {} seconds".format(runtime))

        response_data = response.json()

        process_and_save_data(response_data, db_batch_size)
        call_sp_calculate()

        runtime = datetime.now() - start_time
        logging.info("Running indonesia_trading Done Call Trading view on {} seconds".format(runtime))
    except requests.exceptions.RequestException as e:
        error_message = f"Error with: {response.status_code} - {str(e)}"
        logging.error(error_message)
    except Exception as e:
        logging.exception("Something awful happened!")
        logging.error(f"An unexpected error indonesia_trading occurred in batch : {e}")
