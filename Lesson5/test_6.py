import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
try:
    driver.get("https://the-internet.herokuapp.com/login")
    driver2.get("https://the-internet.herokuapp.com/login")
    login = driver.find_element(By.ID, ("username")).send_keys("tomsmith")
    login = driver2.find_element(By.ID, ("username")).send_keys("tomsmith")
    time.sleep(2)
    passw = driver.find_element(By.ID, ("password")).send_keys("SuperSecretPassword!")
    passw = driver2.find_element(By.ID, ("password")).send_keys("SuperSecretPassword!")
    time.sleep(2)
    button = driver.find_element(By.TAG_NAME, "button").click()
    button = driver2.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)

finally:
    driver.quit()
    driver2.quit()