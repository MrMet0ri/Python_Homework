from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def set_delay(self, delay: int) -> None:
        delay_input = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'delay'))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_text: str) -> None:
        button_locator = (
            By.XPATH, f"//span[normalize-space(text())='{button_text}']"
        )
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def get_result(self) -> str:
        result_display = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'screen'))
        )
        WebDriverWait(self.driver, 60).until(
            lambda driver: result_display.text.strip() not in ('', '7+8')
        )
        return result_display.text.strip()
