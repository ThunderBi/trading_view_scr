import schedule
import time
from datetime import datetime
from fetcher.entire_world import call_trading_view
from fetcher.indonesia_trading import call_trading_view_indonesia_trading

call_trading_view()

def is_weekend():
    today = datetime.today().weekday()
    return today == 5 or today == 6


def schedule_call_trading_view():
    if not is_weekend():
        call_trading_view()


def schedule_call_trading_view_indonesia():
    if not is_weekend():
        call_trading_view_indonesia_trading()


schedule.every().day.at("08:00").do(schedule_call_trading_view)
schedule.every(5).minutes.between("08:50", "16:05").do(schedule_call_trading_view_indonesia)

while True:
    schedule.run_pending()
    time.sleep(30)
