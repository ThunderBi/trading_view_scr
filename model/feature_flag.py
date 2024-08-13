from model.common import *
import logging


logging.basicConfig(filename='logs/db_holiday.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_feature_flag():
    query = 'SELECT * FROM feature_flag'
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    except pyodbc.Error as e:
        logging.error(f"Error retrieving holiday data: {e}")
        return []