import requests
import json
import logging
from datetime import datetime
from fetcher.common import *
from fetcher.request import *
from model.entire_world import *

# Setup logging
logging.basicConfig(filename='logs/trading_view_world.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_batch_info(batch_index, action, runtime):
    logging.info(f"Running batch {batch_index} {action} on {runtime} seconds")


def fetch_trading_view_data(start, end):
    request_entire_world["range"] = [start, end]
    json_data = json.dumps(request_entire_world)
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
    response.raise_for_status()
    return response.json()


def process_and_save_data(response_data, db_batch_size):
    entire_world = get_mapping(columns, mapper_entire_world, request_entire_world["columns"],
                               response_data['data'])
    for j in range(0, len(entire_world), db_batch_size):
        db_batch = entire_world[j:j + db_batch_size]
        save_entire_world_data(db_batch)


def call_trading_view():
    batch_size = 10000
    db_batch_size = 50
    total_batches = 6

    for i in range(total_batches):
        start_time = datetime.now()
        logging.info(f"Running batch {i}")
        start, end = i * batch_size, (i + 1) * batch_size

        try:
            response_data = fetch_trading_view_data(start, end)

            fetch_runtime = (datetime.now() - start_time).total_seconds()
            log_batch_info(i, "Done Call Trading View", fetch_runtime)

            process_and_save_data(response_data, db_batch_size)

            save_runtime = (datetime.now() - start_time).total_seconds()
            log_batch_info(i, "Done Call Save DB", save_runtime)

        except requests.exceptions.RequestException as e:
            error_message = f"Error with batch {i + 1}: {str(e)}"
            logging.error(error_message)
        except Exception as e:
            logging.exception("Something awful happened!")
            logging.error(f"An unexpected error occurred in batch {i + 1}: {str(e)}")
