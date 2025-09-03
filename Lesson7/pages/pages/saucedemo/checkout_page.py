from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Локаторы
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        return self

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
        return self

    def fill_checkout_info(self, first_name, last_name, postal_code):
        return (self.enter_first_name(first_name)
                .enter_last_name(last_name)
                .enter_postal_code(postal_code)
                .click_continue())

    def get_total_amount(self):
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.replace("Total: $", "")