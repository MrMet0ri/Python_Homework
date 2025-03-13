import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page_lesson10 import LoginPage
from inventory_page_lesson10 import InventoryPage
from cart_page_lesson10 import CartPage
from checkout_page_lesson10 import CheckoutPage
from overview_page_lesson10 import OverviewPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации WebDriver.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест покупок на сайте SauceDemo")
@allure.description(
    "Этот тест проверяет процесс покупки товаров от авторизации "
    "до проверки итоговой суммы."
)
@allure.feature("SauceDemo Shop")
@allure.severity(allure.severity_level.CRITICAL)
def test_swag_labs(driver):
    """
    Тест покупки товаров на сайте SauceDemo с проверкой итоговой суммы.
    """
    with allure.step("Открытие главной страницы SauceDemo"):
        driver.get('https://www.saucedemo.com/')

    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.login(
            'standard_user', 'secret_sauce'
        )

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart('Sauce Labs Backpack')
        inventory_page.add_to_cart('Sauce Labs Bolt T-Shirt')
        inventory_page.add_to_cart('Sauce Labs Onesie')

    with allure.step("Открытие корзины"):
        driver.find_element(
            By.XPATH,
            "//a[@data-test='shopping-cart-link']"
        ).click()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form_and_continue(
            'Ваше имя',
            'Ваша фамилия',
            'Ваш индекс'
        )

    with allure.step("Получение итоговой суммы"):
        overview_page = OverviewPage(driver)
        total = overview_page.get_total()

    with allure.step("Проверка итоговой суммы заказа"):
        assert total == 'Total: $58.29', (
            f"Ожидалось: 'Total: $58.29', получено: {total}"
        )
