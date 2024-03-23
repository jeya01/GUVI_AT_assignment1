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
login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()
pim = driver.find_element(By.XPATH, "//span[text()='PIM']")
pim.click()
add_emp = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
add_emp.click()
firstname = driver.find_element(By.XPATH,"//input[@name='firstName']")
lastname = driver.find_element(By.XPATH, "//input[@name='lastName']")
firstname.send_keys("David")
lastname.send_keys("Meier")
save = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
save.click()
time.sleep(5)


driver.quit()