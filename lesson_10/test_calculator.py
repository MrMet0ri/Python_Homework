import pytest
import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page_lesson10 import CalculatorPage


@pytest.fixture
def driver() -> WebDriver:
    """
    Фикстура для инициализации и закрытия WebDriver.

    :return: Инициализированный WebDriver.
    """
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver
    driver.quit()


@allure.title("Тест калькулятора с задержкой")
@allure.description(
    "Этот тест проверяет работу калькулятора со сложением чисел "
    "после задержки."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver: WebDriver) -> None:
    """
    Тест проверки работы калькулятора при задержке.
    """
    calculator_page = CalculatorPage(driver)

    with allure.step("Установить задержку 45 секунд"):
        calculator_page.set_delay(45)

    with allure.step("Нажать на последовательность кнопок 7 + 8 ="):
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

    with allure.step("Проверить, что результат равен 15"):
        result = calculator_page.get_result()
        assert result == '15', (
            f"Ожидалось: 15, Получено: {result}"
        )
