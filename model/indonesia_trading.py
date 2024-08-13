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


def save_entire_world_data(bulk_insert):
    columns = ', '.join(bulk_insert[0].keys())
    update_columns = ', '.join([f"{key} = ?" for key in bulk_insert[0].keys()])
    placeholders = ', '.join('?' * len(bulk_insert[0]))

    sql = (f"MERGE INTO {table_name} AS target "
           f"USING (SELECT ? AS symbol, ? AS [date]) AS source "
           f"ON (target.symbol = source.symbol AND target.[date] = source.[date]) "
           f"WHEN MATCHED THEN "
           f"UPDATE SET {update_columns} "
           f"WHEN NOT MATCHED THEN "
           f"INSERT ({columns}) VALUES ({placeholders});")

    try:
        cursor = conn.cursor()
        values = create_value(bulk_insert)
        result = cursor.executemany(sql, [tuple([v[0], datetime.now().strftime("%Y-%m-%d")] + list(v) + list(v)) for v in values])
        conn.commit()
        return result

    except pyodbc.Error as e:
        logging.error(f"Error inserting/updating data: {e}")
        return []

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()


def call_sp_calculate():
    try:
        cursor = conn.cursor()
        result = cursor.callproc(".s_IndonesiaTrading_Calculate", [])
        conn.commit()
        return result

    except pyodbc.Error as e:
        logging.error(f"Error call cursor data: {e}")
        return []

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()

def create_value(data):
    return [tuple(item.values()) for item in data]

