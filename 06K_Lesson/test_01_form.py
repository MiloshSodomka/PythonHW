from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_form_validation():

    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:

        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


        driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
        driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
        driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")

        driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
        driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
        driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")


        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))


        zip_code_field = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
        zip_code_parent = zip_code_field.find_element(By.XPATH, "./..")
        assert "alert-danger" in zip_code_parent.get_attribute("class")

        
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_name in fields_to_check:
            field = driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']")
            field_parent = field.find_element(By.XPATH, "./..")
            assert "alert-success" in field_parent.get_attribute("class")

    finally:
        driver.quit()