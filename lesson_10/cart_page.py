import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver
        self.checkout_button = driver.find_element(
            By.XPATH, "//button[@data-test='checkout']"
        )

    @allure.step("Нажать на кнопку Checkout")
    def click_checkout(self) -> None:
        """
        Нажимает на кнопку оформления заказа.
        """
        self.checkout_button.click()
