from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            '0': (By.XPATH, "//span[text()='0']"),
            '1': (By.XPATH, "//span[text()='1']"),
            '2': (By.XPATH, "//span[text()='2']"),
            '3': (By.XPATH, "//span[text()='3']"),
            '4': (By.XPATH, "//span[text()='4']"),
            '5': (By.XPATH, "//span[text()='5']"),
            '6': (By.XPATH, "//span[text()='6']"),
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '9': (By.XPATH, "//span[text()='9']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '-': (By.XPATH, "//span[text()='-']"),
            '*': (By.XPATH, "//span[text()='×']"),
            '/': (By.XPATH, "//span[text()='÷']"),
            '=': (By.XPATH, "//span[text()='=']"),
            'C': (By.XPATH, "//span[text()='C']")
        }

    def open(self):
        self.driver.get(self.url)
        return self

    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(*self.delay_input)
        delay_input.clear()
        delay_input.send_keys(str(delay_value))
        return self

    def click_button(self, button):
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()
        return self

    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: driver.find_element(*self.result_display).text != "")
        return self.driver.find_element(*self.result_display).text