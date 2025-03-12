from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn-primary')]"
)
button.click()

wait = WebDriverWait(driver, 30)
message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)

print(message.text)

driver.quit()
