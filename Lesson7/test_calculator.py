import pytest
from pages.calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.calculator_page = CalculatorPage(driver)

    def test_calculator_with_delay(self):
        (self.calculator_page.open()
         .set_delay(45)
         .click_button('7')
         .click_button('+')
         .click_button('8')
         .click_button('='))

        result = self.calculator_page.get_result()
        assert result == "15", f"Expected 15, but got {result}"