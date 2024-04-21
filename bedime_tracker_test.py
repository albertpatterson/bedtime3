from freezegun import freeze_time  # $ pip install freezegun
from bedtime_tracker import BedtimeTracker


@freeze_time("2024-01-01 23:30:00")
def test_past_pm_bedtime():
    btt = BedtimeTracker(
        bedtime_hour=23, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert btt.is_bed_time()


@freeze_time("2024-01-01 22:30:00")
def test_before_pm_bedtime():
    btt = BedtimeTracker(
        bedtime_hour=23, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert not btt.is_bed_time()
    assert btt.time_until_bed().total_seconds() == 30 * 60


@freeze_time("2024-01-02 7:30:00")
def test_before_pm_morning():
    btt = BedtimeTracker(
        bedtime_hour=23, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert btt.is_bed_time()


@freeze_time("2024-01-02 8:30:00")
def test_after_pm_morning():
    btt = BedtimeTracker(
        bedtime_hour=23, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert not btt.is_bed_time()
    assert btt.time_until_bed().total_seconds() == 14.5 * 60 * 60


@freeze_time("2024-02-01 1:30:00")
def test_past_am_bedtime():
    btt = BedtimeTracker(
        bedtime_hour=1, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert btt.is_bed_time()


@freeze_time("2024-02-01 0:30:00")
def test_before_am_bedtime():
    btt = BedtimeTracker(
        bedtime_hour=1, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert not btt.is_bed_time()
    assert btt.time_until_bed().total_seconds() == 30 * 60


@freeze_time("2024-01-01 23:30:00")
def test_before_am_bedtime_2():
    btt = BedtimeTracker(
        bedtime_hour=1, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert not btt.is_bed_time()
    assert btt.time_until_bed().total_seconds() == 1.5 * 60 * 60


@freeze_time("2024-02-01 7:30:00")
def test_before_am_morning():
    btt = BedtimeTracker(
        bedtime_hour=1, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert btt.is_bed_time()


@freeze_time("2024-02-01 8:30:00")
def test_after_am_morning():
    btt = BedtimeTracker(
        bedtime_hour=1, bedtime_minute=0, morning_hour=8, morning_minute=0
    )
    assert not btt.is_bed_time()
    assert btt.time_until_bed().total_seconds() == 16.5 * 60 * 60
