import pytest
import abc
# 為了方便識別書中段落, 把所有程式碼都放在一起.

"""
    情境1: 測試沒有遵循 DRY
    情境1 - 重構: 將重複的地方抽出, 並讓相關測試類去繼承
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

class BaseTestsClass:
    """基底類別供測試使用"""

    def fake_logger(self, mocker):
        """
        不是所有測試方法都會用到 LoggingFacility, 所以讓他們各自使用
        """
        logger = mocker.patch('test_ApiExample1.ILogger')  # 模擬物件
        return logger

    def teardown_method(self):
        LoggingFacility.set_logger(None)


class TestAnalyzer(BaseTestsClass):
    def test_analyzer_filenameTooShort_logCalled(self, mocker):
        logger = super().fake_logger(mocker)
        mocker_method = mocker.patch.object(logger, 'log')
        LoggingFacility.set_logger(logger)

        analyzer = LogAnalyzer()
        analyzer.analyzer('a.txt')

        assert mocker_method.called == True


class TestConfigurationManager(BaseTestsClass):
    def test_configured_logCalled(self, mocker):
        logger = super().fake_logger(mocker)
        mocker_method = mocker.patch.object(logger, 'log')
        LoggingFacility.set_logger(logger)

        manager = ConfigurationManager()
        manager.configured('api1.json')

        assert mocker_method.called == True
