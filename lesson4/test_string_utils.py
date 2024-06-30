import pytest
from string_utils import StringUtils

#capitilize
@pytest.mark.positive_test
@pytest.mark.parametrize('str, result', [("some text", "Some text"), ("некоторый текст", "Некоторый текст"), \
                        ("123", "123"),  ("@#$%", "@#$%"), ("текст с 1234", "Текст с 1234"), \
                        ("123 текст", "123 текст")])
def test_capitilize_func_positive(str, result):
    strUtil = StringUtils()
    res = strUtil.capitilize(str)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, result', [("", ""), (" ", " ")])
def test_capitilize_func_negative(str, result):
    strUtil = StringUtils()
    res = strUtil.capitilize(str)
    assert res == result


# #trim
@pytest.mark.positive_test
@pytest.mark.parametrize('str, result', [("Text", "Text"), (" Text", "Text"), ("    Text", "Text"), \
                                         (" T ext", "T ext"), ("  123", "123"), ("  @#$%", "@#$%"), \
                                         (" t e x t ", "t e x t ")])
def test_trim_func_positive(str, result):
    strUtil = StringUtils()
    res = strUtil.trim(str)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, result', [("", ""), (" ", "")])
def test_trim_func_negative(str, result):
    strUtil = StringUtils()
    res = strUtil.trim(str)
    assert res == result


#to_list
@pytest.mark.positive_test
@pytest.mark.parametrize('str, delimeter, result', [("a,b,c,d", ",", ["a", "b", "c", "d"]), \
                                                    ("1:2", ":", ["1", "2"]), \
                                                    ("т е с т $ %", " ", ["т", "е", "с", "т", "$", "%"]), \
                                                    (" ", " ", [])])
def test_to_list_func_positive(str, delimeter, result):
    strUtil = StringUtils()
    res = strUtil.to_list(str, delimeter)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('str, result', [("a,b,c,d,e", ["a", "b", "c", "d", "e"])])
def test_to_list_func_positive_default(str, result):
    strUtil = StringUtils()
    res = strUtil.to_list(str)
    assert res == result
    

@pytest.mark.negative_test
@pytest.mark.parametrize('str, delimeter, result', [("", "", []), (" : ", ":", [" ", " "]), \
                                                    (" ", ":", [" "]), ("a,b,c,d", " ", ["a,b,c,d"])])
def test_to_list_func_negative(str, delimeter, result):
    strUtil = StringUtils()
    res = strUtil.to_list(str, delimeter)
    assert res == result


#contains
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symbol, result', [("Тест", "е", True), ("Test", "w", False), \
                                                 ("123 456 test", "456", True), ("@#$%^", "^%", False), \
                                                 ("Some text for test", "fort", False)])
def test_contains_func_positive(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.contains(str, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, symbol, result', [(" ", "", True), ("", "", True)])
def test_contains_func_negative(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.contains(str, symbol)
    assert res == result


#delete_symbol
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symbol, result', [("Текст", "т", "Текс"), ("Some text", "e", "Som txt"), \
                                                 ("123456789", "9", "12345678"), ("!@#$%^", "$", "!@#%^"), \
                                                 ("Text", "w", "Text"), ("Three words text", " ", "Threewordstext")])
def test_delete_symbol_func_positive(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.delete_symbol(str, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, symbol, result', [("", "", ""), (" ", "", " "), \
                                                 (" ", " ", ""), ("   t", " ", "t"), \
                                                 ("   t", "t", "   "), ("Text", "е", "Text")])
# в последнем случае "е" русская, "Text" - на английском
def test_delete_symbol_func_negative(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.delete_symbol(str, symbol)
    assert res == result


#starts_with
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symbol, result', [("Текст", "Т", True), ("Text", "e", False), \
                                                 ("12134", "1", True), ("@#$%^&", "%", False)])
def test_starts_with_func_positive(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.starts_with(str, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, symbol, result', [("", "", True), (" ", " ", True), \
                                                 (" ", "", True), ("   T", " ", True), \
                                                 ("text", "T", False), ("t", "t", True)])
def test_starts_with_func_negative(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.starts_with(str, symbol)
    assert res == result


#end_with
@pytest.mark.positive_test
@pytest.mark.parametrize('str, symbol, result', [("Текст", "т", True), ("Text", "e", False), \
                                                 ("12134", "4", True), ("@#$%^&", "@", False)])
def test_end_with_func_positive(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.end_with(str, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, symbol, result', [("", "", True), (" ", " ", True), \
                                                 (" ", "", True), ("   T", " ", False), \
                                                 ("text", "T", False), ("t", "t", True)])
def test_end_with_func_negative(str, symbol, result):
    strUtil = StringUtils()
    res = strUtil.end_with(str, symbol)
    assert res == result


#is_empty
@pytest.mark.positive_test
@pytest.mark.parametrize('str, result', [("", True), (" ", True), \
                                         ("     ", True), ("123", False), \
                                         ("Not empty", False), ("@#$%^", False), \
                                         ("      F", False)])
def test_is_empty_func_positive(str, result):
    strUtil = StringUtils()
    res = strUtil.is_empty(str)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('str, result', [(123, False)])
def test_is_empty_func_negative(str, result):
    strUtil = StringUtils()
    res = strUtil.is_empty(str)
    assert res == result


#list_to_string
@pytest.mark.positive_test
@pytest.mark.parametrize('list, joiner, result', [(["a", "b", "c"], ", ", "a, b, c"), \
                                                  (["$", "$"], "$", "$$$")])
def test_list_to_string_func_positive(list, joiner, result):
    strUtil = StringUtils()
    res = strUtil.list_to_string(list, joiner)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('list, result', [(["a", "b", "c"], "a, b, c")])
def test_list_to_string_func_positive_default(list, result):
    strUtil = StringUtils()
    res = strUtil.list_to_string(list)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('list, joiner, result', [([], "", ""), ([" ", "a"], " ", "  a"), \
                                                  ([" "], " ", "  ")])
def test_list_to_string_func_negative(list, joiner, result):
    strUtil = StringUtils()
    res = strUtil.list_to_string(list, joiner)
    assert res == result
