import time
from selenium import webdriver

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver2= webdriver.Firefox()

# Функция для клика на кнопку "Button"
try:
    driver.get("http://uitestingplayground.com/classattr")
    driver2.get("http://uitestingplayground.com/classattr")

# Вызываем функцию три раза
    for i in range(3):
        blue_button = driver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        print("finish Chrome")
        time.sleep(1)  # Добавляем задержку, чтобы страница успела обновиться
        blue_button = driver2.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        print("finish Fox")
        time.sleep(1)  # Добавляем задержку, чтобы страница успела обновиться
# Клик на ок
        driver.switch_to.alert.accept()
        driver2.switch_to.alert.accept()
except Exception as ex:
    print(ex)

# Закрываем браузер
finally:
    driver.quit()
    driver2.quit()
