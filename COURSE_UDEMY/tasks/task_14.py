#  підготувати модуль до імпорту через * з нього всього крім os and time
import os
import time

__all__ = ["IMPORTANT_VAR", "current_time"]

IMPORTANT_VAR = "SOME FOR USE ANYWHERE"


def current_time():
    return time.asctime()


time_now = current_time()
print(time_now)
