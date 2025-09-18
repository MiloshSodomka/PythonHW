import pytest
import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для функциональности калькулятора."""

    @allure.title("Проверка вычислений с задержкой")
    @allure.description("Тест проверяет работу калькулятора с установленной задержкой 45 секунд")
    def test_calculator_with_delay(self, browser):
        """
        Проверяет работу калькулятора с установленной задержкой.

        Steps:
        1. Открыть страницу калькулятора
        2. Установить задержку 45 секунд
        3. Выполнить вычисление 7 + 8
        4. Проверить, что результат равен 15 после 45 секунд
        """
        with allure.step("Открыть страницу калькулятора"):
            browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
            calculator_page = CalculatorPage(browser)

        with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Выполнить вычисление 7 + 8"):
            calculator_page.click_button("7")
            calculator_page.click_button("+")
            calculator_page.click_button("8")
            calculator_page.click_button("=")

        with allure.step("Дождаться результата и проверить его"):
            calculator_page.wait_for_result("15", 50)
            result = calculator_page.get_result()

            with allure.step(f"Проверить, что результат равен '15', получен: '{result}'"):
                assert result == "15", f"Ожидался результат '15', но получен '{result}'"