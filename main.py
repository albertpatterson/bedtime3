from bedtime_window_manager import BedtimeWindowManager

# bedtime_hour = 0
# bedtime_minute = 0
# morning_hour = 8
# morning_minute = 0

# snooze_ms = 5 * 60 * 1000


from datetime import datetime

now = datetime.now()

bedtime_hour = now.hour
bedtime_minute = now.minute
morning_hour = now.hour
morning_minute = now.minute + 2

snooze_ms = 5 * 1000

btwm = BedtimeWindowManager(
    bedtime_hour, bedtime_minute, morning_hour, morning_minute, snooze_ms
)
