from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = driver.find_element(
            By.XPATH, "//button[@data-test='checkout']"
        )

    def click_checkout(self):
        self.checkout_button.click()
