from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

WebDriverWait(driver, 300).until(
    EC.presence_of_element_located((By.XPATH, "//p[text()='Done!']"))
)

WebDriverWait(driver, 300).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4
)

third_image = driver.find_elements(By.TAG_NAME, "img")[3]
src_value = third_image.get_attribute("src")

print(
    f"Значение атрибута src у 3-й картинки: {src_value}"
)

driver.quit()
