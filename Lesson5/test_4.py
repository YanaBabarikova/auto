import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/entry_ad")
driver2.get("https://the-internet.herokuapp.com/entry_ad")
time.sleep(2)
# Функция для клика на кнопку "Close"
blue_button = driver.find_element(By.CSS_SELECTOR, (".modal-footer")).click()
print("finish Chrome")
blue_button = driver2.find_element(By.CSS_SELECTOR, (".modal-footer")).click()
print("finish Fox")

time.sleep(1)  # Добавляем задержку, чтобы страница успела обновиться

# Закрываем браузер
driver.quit()
driver2.quit()
