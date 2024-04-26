from freezegun import freeze_time  # $ pip install freezegun
from util import ProgressiveSnoozer, five_min_ms, get_secs_till_bedtime


@freeze_time("2024-01-01 0:01:00")
def test_snooze_ms_1_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == five_min_ms


@freeze_time("2024-01-01 0:14:00")
def test_snooze_ms_14_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == five_min_ms


@freeze_time("2024-01-01 0:16:00")
def test_snooze_ms_16_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == five_min_ms / 2


@freeze_time("2024-01-01 0:29:00")
def test_snooze_ms_29_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == five_min_ms / 2


@freeze_time("2024-01-01 0:31:00")
def test_snooze_ms_31_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == five_min_ms / 4


@freeze_time("2024-01-01 0:44:00")
def test_snooze_ms_44_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == five_min_ms / 4


@freeze_time("2024-01-01 0:46:00")
def test_snooze_ms_46_min():
    snoozer = ProgressiveSnoozer(0, 0)
    assert snoozer.get_snooze_ms() == 1000 * round(five_min_ms / 1000 / 8)


@freeze_time("2024-01-01 17:00:00")
def test_get_secs_till_bedtime_6_hour_before_pm():
    assert get_secs_till_bedtime(23, 0) == 6 * 60 * 60


@freeze_time("2024-01-01 21:45:00")
def test_get_secs_till_bedtime_30_min_before_pm():
    assert get_secs_till_bedtime(22, 15) == 30 * 60


@freeze_time("2024-01-01 22:37:00")
def test_get_secs_till_bedtime_7_min_after_pm():
    assert get_secs_till_bedtime(22, 30) == -7 * 60


# crosses into next day
@freeze_time("2024-01-01 02:30:00")
def test_get_secs_till_bedtime_4_hour_after_pm():
    assert get_secs_till_bedtime(22, 30) == -4 * 60 * 60


# crosses into next day
@freeze_time("2024-01-01 07:30:00")
def test_get_secs_till_bedtime_9_hour_after_pm():
    assert get_secs_till_bedtime(22, 30) == -9 * 60 * 60


# crosses into next day (closest is upcoming rather than past bedtime)
@freeze_time("2024-01-01 12:30:00")
def test_get_secs_till_bedtime_14_hour_after_pm():
    assert get_secs_till_bedtime(22, 30) == 10 * 60 * 60


# crosses into next day
@freeze_time("2024-01-01 18:00:00")
def test_get_secs_till_bedtime_6_hour_before_am():
    assert get_secs_till_bedtime(0, 0) == 6 * 60 * 60


# crosses into next day
@freeze_time("2024-01-01 20:00:00")
def test_get_secs_till_bedtime_6_hour_before_am_2():
    assert get_secs_till_bedtime(2, 0) == 6 * 60 * 60


@freeze_time("2024-01-01 00:15:00")
def test_get_secs_till_bedtime_30_min_before_am():
    assert get_secs_till_bedtime(0, 45) == 30 * 60


@freeze_time("2024-01-01 01:37:00")
def test_get_secs_till_bedtime_7_min_after_am():
    assert get_secs_till_bedtime(1, 30) == -7 * 60


@freeze_time("2024-01-01 02:30:00")
def test_get_secs_till_bedtime_4_hour_after_am():
    assert get_secs_till_bedtime(22, 30) == -4 * 60 * 60


@freeze_time("2024-01-01 09:00:00")
def test_get_secs_till_bedtime_9_hour_after_am():
    assert get_secs_till_bedtime(0, 0) == -9 * 60 * 60
