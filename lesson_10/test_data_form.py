import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_page_lesson10 import DataPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации WebDriver.

    :return: Экземпляр WebDriver.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тест на заполнение формы и проверку валидации полей")
@allure.description(
    "Тест заполняет форму и проверяет валидацию полей на странице."
)
@allure.feature("Форма данных")
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_form(driver):
    """
    Тест заполняет форму на странице, отправляет ее и проверяет
    состояние полей.
    """
    page = DataPage(driver)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "data-types.html"
    )

    with allure.step("Ожидание появления поля 'First Name'"):
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        )

    with allure.step("Заполнение формы валидными данными"):
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

    with allure.step("Отправка формы"):
        page.submit_form()

    with allure.step("Ожидание появления валидации Zip Code"):
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "zip-code"))
        )

    with allure.step("Проверка валидации полей"):
        assert "alert-danger" in page.get_element_attribute(
            (By.ID, "zip-code"), "class"
        ), (
            "Поле 'Zip Code' не подсвечено красным."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "first-name"), "class"
        ), (
            "Поле 'First Name' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "last-name"), "class"
        ), (
            "Поле 'Last Name' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "address"), "class"
        ), (
            "Поле 'Address' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "e-mail"), "class"
        ), (
            "Поле 'Email' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "phone"), "class"
        ), (
            "Поле 'Phone' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "city"), "class"
        ), (
            "Поле 'City' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "country"), "class"
        ), (
            "Поле 'Country' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "job-position"), "class"
        ), (
            "Поле 'Job Position' не подсвечено зеленым."
        )

        assert "alert-success" in page.get_element_attribute(
            (By.ID, "company"), "class"
        ), (
            "Поле 'Company' не подсвечено зеленым."
        )
