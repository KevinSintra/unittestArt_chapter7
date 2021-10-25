import datetime

"""
    # 如果時間為測試的目標時, 可能很多類別都使用到如果用依賴注入的方式會到處都需開接口注入, 導致程式不易閱讀與維護.
    # 此時可以使用另一個類別來統一, 此時也達成測試的目標之外, 也讓程式碼易於閱讀.

"""


class BaseSystemTime:
    __date__: datetime.datetime = None

    @staticmethod
    def Set(custom: datetime.datetime) -> None:
        BaseSystemTime.__date__ = custom
        pass

    @staticmethod
    def reset() -> None:
        BaseSystemTime.__date__ = None
        pass

    @staticmethod
    def now() -> datetime.datetime:
        if(BaseSystemTime.__date__ != None):
            return BaseSystemTime.__date__

        return datetime.datetime.now()
