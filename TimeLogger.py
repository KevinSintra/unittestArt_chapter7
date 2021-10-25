from BaseSystemTime import BaseSystemTime


class TimeLogger():
    @staticmethod
    def createMsg(msg: str) -> str:
        return BaseSystemTime.now().strftime("%Y/%m/%d %H:%M:%S") + ' ' + msg
