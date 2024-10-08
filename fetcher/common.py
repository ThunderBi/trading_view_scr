from datetime import datetime

url = 'https://scanner.tradingview.com/global/scan'

mapper_entire_world = {
    'symbol': 'name',
    'description': 'description',
    'price_52_week_low': 'price_52_week_low',
    'price_52_week_low_currency': 'currency',
    'price_52_week_high': 'price_52_week_high',
    'price_52_week_high_currency': 'currency',
    'price': 'close',
    'price_currency': 'currency',
    'total_revenue_yoy_growth_ttm': 'total_revenue_yoy_growth_ttm',
    'gross_profit_yoy_growth_ttm': 'gross_profit_yoy_growth_ttm',
    'net_income_yoy_growth_ttm': 'net_income_yoy_growth_ttm',
    'total_assets_yoy_growth_fy': 'total_assets_yoy_growth_fy',
    'total_debt_yoy_growth_fy': 'total_debt_yoy_growth_fy',
    'performance_percent_year_to_date': 'Perf.YTD',
    'volume_x_price_1_month': 'Value.Traded|1M',
    'volume_x_price_1_month_currency': 'currency',
    'earnings_per_share_basic_12_month_ttm': 'earnings_per_share_basic_ttm',
    'earnings_per_share_basic_12_month_ttm_currency': 'fundamental_currency_code',
    'dividends_yield_fy': 'dividends_yield_fy',
    'revenue_per_employee_annual': 'revenue_per_employee',
    'revenue_per_employee_annual_currency': 'fundamental_currency_code',
    'return_on_assets_trailing_fy': 'return_on_assets_fq',
    'return_on_equity_trailing_fy': 'return_on_equity_fq',
    'price_earnings_ttm': 'price_earnings_ttm',
    'sector': 'sector.tr',
    'average_volume_10d_calc': 'average_volume_10d_calc',
    'debt_to_asset_fy': 'debt_to_asset_fy',
    'debt_to_equity_fq': 'debt_to_equity_fq',
    'market_capitalization': 'market_cap_basic',
}

mapper_indonesia_trading = {
    'symbol': 'name',
    'description': 'description',
    'open_price': 'open',
    'open_currency': 'currency',
    'low': 'low',
    'low_currency': 'currency',
    'high': 'high',
    'high_currency': 'currency',
    'price': 'close',
    'price_currency': 'currency',
    'change_percentage': 'change',
    'volume': 'volume',
    'average_volume_10d_calc': 'average_volume_10d_calc',
    'average_volume_30d_calc': 'average_volume_30d_calc',
    'volume_x_price_1d': 'Value.Traded',
    'volatility_1d': 'Volatility.D',
    'volatility_1w': 'Volatility.W',
    'volatility_1m': 'Volatility.M',
    'aroon_1d_up': 'Aroon.Up',
    'aroon_1d_down': 'Aroon.Down',
    'average_directional_index_1d': 'ADX',
    'awesome_oscillator_1d': 'AO',
    'bollinger_bands_20_1d_upper': 'BB.upper',
    'bollinger_bands_20_1d_basis': 'BB.basis',
    'bollinger_bands_20_1d_lower': 'BB.lower',
    'bull_bear_power_13_4h': 'BBPower|240',
    'bull_bear_power_13_1d': 'BBPower',
    'bull_bear_power_13_1w': 'BBPower|1W',
    'bull_bear_power_13_1m': 'BBPower|1M',
    'chaikin_money_flow_20_1d': 'ChaikinMoneyFlow',
    'chaikin_money_flow_20_1w': 'ChaikinMoneyFlow|1W',
    'chaikin_money_flow_20_1M': 'ChaikinMoneyFlow|1M',
    'commodity_channel_index_20_1d': 'CCI20',
    'commodity_channel_index_20_1w': 'CCI20|1W',
    'commodity_channel_index_20_1m': 'CCI20|1M',
    'directional_movement_index_14_1d_positive': 'ADX+DI',
    'directional_movement_index_14_1d_negative': 'ADX-DI',
    'donchian_channels_20_1d_basis': 'DonchCh20.Middle',
    'donchian_channels_20_1d_lower': 'DonchCh20.Lower',
    'EMA12_1d': 'EMA12',
    'EMA26_1d': 'EMA26',
    'EMA50_1d': 'EMA50',
    'EMA200_1d': 'EMA200',
    'ichimoku_base_line_1d': 'Ichimoku.BLine',
    'ichimoku_conversation_line_1d': 'Ichimoku.CLine',
    'ichimoku_leading_span_a_1d': 'Ichimoku.Lead1',
    'ichimoku_leading_span_b_1d': 'Ichimoku.Lead2',
    'momentum_1d': 'Mom',
    'momentum_1w': 'Mom|1W',
    'momentum_1m': 'Mom|1M',
    'money_flow_14_1d': 'MoneyFlow',
    'money_flow_14_1w': 'MoneyFlow|1W',
    'money_flow_14_1m': 'MoneyFlow|1M',
    'macd_1d_level': 'MACD.macd',
    'macd_1d_signal': 'MACD.signal',
    'pivot_points_fibonacci_1d_r1': 'Pivot.M.Fibonacci.R1',
    'pivot_points_fibonacci_1d_s1': 'Pivot.M.Fibonacci.S1',
    'pivot_points_fibonacci_1d_r2': 'Pivot.M.Fibonacci.R2',
    'pivot_points_fibonacci_1d_s2': 'Pivot.M.Fibonacci.S2',
    'pivot_points_fibonacci_1d_r3': 'Pivot.M.Fibonacci.R3',
    'pivot_points_fibonacci_1d_s3': 'Pivot.M.Fibonacci.S3',
    'rate_of_change_9_1d': 'ROC',
    'rate_of_change_9_1w': 'ROC|1W',
    'rate_of_change_9_1m': 'ROC|1M',
    'stochastic_rsi_k_1d': 'Stoch.RSI.K',
    'stochastic_rsi_d_1d': 'Stoch.RSI.D',
    'william_percentage_range_1d': 'W.R',
    'william_percentage_range_1W': 'W.R|1W',
    'william_percentage_range_1M': 'W.R|1M',
}


def format_value(value):
    """Format the value according to specified rules:
       - If the value is empty or None, return 0.
       - If the value is a float, limit decimal places to 5.
    """
    if value is None or value == '':
        return 0

    try:
        # Attempt to convert value to float for decimal handling
        if '.' in str(value):
            float_value = float(value)
            # Round to 5 decimal places
            return round(float_value, 5)
        return value
    except ValueError:
        # If conversion fails, return the original value
        return value


def get_mapping(columns, mapper, request, responses):
    mappings = []
    for response in responses:
        mapping = {}
        mapping['date'] = datetime.now().strftime('%Y-%m-%d')
        for column in columns:
            mapped_value = mapper[column]
            index = request.index(mapped_value)
            value = response['d'][index]
            value = format_value(value)
            if (column == 'sector' or column.endswith('_currency')) and (value is None or value == ''
                                                                         or value == 0):
                value = ''

            mapping[column] = value
        # mapping['created_at'] = datetime.now()
        mappings.append(mapping)
    return mappings
