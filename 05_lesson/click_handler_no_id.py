from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com/page")

button = driver.find_element(
    By.XPATH, "//button[@class='example-button']"
)
button.click()

driver.quit()
