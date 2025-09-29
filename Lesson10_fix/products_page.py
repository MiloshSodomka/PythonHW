from selenium.webdriver.common.by import By
import allure


class ProductsPage:
    """Page Object для страницы товаров Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует страницу товаров.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар в корзину: {product_name}")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        Args:
            product_name: Название товара
        """
        add_button_locator = (By.XPATH,
                              f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.driver.find_element(*add_button_locator).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        self.driver.find_element(*self.cart_button).click()