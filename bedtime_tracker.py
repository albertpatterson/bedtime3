from datetime import datetime, timedelta


class BedtimeTracker:
    def __init__(self, bedtime_hour, bedtime_minute, morning_hour, morning_minute):
        self.bedtime_hour = bedtime_hour
        self.bedtime_minute = bedtime_minute
        self.morning_hour = morning_hour
        self.morning_minute = morning_minute
        self.sleep_time = self._get_sleep_time()

    def _get_sleep_time(self):
        if self.bedtime_hour > self.morning_hour:
            return timedelta(
                hours=(23 - self.bedtime_hour), minutes=(60 - self.bedtime_minute)
            ) + timedelta(hours=self.morning_hour, minutes=self.morning_minute)
        else:
            return timedelta(
                hours=self.morning_hour - self.bedtime_hour,
                minutes=self.morning_minute - self.bedtime_minute,
            )

    def is_bed_time(self):

        seconds_till_bed = self.time_until_bed().total_seconds()

        past_bed_time = (
            seconds_till_bed > 24 * 60 * 60 - self.sleep_time.total_seconds()
        )

        return seconds_till_bed == 0 or past_bed_time

    def time_until_bed(self):
        now = datetime.now()
        dt = (
            datetime(
                year=now.year,
                month=now.month,
                day=now.day,
                hour=self.bedtime_hour,
                minute=self.bedtime_minute,
                second=now.second,
            )
            - now
        )

        if dt.total_seconds() < 0:
            dt += timedelta(hours=24)

        return dt
