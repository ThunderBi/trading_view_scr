from model.common import *
import logging


logging.basicConfig(filename='logs/db_holiday.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_holidays():
    query = 'SELECT * FROM LiburBursa'
    try:
        conn = pyodbc.connect(conn_str)
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    except pyodbc.Error as e:
        logging.error(f"Error retrieving holiday data: {e}")
        return []

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

        if 'conn' in locals() and conn is not None:
            conn.close()