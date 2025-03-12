import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_page import DataPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_fill_form(driver):
    page = DataPage(driver)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )

    page.submit_form()

    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )

    assert "alert-danger" in page.get_element_attribute(
        (By.ID, "zip-code"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "first-name"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "last-name"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "address"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "e-mail"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "phone"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "city"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "country"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "job-position"), "class"
    )
    assert "alert-success" in page.get_element_attribute(
        (By.ID, "company"), "class"
    )
