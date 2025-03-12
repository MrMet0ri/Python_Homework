from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = driver.find_element(By.ID, 'first-name')
        self.last_name_input = driver.find_element(By.ID, 'last-name')
        self.zip_code_input = driver.find_element(By.ID, 'postal-code')
        self.continue_button = driver.find_element(By.ID, 'continue')

    def fill_form_and_continue(self, first_name, last_name, zip_code):
        self.first_name_input.send_keys(first_name)
        self.last_name_input.send_keys(last_name)
        self.zip_code_input.send_keys(zip_code)
        self.continue_button.click()
