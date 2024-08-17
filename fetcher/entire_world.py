from fetcher.request import *
from model.entire_world import *
from fetcher.base_fetcher import *

# Setup logging
logging.basicConfig(filename='logs/trading_view_world.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_batch_info(batch_index, action, runtime):
    logging.info(f"Running batch {batch_index} {action} on {runtime} seconds")


def call_tv_world():
    batch_size = 10000
    db_batch_size = 1000
    total_batches = 6
    start_time = datetime.now()

    for i in range(total_batches):
        logging.info(f"Running batch {i}")
        start, end = i * batch_size, (i + 1) * batch_size

        try:
            response_data = fetch_trading_view_data(request_entire_world, start, end)
            log_batch_info(i, "World Done Call Trading View",
                           (datetime.now() - start_time).total_seconds())

            process_and_save_data(request_entire_world, response_data,
                                  columns, mapper_entire_world, db_batch_size, safe_bulk)

            log_batch_info(i, "World Screener Done Call Save DB", (datetime.now() - start_time).total_seconds())
        except requests.exceptions.RequestException as e:
            error_message = f"World Screener Error with batch {i + 1}: {str(e)}"
            logging.error(error_message)
        except Exception as e:
            logging.exception("World Screener Something awful happened!")
            logging.error(f"World Screener An unexpected error occurred in batch {i + 1}: {str(e)}")

    logging.info(f"world screener total {(datetime.now() - start_time).total_seconds()} seconds")
