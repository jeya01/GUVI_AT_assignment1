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
emp_id = '0066'
edit_emp = driver.find_element(By.XPATH, "//div[@role='table']//div[contains(text()," + emp_id + ")]" \
                                                                                                 "/../following-sibling::div[7]/div/button[2]/i")
edit_emp.click()

ssn_no = driver.find_element(By.XPATH,"//label[text()='SSN Number']/../following-sibling::div/input")
ssn_no.send_keys("123")

sin_no = driver.find_element(By.XPATH,"//label[text()='SIN Number']/../following-sibling::div/input")
sin_no.send_keys("456")

save_button = driver.find_element(By.XPATH,"//div[@class='orangehrm-edit-employee']/div[2]/div[1]/form[@class='oxd-form']" \
                        "/div[@class='oxd-form-row']/../div[@class='oxd-form-actions']/button[@type='submit']")
save_button.click()

driver.quit()
