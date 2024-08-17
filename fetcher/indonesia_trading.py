import requests
import csv
import os
import json
import logging
from datetime import datetime
from fetcher.common import *
from fetcher.request import *
from model.indonesia_trading import *
from fetcher.base_fetcher import *

logging.basicConfig(filename='logs/trading_view_indonesia.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_batch_info(batch_index, action, runtime):
    logging.info(f"Running batch {batch_index} {action} on {runtime} seconds")

def call_tv_indonesia():
    batch_size = 1000
    db_batch_size = 1000
    total_batches = 1

    delete_today()
    for i in range(total_batches):
        start_time = datetime.now()
        logging.info(f"Running batch {i}")
        start, end = i * batch_size, (i + 1) * batch_size

        try:
            response_data = fetch_trading_view_data(request_indonesia_trading, start, end)
            log_batch_info(i, "Indonesia Screener Done Call Trading View", (datetime.now() - start_time).total_seconds())

            process_and_save_data(request_indonesia_trading, response_data,
                                  columns, mapper_indonesia_trading, db_batch_size, safe_bulk)

            log_batch_info(i, "Indonesia Screener Done Call Save DB", (datetime.now() - start_time).total_seconds())
        except requests.exceptions.RequestException as e:
            error_message = f"Indonesia Screener Error with batch {i + 1}: {str(e)}"
            logging.error(error_message)
        except Exception as e:
            logging.exception("Indonesia Screener Something awful happened!")
            logging.error(f"Indonesia Screener An unexpected error occurred in batch {i + 1}: {str(e)}")

# def call_trading_view_indonesia_trading():
#     batch_size = 1500
#     db_batch_size = 1500
#     total_batches = 1
#
#     delete_today()
#     for i in range(total_batches):
#         start_time = datetime.now()
#         logging.info(f"Running batch {i}")
#         start, end = i * batch_size, (i + 1) * batch_size
#
#         try:
#             response_data = fetch_trading_view_data(start, end)
#
#             fetch_runtime = (datetime.now() - start_time).total_seconds()
#             log_batch_info(i, "Done Call Trading View", fetch_runtime)
#
#             process_and_save_data(response_data, db_batch_size)
#
#             save_runtime = (datetime.now() - start_time).total_seconds()
#             log_batch_info(i, "Done Call Save DB", save_runtime)
#
#         except requests.exceptions.RequestException as e:
#             error_message = f"Error with batch {i + 1}: {str(e)}"
#             logging.error(error_message)
#         except Exception as e:
#             logging.exception("Something awful happened!")
#             logging.error(f"An unexpected error occurred in batch {i + 1}: {str(e)}")
