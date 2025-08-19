from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()

try:
    alert = driver.switch_to.alert
    alert.accept()
except:
    pass

time.sleep(2)
driver.quit()