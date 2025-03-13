import allure
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver) -> None:
        """
        Инициализация страницы входа.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver
        self.username_input = driver.find_element(By.ID, 'user-name')
        self.password_input = driver.find_element(By.ID, 'password')
        self.login_button = driver.find_element(By.ID, 'login-button')

    @allure.step("Выполнить вход с именем пользователя: {username} и паролем")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему, вводя имя пользователя и пароль.

        :param username: Имя пользователя.
        :param password: Пароль.
        """
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
