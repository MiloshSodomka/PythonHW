from string_utils import StringUtils
import pytest
from string_utils import StringUtils

class TestStringUtils:
    @pytest.fixture
    def utils(self):
        return StringUtils()

    # Тесты для capitalize
    def test_capitalize_positive(self, utils):
        assert utils.capitalize("skypro") == "Skypro"
        assert utils.capitalize("hello world") == "Hello world"
        assert utils.capitalize("123") == "123"
        assert utils.capitalize("тест") == "Тест"

    def test_capitalize_empty_string(self, utils):
        assert utils.capitalize("") == ""

    def test_capitalize_single_character(self, utils):
        assert utils.capitalize("a") == "A"
        assert utils.capitalize("A") == "A"

    def test_capitalize_already_capitalized(self, utils):
        assert utils.capitalize("Skypro") == "Skypro"

    # Тесты для trim
    def test_trim_positive(self, utils):
        assert utils.trim("   skypro") == "skypro"
        assert utils.trim("  hello world  ") == "hello world  "
        assert utils.trim("test") == "test"

    def test_trim_empty_string(self, utils):
        assert utils.trim("") == ""

    def test_trim_only_spaces(self, utils):
        assert utils.trim("     ") == ""

    def test_trim_no_leading_spaces(self, utils):
        assert utils.trim("skypro   ") == "skypro   "

    # Тесты для contains
    def test_contains_positive(self, utils):
        assert utils.contains("SkyPro", "S") is True
        assert utils.contains("SkyPro", "k") is True
        assert utils.contains("SkyPro", "U") is False
        assert utils.contains("", "a") is False
        assert utils.contains(" ", " ") is True

    def test_contains_empty_string(self, utils):
        assert utils.contains("", "a") is False

    def test_contains_empty_symbol(self, utils):
        assert utils.contains("SkyPro", "") is True

    def test_contains_symbol_not_found(self, utils):
        assert utils.contains("SkyPro", "X") is False

    # Тесты для delete_symbol
    def test_delete_symbol_positive(self, utils):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert utils.delete_symbol("Hello World", " ") == "HelloWorld"

    def test_delete_symbol_not_found(self, utils):
        assert utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_string(self, utils):
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_empty_symbol(self, utils):
        assert utils.delete_symbol("SkyPro", "") == "SkyPro"

    def test_delete_symbol_all_occurrences(self, utils):
        assert utils.delete_symbol("abababa", "a") == "bbb"
