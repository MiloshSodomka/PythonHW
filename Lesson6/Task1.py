from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_button():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/ajax")

        button = driver.find_element(By.ID, "ajaxButton")
        button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
        )


        print(success_message.text)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_ajax_button()