from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait_for_images():
    driver = webdriver.Chrome()
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )

        third_image = driver.find_element(By.ID, "image3")

        src_attribute = third_image.get_attribute("src")

        print(src_attribute)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_wait_for_images()