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
password.send_keys("admin123")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
pim = driver.find_element(By.XPATH, "//span[text()='PIM']")
pim.click()
emp_id = '0099'
delete_emp = driver.find_element(By.XPATH, "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                                                 "/../following-sibling::div[7]/div/button[1]/i")
delete_emp.click()

time.sleep(10)
delete_confirm = driver.find_element(By.XPATH,"//div[@role='document']/div[3]/button[2]/i")
delete_confirm.click()
time.sleep(5)
driver.quit()
