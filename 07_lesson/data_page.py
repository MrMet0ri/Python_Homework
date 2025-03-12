from selenium.webdriver.common.by import By
from base_page import BasePage


class DataPage(BasePage):
    FIRST_NAME = (By.NAME, "first-name")
    LAST_NAME = (By.NAME, "last-name")
    ADDRESS = (By.NAME, "address")
    EMAIL = (By.NAME, "e-mail")
    PHONE = (By.NAME, "phone")
    ZIP_CODE = (By.NAME, "zip-code")
    CITY = (By.NAME, "city")
    COUNTRY = (By.NAME, "country")
    JOB_POSITION = (By.NAME, "job-position")
    COMPANY = (By.NAME, "company")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_form(self, first_name, last_name, address, email, phone, city,
                  country, job_position, company):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.ADDRESS, address)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PHONE, phone)
        self.send_keys(self.CITY, city)
        self.send_keys(self.COUNTRY, country)
        self.send_keys(self.JOB_POSITION, job_position)
        self.send_keys(self.COMPANY, company)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
