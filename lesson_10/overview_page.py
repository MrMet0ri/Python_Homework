import allure
from selenium.webdriver.common.by import By


class OverviewPage:
    def __init__(self, driver) -> None:
        """
        Инициализация страницы Overview.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Возвращает итоговую сумму заказа.

        :return: Итоговая сумма в виде строки.
        """
        total_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label'
        )
        return total_element.text
