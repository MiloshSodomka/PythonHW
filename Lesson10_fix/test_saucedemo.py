import pytest
import allure
from Lesson_10_fix.pages.login_page import LoginPage
from Lesson_10_fix.pages.products_page import ProductsPage
from Lesson_10_fix.pages.cart_page import CartPage
from Lesson_10_fix.pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestSauceDemo:
    """Тесты для функциональности интернет-магазина Saucedemo."""

    @allure.title("Проверка оформления заказа")
    @allure.description("Тест проверяет процесс оформления заказа с несколькими товарами")
    def test_checkout_process(self, browser):
        """
        Проверяет процесс оформления заказа в интернет-магазине.

        Steps:
        1. Авторизоваться как standard_user
        2. Добавить три товара в корзину
        3. Перейти в корзину и оформить заказ
        4. Заполнить информацию о покупателе
        5. Проверить итоговую сумму
        """
        with allure.step("Открыть сайт магазина и авторизоваться"):
            browser.get("https://www.saucedemo.com/")
            login_page = LoginPage(browser)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            products_page = ProductsPage(browser)
            products_page.add_product_to_cart("Sauce Labs Backpack")
            products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
            products_page.add_product_to_cart("Sauce Labs Onesie")

        with allure.step("Перейти в корзину и начать оформление заказа"):
            products_page.go_to_cart()
            cart_page = CartPage(browser)
            cart_page.click_checkout()

        with allure.step("Заполнить информацию о покупателе"):
            checkout_page = CheckoutPage(browser)
            checkout_page.fill_customer_info("Иван", "Иванов", "123456")
            checkout_page.click_continue()

        with allure.step("Проверить итоговую сумму"):
            total_amount = checkout_page.get_total_amount()

            with allure.step(f"Проверить, что итоговая сумма равна '$58.29', получена: '{total_amount}'"):
                assert total_amount == "Total: $58.29", f"Ожидалась сумма '$58.29', но получена '{total_amount}'"