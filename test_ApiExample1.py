import pytest
import abc
# 為了方便識別書中段落, 把所有程式碼都放在一起.

"""
    情境1: 測試沒有遵循 DRY
"""


class ILogger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def log(msg: str) -> None:
        pass


class LoggingFacility:
    """工具類: 因很多地方使用, 所以抽出來統一後提供給各處使用. 方便維護外也可被測試"""
    __logger__: ILogger = None

    @staticmethod
    def get_logger() -> ILogger:
        return LoggingFacility.__logger__

    @staticmethod
    def set_logger(logger: ILogger) -> None:
        LoggingFacility.__logger__ = logger


class LogAnalyzer:
    """使用 LoggingFacility 工具類的高階物件"""

    def analyzer(self, filename: str) -> None:
        if(len(filename) < 8):
            LoggingFacility.get_logger().log('filename too short:' + filename)


class ConfigurationManager:
    """使用 LoggingFacility 工具類的高階物件"""

    def configured(self, config_name: str) -> None:
        LoggingFacility.get_logger().log('the file configured:' + config_name)


# 以下為測試程式碼


class TestAnalyzer:
    def test_analyzer_filenameTooShort_logCalled(self, mocker):
        logger = mocker.patch('test_ApiExample1.ILogger')  # 模擬物件
        mocker_method = mocker.patch.object(logger, 'log')
        LoggingFacility.set_logger(logger)

        analyzer = LogAnalyzer()
        analyzer.analyzer('a.txt')

        assert mocker_method.called == True

    def teardown_method(self):
        LoggingFacility.set_logger(None)


class TestConfigurationManager:
    def test_configured_logCalled(self, mocker):
        logger = mocker.patch('test_ApiExample1.ILogger') # 模擬物件
        mocker_method = mocker.patch.object(logger, 'log')
        LoggingFacility.set_logger(logger)

        manager = ConfigurationManager()
        manager.configured('api1.json')

        assert mocker_method.called == True