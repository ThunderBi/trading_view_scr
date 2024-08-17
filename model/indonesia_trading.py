import pyodbc

from model.common import *
from datetime import datetime
import logging

logging.basicConfig(filename='logs/db_indonesia.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


table_name = 'indonesia_trading_screener'
columns = [
    'symbol', 
    'description',
    'open_price',
    'open_currency', 
    'low', 
    'low_currency', 
    'high', 
    'high_currency', 
    'price', 
    'price_currency', 
    'change_percentage', 
    'volume', 
    'average_volume_10d_calc', 
    'average_volume_30d_calc', 
    'volume_x_price_1d', 
    'volatility_1d', 
    'volatility_1w', 
    'volatility_1m', 
    'aroon_1d_up', 
    'aroon_1d_down', 
    'average_directional_index_1d', 
    'awesome_oscillator_1d', 
    'bollinger_bands_20_1d_upper',
    'bollinger_bands_20_1d_basis',
    'bollinger_bands_20_1d_lower', 
    'bull_bear_power_13_4h', 
    'bull_bear_power_13_1d', 
    'bull_bear_power_13_1w', 
    'bull_bear_power_13_1m', 
    'chaikin_money_flow_20_1d', 
    'chaikin_money_flow_20_1w', 
    'chaikin_money_flow_20_1M', 
    'commodity_channel_index_20_1d', 
    'commodity_channel_index_20_1w',
    'commodity_channel_index_20_1m', 
    'directional_movement_index_14_1d_positive', 
    'directional_movement_index_14_1d_negative', 
    'donchian_channels_20_1d_basis', 
    'donchian_channels_20_1d_lower', 
    'EMA12_1d', 
    'EMA26_1d', 
    'EMA50_1d',
    'EMA200_1d', 
    'ichimoku_base_line_1d', 
    'ichimoku_conversation_line_1d', 
    'ichimoku_leading_span_a_1d', 
    'ichimoku_leading_span_b_1d', 
    'momentum_1d', 
    'momentum_1w', 
    'momentum_1m', 
    'money_flow_14_1d', 
    'money_flow_14_1w', 
    'money_flow_14_1m',
    'macd_1d_level', 
    'macd_1d_signal', 
    'pivot_points_fibonacci_1d_r1', 
    'pivot_points_fibonacci_1d_s1', 
    'pivot_points_fibonacci_1d_r2', 
    'pivot_points_fibonacci_1d_s2', 
    'pivot_points_fibonacci_1d_r3', 
    'pivot_points_fibonacci_1d_s3', 
    'rate_of_change_9_1d', 
    'rate_of_change_9_1w', 
    'rate_of_change_9_1m', 
    'stochastic_rsi_k_1d', 
    'stochastic_rsi_d_1d', 
    'william_percentage_range_1d', 
    'william_percentage_range_1W', 
    'william_percentage_range_1M'
]

def delete_today():
    delete_sql = f"DELETE FROM {table_name} WHERE [date] = ?;"

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(delete_sql, datetime.now().strftime("%Y-%m-%d"))
        conn.commit()
        return cursor.rowcount

    except pyodbc.Error as e:
        logging.error(f"Error deleting/inserting data: {e}")
        return 0

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()


def save_csv(csv_file_path):
    print(csv_file_path)
    # Bulk insert SQL command
    bulk_insert_query = f"""
    BULK INSERT {table_name}
    FROM '{csv_file_path}'
    WITH (
        FIELDTERMINATOR = ',',
        ROWTERMINATOR = '0x0A',
        FIRSTROW = 2
    );
    """

    # Execute the bulk insert command
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(bulk_insert_query)
        conn.commit()
        print("Bulk insert completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()


def format_value(value):
    if isinstance(value, str):
        return f"'{value.replace('\'', '\'\'')}'"  # Escape single quotes in strings
    else:
        return str(value)

def safe_bulk(bulk_insert):
    columns = ', '.join(bulk_insert[0].keys())
    formatted_items = [f"({','.join(map(str, item.values()))})" for item in bulk_insert]
    formatted_rows = []

    for item in bulk_insert:
        formatted_values = [format_value(value) for value in item.values()]
        formatted_row = f"({','.join(formatted_values)})"
        formatted_rows.append(formatted_row)


    result = ','.join(formatted_rows)

    sql = (f"INSERT INTO {table_name} ({columns}) "
           f"VALUES {result};")

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        result = cursor.execute(sql)
        conn.commit()
        return result

    except pyodbc.Error as e:
        logging.error(f"Error inserting/updating data: {e}")
        return []

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

        if 'conn' in locals() and conn is not None:
            conn.close()


def save_entire_world_data(bulk_insert):
    columns = ', '.join(bulk_insert[0].keys())
    update_columns = ', '.join([f"{key} = ?" for key in bulk_insert[0].keys()])
    placeholders = ', '.join('?' * (len(bulk_insert[0])))

    sql = (f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});")

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        values = create_value(bulk_insert)
        result = cursor.executemany(sql, values)
        conn.commit()
        return result

    except pyodbc.Error as e:
        logging.error(f"Error inserting/updating data: {e}")
        return []

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()


def create_value(data):
    return [tuple(item.values()) for item in data]

