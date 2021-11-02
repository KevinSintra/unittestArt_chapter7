import abc

# 為了方便識別書中段落, 把所有程式碼都放在一起.
# 參考 p173 圖7-3 的類別圖(https://i.imgur.com/K9Zut3g.jpg?1) 只撰寫測試, 沒有實作程式

"""
    測試模板類別模式

    情境1:
        類別圖是真實環境中常用的一種情境, 有幾個類別應該就要有幾個測試. (以圖來看要有三個鄵是, 這邊只寫一個做代表)

    情境2: 
        因為: 每個測試類別中寫的測試方法是相同的, 其中只有被測試的類別不同.(DRY)
        所以: 打算運用樣板模式來簡化此次的測試
            # 增加基底類別
            # 使用抽象去規範衍生測試類別, 要實作的方法. 相當於衍生類別只做設定
            # 將測試方法轉到基底類別

        note: 
                撇開實力化的類別不同來說, 也可以用 pytest 參數化的方法達成, 也不用搞繼承關係了. 
            但不知道繼承與參數化的方式, 哪種比較容易閱讀.
"""


class BaseStringParser(metaclass=abc.ABCMeta):
    def expected_singl_digit(self) -> str:
        return '1'

    def expected_with_minor(self) -> str:
        return '1.1'

    def expected_with_revision(self) -> str:
        return '1.1.1'

    @abc.abstractmethod
    def get_parser(input: str) -> IStringParser:
        pass

    @abc.abstractmethod
    def header_version_single_digit() -> str:
        pass

    @abc.abstractmethod
    def header_version_minor() -> str:
        pass

    @abc.abstractmethod
    def header_version_revision() -> str:
        pass

    def test_getStringVersionFromHeader_singleDigit_found(self):
        input = self.header_version_single_digit()
        parser = self.get_parser(input)
        version_name = parser.get_string_version_from_header()
        assert self.expected_singl_digit() == version_name

    def test_getStringVersionFromHeader_withMiorVersion_found(self):
        input = self.header_version_minor()
        parser = self.get_parser(input)
        version_name = parser.get_string_version_from_header()
        assert self.expected_with_minor() == version_name

    def test_getStringVersionFromHeader_withRevisionVersion_found(self):
        input = self.header_version_revision()
        parser = self.get_parser(input)
        version_name = parser.get_string_version_from_header()
        assert self.expected_with_revision() == version_name


class TestStandarStringParse(BaseStringParser):
    def get_parser(self, input: str) -> IStringParser:
        return StandarStringParse(input)

    def header_version_single_digit(self):
        return f'header;version={super().expected_singl_digit()};\n'

    def header_version_minor(self):
        return f'header;version={super().expected_with_minor()};\n'

    def header_version_revision(self):
        return f'header;version={super().expected_with_revision()};\n'
