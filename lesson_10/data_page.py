import allure
from selenium.webdriver.common.by import By
from base_page_lesson10 import BasePage


class DataPage(BasePage):
    # Локаторы элементов на странице
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

    @allure.step("Заполнить форму с данными")
    def fill_form(
        self, first_name: str, last_name: str, address: str,
        email: str, phone: str, city: str, country: str,
        job_position: str, company: str
    ) -> None:
        """
        Заполняет форму на странице введенными данными.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param address: Адрес.
        :param email: Электронная почта.
        :param phone: Телефон.
        :param city: Город.
        :param country: Страна.
        :param job_position: Должность.
        :param company: Компания.
        """
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.ADDRESS, address)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PHONE, phone)
        self.send_keys(self.CITY, city)
        self.send_keys(self.COUNTRY, country)
        self.send_keys(self.JOB_POSITION, job_position)
        self.send_keys(self.COMPANY, company)

    @allure.step("Отправить форму")
    def submit_form(self) -> None:
        """
        Нажимает на кнопку отправки формы.
        """
        self.click(self.SUBMIT_BUTTON)
