import schedule
import time
from datetime import datetime
from fetcher.health_check import health_check
from fetcher.entire_world import call_tv_world
from fetcher.indonesia_trading import call_tv_indonesia
from model.holiday import get_holidays
from model.feature_flag import get_feature_flag


call_tv_indonesia()

def is_holiday():
    holidays = get_holidays()
    today = datetime.today().date()
    return any(holiday[0] == today for holiday in holidays) or is_weekend()


def is_weekend():
    today = datetime.today().weekday()
    return today in (5, 6)  # 5 is Saturday, 6 is Sunday


def is_friday():
    today = datetime.today().weekday()
    return today == 4  # 4 is Friday


def is_within_time_range(start_time, end_time):
    now = datetime.now().time()
    return start_time <= now <= end_time


def schedule_call_trading_view():
    if not is_holiday():
        call_tv_world()


def schedule_call_trading_view_indonesia():
    if not is_holiday():
        call_tv_indonesia()


def scheduled_task_indonesia():
    if is_friday():
        if is_within_time_range(datetime.strptime("08:50", "%H:%M").time(),
                                datetime.strptime("11:35", "%H:%M").time()) or \
                is_within_time_range(datetime.strptime("14:00", "%H:%M").time(),
                                     datetime.strptime("16:05", "%H:%M").time()):
            schedule_call_trading_view_indonesia()
    else:
        if is_within_time_range(datetime.strptime("08:50", "%H:%M").time(),
                                datetime.strptime("12:05", "%H:%M").time()) or \
                is_within_time_range(datetime.strptime("13:30", "%H:%M").time(),
                                     datetime.strptime("16:05", "%H:%M").time()):
            schedule_call_trading_view_indonesia()


def schedule_health_check():
    health_check()


# Schedule tasks
schedule.every().day.at("08:00").do(schedule_call_trading_view)
schedule.every(5).minutes.do(scheduled_task_indonesia)
schedule.every(30).seconds.do(health_check)

while True:
    schedule.run_pending()
    time.sleep(1)
