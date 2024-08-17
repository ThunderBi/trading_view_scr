from datetime import datetime
import csv
import os
import logging
import json
import requests
from fetcher.common import *

def log_batch_info(batch_index, action, runtime):
    logging.info(f"Running batch {batch_index} {action} on {runtime} seconds")


def fetch_trading_view_data(request, start, end):
    request["range"] = [start, end]
    json_data = json.dumps(request)
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    response.raise_for_status()
    return response.json()


def to_csv(data):
    filename = f'data-{datetime.now().timestamp()}.csv'
    headers = data[0].keys()

    # Write the data to the CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write the rows

    return os.path.abspath(filename)


def process_and_save_data(request, response_data, columns, mapper, db_batch_size, safe_bulk):
    mapping = get_mapping(columns, mapper, request["columns"],
                               response_data['data'])
    # to_csv(mapping)
    # print(indonesia_trading)
    # save_csv(to_csv(indonesia_trading))
    for j in range(0, len(mapping), db_batch_size):
        logging.info(f'db {j}')
        db_batch = mapping[j:j + db_batch_size]
        safe_bulk(db_batch)


