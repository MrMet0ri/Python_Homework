import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver() -> WebDriver:
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver
    driver.quit()


def test_calculator(driver: WebDriver) -> None:
    calculator_page = CalculatorPage(driver)

    calculator_page.set_delay(45)
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')

    result = calculator_page.get_result()
    assert result == '15'
