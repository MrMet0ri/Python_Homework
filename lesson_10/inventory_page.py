import allure
from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver) -> None:
        """
        Инициализация страницы списка товаров.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """
        Добавляет указанный товар в корзину.

        :param item_name: Название товара для добавления.
        """
        item_test_attr = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": (
                "add-to-cart-sauce-labs-bolt-t-shirt"
            ),
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }

        if item_name not in item_test_attr:
            raise ValueError(
                f"Товар '{item_name}' не найден в списке доступных товаров."
            )

        item = self.driver.find_element(
            By.XPATH,
            f"//button[@data-test='{item_test_attr[item_name]}']"
        )
        item.click()
