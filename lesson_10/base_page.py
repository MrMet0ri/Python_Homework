import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver) -> None:
        """
        Инициализация базовой страницы.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    @allure.step("Найти элемент с локатором: {locator}")
    def find_element(self, locator, time=10):
        """
        Поиск элемента на странице.

        :param locator: Локатор элемента (например, (By.ID, 'element_id')).
        :param time: Время ожидания элемента в секундах (по умолчанию 10).
        :return: Веб-элемент, если он найден.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент с локатором: {locator}")
    def click(self, locator) -> None:
        """
        Нажатие на элемент.

        :param locator: Локатор элемента (например, (By.ID, 'button_id')).
        """
        self.find_element(locator).click()

    @allure.step("Ввести текст '{text}' в элемент с локатором: {locator}")
    def send_keys(self, locator, text: str) -> None:
        """
        Ввод текста в элемент.

        :param locator: Локатор элемента (например, (By.ID, 'input_id')).
        :param text: Текст для ввода.
        """
        self.find_element(locator).send_keys(text)

    @allure.step(
        "Получить значение атрибута '{attribute}' элемента "
        "с локатором: {locator}"
    )
    def get_element_attribute(self, locator, attribute: str) -> str:
        """
        Получение значения атрибута элемента.

        :param locator: Локатор элемента (например, (By.ID, 'element_id')).
        :param attribute: Имя атрибута (например, 'value' или 'class').
        :return: Значение атрибута элемента.
        """
        return self.find_element(locator).get_attribute(attribute)
