from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)

##### регистрация аккаунта
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# time.sleep(2)
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("tester@mail.ru")
# time.sleep(2)
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("1!Qqaz2wsx")
# time.sleep(2)
# register = driver.find_element_by_css_selector("[name='register']")
# register.click()

###### логин в систему
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
time.sleep(2)
login_email = driver.find_element_by_id("username")
login_email.send_keys("tester@mail.ru")
login_password = driver.find_element_by_id("password")
login_password.send_keys("1!Qqaz2wsx")
login_btn = driver.find_element_by_name("login") # css_selector("[name='login']")
login_btn.click()
time.sleep(2)
element = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout")
element_text = element.text
assert element_text == "Logout"


driver.quit()