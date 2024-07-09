from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()

# Функция для клика на кнопку "Button with Dynamic ID"
push=1
driver.get("http://uitestingplayground.com/dynamicid")
driver2.get("http://uitestingplayground.com/dynamicid")

def click_element():
    blue_button = driver.find_element(By.CSS_SELECTOR,"[type=button].btn.btn-primary")
    blue_button.click()
    print("Fox", push)
    blue_button2 = driver2.find_element(By.CSS_SELECTOR,"[type=button].btn.btn-primary")
    blue_button2.click()
    print("Chrome", push) 

# Вызываем функцию три раза
for i in range(3):
    
    click_element()  
    push = push + 1

# Закрываем браузер
driver.quit()
driver2.quit()
