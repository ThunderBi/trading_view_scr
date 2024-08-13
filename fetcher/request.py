request_entire_world = {
    "columns": [
        "name",
        "description",
        "logoid",
        "update_mode",
        "type",
        "typespecs",
        "price_52_week_low",
        "pricescale",
        "minmov",
        "fractional",
        "minmove2",
        "currency",
        "price_52_week_high",
        "close",
        "total_revenue_yoy_growth_ttm",
        "gross_profit_yoy_growth_ttm",
        "net_income_yoy_growth_ttm",
        "total_assets_yoy_growth_fy",
        "total_debt_yoy_growth_fy",
        "Perf.YTD",
        "Value.Traded|1M",
        "earnings_per_share_basic_ttm",
        "fundamental_currency_code",
        "dividends_yield_fy",
        "revenue_per_employee",
        "return_on_assets_fq",
        "return_on_equity_fq",
        "price_earnings_ttm",
        "sector.tr",
        "market",
        "sector",
        "average_volume_10d_calc",
        "debt_to_asset_fy",
        "debt_to_equity_fq",
        "market_cap_basic",
        "exchange"
    ],
    "filter": [
        {
            "left": "is_primary",
            "operation": "equal",
            "right": True
        }
    ],
    "ignore_unknown_fields": False,
    "options": {
        "lang": "en"
    },
    "price_conversion": {
        "to_currency": "usd"
    },
    "range": [
        0,
        100000
    ],
    "sort": {
        "sortBy": "return_on_equity_fq",
        "sortOrder": "desc"
    },
    "symbols": {},
    "markets": [
        "america",
        "argentina",
        "australia",
        "austria",
        "bahrain",
        "bangladesh",
        "belgium",
        "brazil",
        "canada",
        "chile",
        "china",
        "colombia",
        "cyprus",
        "czech",
        "denmark",
        "egypt",
        "estonia",
        "finland",
        "france",
        "germany",
        "greece",
        "hongkong",
        "hungary",
        "iceland",
        "india",
        "indonesia",
        "israel",
        "italy",
        "japan",
        "kenya",
        "kuwait",
        "latvia",
        "lithuania",
        "luxembourg",
        "malaysia",
        "mexico",
        "morocco",
        "netherlands",
        "newzealand",
        "nigeria",
        "norway",
        "pakistan",
        "peru",
        "philippines",
        "poland",
        "portugal",
        "qatar",
        "romania",
        "russia",
        "ksa",
        "serbia",
        "singapore",
        "slovakia",
        "rsa",
        "korea",
        "spain",
        "srilanka",
        "sweden",
        "switzerland",
        "taiwan",
        "thailand",
        "tunisia",
        "turkey",
        "uae",
        "uk",
        "venezuela",
        "vietnam"
    ],
    "filter2": {
        "operator": "and",
        "operands": [
            {
                "operation": {
                    "operator": "or",
                    "operands": [
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "stock"
                                        }
                                    },
                                    {
                                        "expression": {
                                            "left": "typespecs",
                                            "operation": "has",
                                            "right": [
                                                "common"
                                            ]
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "stock"
                                        }
                                    },
                                    {
                                        "expression": {
                                            "left": "typespecs",
                                            "operation": "has",
                                            "right": [
                                                "preferred"
                                            ]
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "dr"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "fund"
                                        }
                                    },
                                    {
                                        "expression": {
                                            "left": "typespecs",
                                            "operation": "has_none_of",
                                            "right": [
                                                "etf"
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}

request_indonesia_trading = {
    "columns": [
        "name",
        "description",
        "logoid",
        "update_mode",
        "type",
        "typespecs",
        "open",
        "pricescale",
        "minmov",
        "fractional",
        "minmove2",
        "currency",
        "high",
        "low",
        "close",
        "change",
        "volume",
        "average_volume_10d_calc",
        "average_volume_30d_calc",
        "Value.Traded",
        "Volatility.D",
        "Volatility.W",
        "Volatility.M",
        "Aroon.Up",
        "Aroon.Down",
        "ADX",
        "AO",
        "BB.upper",
        "BB.basis",
        "BB.lower",
        "BBPower|240",
        "BBPower",
        "BBPower|1W",
        "BBPower|1M",
        "ChaikinMoneyFlow",
        "ChaikinMoneyFlow|1W",
        "ChaikinMoneyFlow|1M",
        "CCI20",
        "CCI20|1W",
        "CCI20|1M",
        "ADX+DI",
        "ADX-DI",
        "DonchCh20.Upper",
        "DonchCh20.Middle",
        "DonchCh20.Lower",
        "EMA12",
        "EMA26",
        "EMA50",
        "EMA200",
        "Ichimoku.BLine",
        "Ichimoku.CLine",
        "Ichimoku.Lead1",
        "Ichimoku.Lead2",
        "Mom",
        "Mom|1W",
        "Mom|1M",
        "MoneyFlow",
        "MoneyFlow|1W",
        "MoneyFlow|1M",
        "MACD.macd",
        "MACD.signal",
        "Pivot.M.Fibonacci.R1",
        "Pivot.M.Fibonacci.S1",
        "Pivot.M.Fibonacci.R2",
        "Pivot.M.Fibonacci.S2",
        "Pivot.M.Fibonacci.R3",
        "Pivot.M.Fibonacci.S3",
        "ROC",
        "ROC|1W",
        "ROC|1M",
        "Stoch.RSI.K",
        "Stoch.RSI.D",
        "W.R",
        "W.R|1W",
        "W.R|1M",
        "exchange"
    ],
    "ignore_unknown_fields": False,
    "options": {
        "lang": "en"
    },
    "range": [
        0,
        100000
    ],
    "sort": {
        "sortBy": "name",
        "sortOrder": "asc"
    },
    "symbols": {},
    "markets": [
        "indonesia"
    ],
    "filter2": {
        "operator": "and",
        "operands": [
            {
                "operation": {
                    "operator": "or",
                    "operands": [
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "stock"
                                        }
                                    },
                                    {
                                        "expression": {
                                            "left": "typespecs",
                                            "operation": "has",
                                            "right": [
                                                "common"
                                            ]
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "stock"
                                        }
                                    },
                                    {
                                        "expression": {
                                            "left": "typespecs",
                                            "operation": "has",
                                            "right": [
                                                "preferred"
                                            ]
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "dr"
                                        }
                                    }
                                ]
                            }
                        },
                        {
                            "operation": {
                                "operator": "and",
                                "operands": [
                                    {
                                        "expression": {
                                            "left": "type",
                                            "operation": "equal",
                                            "right": "fund"
                                        }
                                    },
                                    {
                                        "expression": {
                                            "left": "typespecs",
                                            "operation": "has_none_of",
                                            "right": [
                                                "etf"
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }
}