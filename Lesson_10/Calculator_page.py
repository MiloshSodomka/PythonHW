from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Page Object для страницы калькулятора."""

    def __init__(self, driver):
        """
        Инициализирует страницу калькулятора.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")

    @allure.step("Ввести задержку: {delay}")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает значение задержки в поле ввода.

        Args:
            delay: Значение задержки в секундах
        """
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step("Нажать кнопку: {button}")
    def click_button(self, button: str) -> None:
        """
        Нажимает указанную кнопку калькулятора.

        Args:
            button: Текст на кнопке (например, '7', '+', '=')
        """
        button_locator = (By.XPATH, f"//span[text()='{button}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """
        Получает текст из поля результата.

        Returns:
            str: Текст результата вычислений
        """
        return self.driver.find_element(*self.result_field).text

    @allure.step("Дождаться появления результата: {expected_result}")
    def wait_for_result(self, expected_result: str, timeout: int) -> None:
        """
        Ожидает появления ожидаемого результата.

        Args:
            expected_result: Ожидаемый результат
            timeout: Максимальное время ожидания в секундах
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.result_field, expected_result)
        )