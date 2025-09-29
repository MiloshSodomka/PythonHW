import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации и закрытия браузера.

    Yields:
        WebDriver instance
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении тестов.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            if "browser" in item.funcargs:
                browser = item.funcargs["browser"]
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception as e:
            print(f"Не удалось сделать скриншот: {e}")