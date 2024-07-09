import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
try:
    driver.get("https://the-internet.herokuapp.com/inputs")
    driver2.get("https://the-internet.herokuapp.com/inputs")
#Для Chrome
    search_input = driver.find_element(By.TAG_NAME, ("input"))
    search_input.send_keys("1000")
    time.sleep(2)
    search_input.clear()
    time.sleep(1)
    search_input.send_keys("999")
    time.sleep(2)
#Для Firefox
    search_input = driver2.find_element(By.TAG_NAME, ("input"))
    search_input.send_keys("1000")
    time.sleep(2)
    search_input.clear()
    time.sleep(1)
    search_input.send_keys("999")
    time.sleep(2)

finally:
    driver.quit()
    driver2.quit()