from selenium.webdriver.common.by import By
import allure


class CartPage:
    """Page Object для страницы корзины Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует страницу корзины.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа."""
        self.driver.find_element(*self.checkout_button).click()