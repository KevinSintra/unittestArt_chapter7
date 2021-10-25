import pytest
import datetime

from BaseSystemTime import BaseSystemTime
from TimeLogger import TimeLogger


class TestTimeLogger():
    def test_settingSystemTime_always_changesTime(self):
        dt = datetime.datetime(2021, 10, 25).replace(
            hour=11, minute=59, second=59)
        BaseSystemTime.Set(dt)
        result = TimeLogger.createMsg('a')
        assert '2021/10/25 11:59:59 a' == result

    def test_defaultSystemTime_nowtime(self):
        result = TimeLogger.createMsg('a')
        expected = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ' ' + 'a'
        assert expected == result

    def teardown_method(self):
        """
            teardown any state that was previously setup with a setup_method call.
            確保每個測試方法的時間都是初始化的
        """
        BaseSystemTime.reset()
