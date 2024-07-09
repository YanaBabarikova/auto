import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver2.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Функция для клика на кнопку "Add Element"
def click_add_element():
    add_element_btn = driver.find_element(By.CSS_SELECTOR, ".example button")
    add_element_btn.click()
    add_element_btn2 = driver2.find_element(By.CSS_SELECTOR, ".example button")
    add_element_btn2.click()
# Вызываем функцию пять раз
for i in range(5):
    click_add_element()
    time.sleep(1)  # Добавляем задержку, чтобы страница успела обновиться

# Вывести длинну списка delete
driver.find_elements(By.CSS_SELECTOR, "[class=added-manually]")
delete = driver.find_elements(By.CSS_SELECTOR, "[class=added-manually]")
print("Chrome:", len(delete)) 
driver2.find_elements(By.CSS_SELECTOR, "[class=added-manually]")
delete2 = driver2.find_elements(By.CSS_SELECTOR, "[class=added-manually]")
print("Fox:", len(delete)) 
# Закрываем браузер
driver.quit()
driver2.quit()