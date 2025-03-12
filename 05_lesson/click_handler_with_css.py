from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn-primary')]"
)
button.click()

driver.quit()
