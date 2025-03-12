from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from overview_page import OverviewPage


def test_swag_labs():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.login('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Bolt T-Shirt')
    inventory_page.add_to_cart('Sauce Labs Onesie')

    driver.find_element(
        By.XPATH, "//a[@data-test='shopping-cart-link']"
    ).click()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form_and_continue(
        'Ваше имя', 'Ваша фамилия', 'Ваш индекс'
    )

    overview_page = OverviewPage(driver)
    total = overview_page.get_total()

    assert total == 'Total: $58.29'

    driver.quit()
