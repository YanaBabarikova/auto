from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

try:
    search_input = driver.find_element(By.CSS_SELECTOR, ("#newButtonName"))
    search_input.send_keys("SkyPro")
    blue_button = driver.find_element(By.CSS_SELECTOR, ("#updatingButton")).click()
    driver.implicitly_wait(20)
    text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(text)

except Exception as ex:
    print(ex)

finally:
    driver.quit()
