import pytest
from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.products_page import ProductsPage
from pages.saucedemo.cart_page import CartPage
from pages.saucedemo.checkout_page import CheckoutPage


class TestSauceDemo:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.products_page = ProductsPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)

    def test_checkout_total_amount(self):
        # Логин
        (self.login_page.open()
         .login("standard_user", "secret_sauce"))

        # Добавление товаров в корзину
        (self.products_page.add_product_to_cart('backpack')
         .add_product_to_cart('bolt_t_shirt')
         .add_product_to_cart('onesie')
         .go_to_cart())

        # Переход к оформлению заказа
        self.cart_page.click_checkout()

        # Заполнение информации
        (self.checkout_page.fill_checkout_info("John", "Doe", "12345")
         .click_finish())

        # Получение итоговой суммы
        total_amount = self.checkout_page.get_total_amount()

        assert total_amount == "58.29", f"Expected $58.29, but got ${total_amount}"