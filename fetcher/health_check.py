import requests
import logging


logging.basicConfig(
    filename='logs/health_check.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def health_check():
    url = "https://apikanban.bizmatic.id/monitoring/v1/ping/0CAD6DAB-4EAD-4A0E-AAAD-AF9582578946"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Log the status code and response text
        logging.info(f"Health Check: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")

