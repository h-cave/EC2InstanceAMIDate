import pytest
from dateutil.tz import tzutc

from main.main import extract_date, format_times
from test.test_data import test_data
import datetime


def test_extract_date():
    assert extract_date(test_data)[0] == ['ami-09ee0944866c73f62', 'ami-09ee0944866c73f62', 'ami-09ee0944866c73f62']
    assert extract_date(test_data)[1] == ['i-0b9d46b86d18de170', 'i-0ec73e2ff716188a9', 'i-080e3e0d428d0ccc6']
    assert extract_date(test_data)[3] == ['webServer', 'webServer', 'webServer']


def test_format_times():
    time = [datetime.datetime(2023, 2, 28, 16, 38, 27, tzinfo=tzutc())]
    assert format_times(time) == ['02/28/2023, 16:38:27']
