from bedtime_window_manager import BedtimeWindowManager
from util import snooze_ms

bedtime_hour = 0
bedtime_minute = 0
morning_hour = 8
morning_minute = 0


# now = datetime.now()
# bedtime_hour = now.hour
# bedtime_minute = now.minute
# morning_hour = now.hour
# morning_minute = now.minute + 2


# count = 0


# def snooze_ms():
#     global count
#     count += 1
#     return 4 * 1000 + 1000 * count


btwm = BedtimeWindowManager(
    bedtime_hour, bedtime_minute, morning_hour, morning_minute, snooze_ms
)
