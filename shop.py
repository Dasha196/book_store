from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)

###### отображение страницы товара
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("tester@mail.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1!Qqaz2wsx")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# # shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# time.sleep(2)
# html_5_book = driver.find_element_by_css_selector(".post-181 h3")
# html_5_book.click()
# book_title = driver.find_element_by_class_name("entry-title")
# book_title_text = book_title.text
# assert book_title_text == "HTML5 Forms"


##### количество товаров в категории
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("tester@mail.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1!Qqaz2wsx")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# # shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# time.sleep(2)
# html = driver.find_element_by_link_text("HTML")
# html.click()
# time.sleep(2)
# items_count = driver.find_elements_by_class_name("type-product")
# assert len(items_count) == 3


###### сортировка товаров
# from selenium.webdriver.support.select import Select
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("tester@mail.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1!Qqaz2wsx")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# # shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# time.sleep(2)
# selector = driver.find_element_by_css_selector("[value='menu_order']")  # (".orderby>:nth-child(1)")
# selector_selected = selector.get_attribute("selected")
# print("value of selector: ", selector_selected)
# if selector_selected is not None:
#     print("Выбрана сортировка по умолчанию")
# else:
#     print("Не выбрана сортировка по умолчанию")
# selector_price = driver.find_element_by_class_name("orderby")
# select = Select(selector_price)
# select.select_by_index(5)
# time.sleep(2)
# selector = driver.find_element_by_css_selector("[value='price-desc']")
# selector_selected = selector.get_attribute("selected")
# print("value of selector: ", selector_selected)
# if selector_selected is not None:
#     print("Выбрана сортировка по цене от большей к меньшей")
# else:
#     print("Не выбрана сортировка по цене от большей к меньшей")
# time.sleep(2)


##### отображение, скидка товара
## логин
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login_email = driver.find_element_by_id("username")
# login_email.send_keys("tester@mail.ru")
# login_password = driver.find_element_by_id("password")
# login_password.send_keys("1!Qqaz2wsx")
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# ## переход на вкладку Shop
# shop_tab = driver.find_element_by_link_text("Shop")
# # shop_tab = driver.find_element_by_id("menu-item-40")
# shop_tab.click()
# ## открытие книги "Android Quick Start Guide"
# android_quick_start_book = driver.find_element_by_css_selector(".post-169 h3")
# # android_quick_start_book = driver.find_element_by_css_selector(".post-169 > a:nth-child(1)")
# # android_quick_start_book = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
# android_quick_start_book.click()
# ## получение значения новой и старой цены
# book_old_price = driver.find_element_by_css_selector(".price > del >span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins >span")
# book_new_price_text = book_new_price.text
# ## проверка значений цены
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# ## явное ожидание для обложки книги
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# ## явное ожидание для кнопки закрытия обложки книги в режиме предпросмотра
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()


##### проверка цены в корзине
# shop_tab = driver.find_element_by_link_text("Shop")
# shop_tab.click()
# add_to_basket = driver.find_element_by_css_selector(".post-182 .button")
# add_to_basket.click()
# time.sleep(2) # без этого не работает
# item_basket = driver.find_element_by_class_name("cartcontents")
# item_basket_text = item_basket.text
# assert item_basket_text == "1 Item"
# price_basket = driver.find_element_by_css_selector(".wpmenucart-contents :nth-child(3)")
# price_basket_text = price_basket.text
# assert price_basket_text == "₹180.00"
# time.sleep(2) # без этого не работает
# basket_btn = driver.find_element_by_id("wpmenucartli")
# basket_btn.click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>:nth-child(2)>:nth-child(1)"), "₹180.00"))
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td strong span"), "₹183.60"))


##### работа в корзине
# shop_tab = driver.find_element_by_link_text("Shop")
# shop_tab.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_to_basket_html_5 = driver.find_element_by_css_selector(".post-182 .button")
# add_to_basket_html_5.click()
# time.sleep(2) #обязательно
# add_to_basket_js_data = driver.find_element_by_css_selector(".post-180 .button")
# add_to_basket_js_data.click()
# basket_btn = driver.find_element_by_id("wpmenucartli")
# basket_btn.click()
# time.sleep(2) #обязательно
# delete_btn = driver.find_element_by_css_selector("[data-product_id='182']")
# delete_btn.click()
# delete_undo = driver.find_element_by_link_text("Undo?")
# delete_undo.click()
# time.sleep(2)
# quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity.clear()
# quantity.send_keys(3)
# time.sleep(2)
# update_basket = driver.find_element_by_name("update_cart")
# update_basket.click()
# quantity = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == '3'
# time.sleep(2) #обязательно
# apply_coupon = driver.find_element_by_name("apply_coupon")
# apply_coupon.click()
# time.sleep(2)
# message = driver.find_element_by_class_name("woocommerce-error")
# message_text = message.text
# assert message_text == "Please enter a coupon code."


##### покупка товара
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()
driver.execute_script("window.scrollBy(0, 300);")
add_to_basket_html_5 = driver.find_element_by_css_selector(".post-182 .button")
add_to_basket_html_5.click()
time.sleep(2)
basket_btn = driver.find_element_by_id("wpmenucartli")
basket_btn.click()
proceed_to_checkout = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
proceed_to_checkout.click()
first_name = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")) )
first_name.send_keys("Tester")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Tester")
email = driver.find_element_by_id("billing_email")
email.send_keys("tester@mail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("123456789")
time.sleep(2)
country_selector = driver.find_element_by_id("s2id_billing_country")
country_selector.click()
time.sleep(2)
country = driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
time.sleep(2)
country_russia = driver.find_element_by_class_name("select2-match")
country_russia.click()
time.sleep(2)
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Lenina")
city = driver.find_element_by_id("billing_city")
city.send_keys("Ekaterinburg")
time.sleep(2)
state = driver.find_element_by_id("billing_state")
state.send_keys("Sverdlovskaya")
city = driver.find_element_by_id("billing_postcode")
city.send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2) #обязательно
payments = driver.find_element_by_id("payment_method_cheque")
payments.click()
time.sleep(3)
place_order = driver.find_element_by_id("place_order")
place_order.click()
time.sleep(2)
text_thank_you= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
text_check_payments= WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))


driver.quit()