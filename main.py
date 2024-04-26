from bedtime_window_manager import BedtimeWindowManager
from util import ProgressiveSnoozer

bedtime_hour = 0
bedtime_minute = 0
morning_hour = 8
morning_minute = 0

snoozer = ProgressiveSnoozer(
    bedtime_hour=bedtime_hour,
    bedtime_minute=bedtime_minute,
)

snooze_ms = lambda: snoozer.get_snooze_ms()


# from datetime import datetime

# now = datetime.now()
# bedtime_hour = now.hour
# bedtime_minute = now.minute
# morning_hour = now.hour
# morning_minute = now.minute + 5

# snoozer = ProgressiveSnoozer(
#     bedtime_hour=bedtime_hour,
#     bedtime_minute=bedtime_minute,
#     base_snooze_secs=10,
#     snooze_half_life_secs=30,
#     min_snooze_sec=3,
# )

# snooze_ms = lambda: snoozer.get_snooze_ms()


btwm = BedtimeWindowManager(
    bedtime_hour, bedtime_minute, morning_hour, morning_minute, snooze_ms
)
