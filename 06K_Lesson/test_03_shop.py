from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_shopping_cart_total():

    driver = webdriver.Firefox()

    try:

        driver.get("https://www.saucedemo.com/")


        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()


        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()


        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


        driver.find_element(By.CSS_SELECTOR, "#checkout").click()


        driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
        driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
        driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")


        driver.find_element(By.CSS_SELECTOR, "#continue").click()


        total_element = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total_text = total_element.text


        assert total_text == "Total: $58.29"

    finally:
        driver.quit()