import allure
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver) -> None:
        """
        Инициализация страницы Checkout.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver
        self.first_name_input = driver.find_element(
            By.ID, 'first-name'
        )
        self.last_name_input = driver.find_element(
            By.ID, 'last-name'
        )
        self.zip_code_input = driver.find_element(
            By.ID, 'postal-code'
        )
        self.continue_button = driver.find_element(
            By.ID, 'continue'
        )

    @allure.step(
        "Заполнить форму Checkout: {first_name}, {last_name}, {zip_code}"
    )
    def fill_form_and_continue(
        self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        """
        Заполняет форму на странице Checkout и нажимает на кнопку Continue.

        :param first_name: Имя пользователя.
        :param last_name: Фамилия пользователя.
        :param zip_code: Почтовый индекс.
        """
        self.first_name_input.send_keys(first_name)
        self.last_name_input.send_keys(last_name)
        self.zip_code_input.send_keys(zip_code)
        self.continue_button.click()
