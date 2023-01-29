import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
username = driver.find_element(By.XPATH, "//input[@name='username']")
password = driver.find_element(By.XPATH, "//input[@name='password']")
username.send_keys("Admin")
password.send_keys("admin1234")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
error_message = driver.find_element(By.XPATH, "//p[text()='Invalid credentials']")
print("Invalid Login:", error_message.text)
driver.quit()