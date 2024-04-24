from datetime import datetime
import math

five_min = 5 * 60 * 1000


def snooze_ms():
    now = datetime.now()
    bt = datetime(now.year, now.month, now.day, hour=0, minute=0)
    dt_past_bedtime = now - bt
    mins_past_bedtime = dt_past_bedtime.total_seconds() / 60

    demon_pow = math.floor(mins_past_bedtime / 15)

    return five_min / 2**demon_pow
