from model.common import *
from datetime import datetime
import logging

logging.basicConfig(filename='logs/db_world.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


table_name = 'entire_world_screener'
columns = [
    'symbol',
    'description',
    'price_52_week_low',
    'price_52_week_low_currency',
    'price_52_week_high',
    'price_52_week_high_currency',
    'price',
    'price_currency',
    'total_revenue_yoy_growth_ttm',
    'gross_profit_yoy_growth_ttm',
    'net_income_yoy_growth_ttm',
    'total_assets_yoy_growth_fy',
    'total_debt_yoy_growth_fy',
    'performance_percent_year_to_date',
    'volume_x_price_1_month',
    'volume_x_price_1_month_currency',
    'earnings_per_share_basic_12_month_ttm',
    'earnings_per_share_basic_12_month_ttm_currency',
    'dividends_yield_fy',
    'revenue_per_employee_annual',
    'revenue_per_employee_annual_currency',
    'return_on_assets_trailing_fy',
    'return_on_equity_trailing_fy',
    'price_earnings_ttm',
    'sector',
    'average_volume_10d_calc',
    'debt_to_asset_fy',
    'debt_to_equity_fq',
    'market_capitalization'
]


def save_entire_world_data(bulk_insert):
    columns = ', '.join(bulk_insert[0].keys())
    update_columns = ', '.join([f"{key} = ?" for key in bulk_insert[0].keys()])
    placeholders = ', '.join('?' * (len(bulk_insert[0])))
    str_values = ', '.join([f"({placeholders})"] * len(bulk_insert))

    sql = (f"INSERT INTO {table_name} ({columns}) VALUES {str_values};")

    try:
        cursor = conn.cursor()
        values = create_value(bulk_insert)
        result = cursor.execute(sql, values)
        conn.commit()
        return result

    except pyodbc.Error as e:
        logging.error(f"Error inserting/updating data: {e}")
        return []

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()


def create_value(data):
    return [item for sublist in data for item in sublist.values()]

