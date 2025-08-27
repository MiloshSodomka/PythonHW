from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_rename_button():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/textinput")

        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.clear()
        input_field.send_keys("SkyPro")

        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
        )

        button_text = button.text
        print(button_text)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_rename_button()