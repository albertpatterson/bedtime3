from datetime import datetime, timedelta
import math

five_min_sec = 5 * 60
five_min_ms = five_min_sec * 1000


def get_secs_till_bedtime(bedtime_hour, bedtime_minute):
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)

    diff_yesterday = (
        yesterday.replace(hour=bedtime_hour, minute=bedtime_minute, second=0) - now
    ).total_seconds()
    diff_today = (
        now.replace(hour=bedtime_hour, minute=bedtime_minute, second=0) - now
    ).total_seconds()
    diff_tomorrow = (
        tomorrow.replace(hour=bedtime_hour, minute=bedtime_minute, second=0) - now
    ).total_seconds()

    min_diff_abs = None
    min_diff = None
    for diff in [diff_yesterday, diff_today, diff_tomorrow]:
        if min_diff_abs is None or abs(diff) < min_diff_abs:
            min_diff = diff
            min_diff_abs = abs(diff)

    return min_diff


class ProgressiveSnoozer:
    def __init__(
        self,
        bedtime_hour,
        bedtime_minute,
        base_snooze_secs=five_min_sec,
        snooze_half_life_secs=3 * five_min_sec,
        min_snooze_sec=30,
    ):
        self._bedtime_hour = bedtime_hour
        self._bedtime_minute = bedtime_minute
        self._base_snooze_secs = base_snooze_secs
        self._snooze_half_life_secs = snooze_half_life_secs
        self._min_snooze_sec = min_snooze_sec

    def get_snooze_secs(self):
        secs_till_bed = get_secs_till_bedtime(self._bedtime_hour, self._bedtime_minute)

        if secs_till_bed > 0:
            return self._base_snooze_secs

        secs_since_bedtime = abs(secs_till_bed)

        denom_pow = math.floor(secs_since_bedtime / self._snooze_half_life_secs)

        cand_snooze_sec = round(self._base_snooze_secs / 2**denom_pow)
        return max(cand_snooze_sec, self._min_snooze_sec)

    def get_snooze_ms(self):
        return 1000 * self.get_snooze_secs()


def display_time(seconds):
    """Displays a number of seconds in a very short format (seconds, minutes, or hours)."""
    if seconds < 60:
        return f"{seconds}s"  # Display seconds
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes}m"  # Display minutes
    else:
        hours = int(seconds / 3600)
        return f"{hours}h"  # Display hours
