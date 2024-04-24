from freezegun import freeze_time  # $ pip install freezegun
from util import snooze_ms, five_min


@freeze_time("2024-01-01 0:01:00")
def test_snooze_ms_1_min():
    assert snooze_ms() == five_min


@freeze_time("2024-01-01 0:14:00")
def test_snooze_ms_14_min():
    assert snooze_ms() == five_min


@freeze_time("2024-01-01 0:16:00")
def test_snooze_ms_16_min():
    assert snooze_ms() == five_min / 2


@freeze_time("2024-01-01 0:29:00")
def test_snooze_ms_29_min():
    assert snooze_ms() == five_min / 2


@freeze_time("2024-01-01 0:31:00")
def test_snooze_ms_31_min():
    assert snooze_ms() == five_min / 4


@freeze_time("2024-01-01 0:44:00")
def test_snooze_ms_44_min():
    assert snooze_ms() == five_min / 4


@freeze_time("2024-01-01 0:46:00")
def test_snooze_ms_46_min():
    assert snooze_ms() == five_min / 8
