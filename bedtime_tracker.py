from datetime import datetime, timedelta
from util import get_secs_till_bedtime


class BedtimeTracker:
    def __init__(self, bedtime_hour, bedtime_minute, morning_hour, morning_minute):
        self.bedtime_hour = bedtime_hour
        self.bedtime_minute = bedtime_minute
        self.morning_hour = morning_hour
        self.morning_minute = morning_minute
        self.sleep_secs = self._get_sleep_secs()

    def _get_sleep_timedelta(self):
        if self.bedtime_hour > self.morning_hour:
            return timedelta(
                hours=(23 - self.bedtime_hour), minutes=(60 - self.bedtime_minute)
            ) + timedelta(hours=self.morning_hour, minutes=self.morning_minute)
        else:
            return timedelta(
                hours=self.morning_hour - self.bedtime_hour,
                minutes=self.morning_minute - self.bedtime_minute,
            )

    def _get_sleep_secs(self):
        return self._get_sleep_timedelta().total_seconds()

    def is_bed_time(self):
        secs_till_bedtime = self.get_secs_till_bedtime()

        return secs_till_bedtime <= 0 and secs_till_bedtime > -1 * self.sleep_secs

    def get_secs_till_bedtime(self):
        return get_secs_till_bedtime(self.bedtime_hour, self.bedtime_minute)

    def get_secs_till_next_bedtime(self):
        secs = self.get_secs_till_bedtime()
        return secs if secs > 0 else 24 * 60 * 60 + secs
