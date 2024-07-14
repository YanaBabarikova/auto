from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.CSS_SELECTOR, ("#ajaxButton")).click()
driver.implicitly_wait(20)
text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(text)

driver.quit()
