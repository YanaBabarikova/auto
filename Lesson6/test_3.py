from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 20) 
waiter.until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#text"), "Done!"))
print( driver.find_element(By.CSS_SELECTOR, "#text").text )

element = driver.find_element(By.CSS_SELECTOR, "#award").tag_name #поиск элемента
print(element)

driver.quit()