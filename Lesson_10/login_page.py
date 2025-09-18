from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """Page Object для страницы авторизации Saucedemo."""

    def __init__(self, driver):
        """
        Инициализирует страницу авторизации.

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввести логин: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        Args:
            username: Имя пользователя
        """
        self.driver.find_element(*self.username_input).send_keys(username)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        Args:
            password: Пароль пользователя
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> None:
        """Нажимает кнопку входа."""
        self.driver.find_element(*self.login_button).click()

    @allure.step("Выполнить авторизацию с логином: {username} и паролем: {password}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет полный процесс авторизации.

        Args:
            username: Имя пользователя
            password: Пароль пользователя
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()