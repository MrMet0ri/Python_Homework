import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    ).text

    assert total_price == "Total: $58.29"


if __name__ == "__main__":
    pytest.main()
