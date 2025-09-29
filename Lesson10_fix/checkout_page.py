from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует страницу оформления заказа.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить информацию о покупателе: {first_name} {last_name}, {postal_code}")
    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет информацию о покупателе.

        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> None:
        """Нажимает кнопку продолжения оформления заказа."""
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую сумму")
    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        Returns:
            str: Итоговая сумма
        """
        return self.driver.find_element(*self.total_label).text