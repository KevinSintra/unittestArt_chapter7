
# 為了方便識別書中段落, 把所有程式碼都放在一起.
# 參考 p173 圖7-3 的類別圖(https://i.imgur.com/K9Zut3g.jpg?1) 只撰寫測試, 沒有實作程式

"""
    情境1: 測試模板類別模式
        類別圖是真實環境中常用的一種情境, 有幾個類別應該就要有幾個測試. (以圖來看要有三個鄵是, 這邊只寫一個做代表)
"""

class TestStandarStringParser:
    def test_getStringVersionFromHeader_singleDigit_found(self):
        input = 'header;version=1;\n'
        parser = StandardStringParser(input)
        version_name = parser.get_string_version_from_header()
        assert '1' == version_name

    def test_getStringVersionFromHeader_withMiorVersion_found(self):
        input = 'header;version=1.1;\n'
        parser = StandardStringParser(input)
        version_name = parser.get_string_version_from_header()
        assert '1.1' == version_name

    def test_getStringVersionFromHeader_withRevisionVersion_found(self):
        input = 'header;version=1.1.1;\n'
        parser = StandardStringParser(input)
        version_name = parser.get_string_version_from_header()
        assert '1.1.1' == version_name
