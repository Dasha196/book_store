from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)

####### добавление комментария
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
selenium = driver.find_element_by_css_selector(".post-160>:nth-child(1)")
selenium.click()
reviews_btn = driver.find_element_by_class_name("reviews_tab")
reviews_btn.click()
time.sleep(2)
stars = driver.find_element_by_css_selector(".stars :nth-child(5)")
stars.click()
time.sleep(2)
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Tester")
email = driver.find_element_by_id("email")
email.send_keys("tester@mail.ru")
time.sleep(2)
submit = driver.find_element_by_class_name("submit")
submit.click()

driver.quit()