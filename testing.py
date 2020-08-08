from time import sleep
 2 from selenium import webdriver
 3 
 4 browser = webdriver.Firefox()
 5 browser.implicitly_wait(5)
 6 
 7 browser.get('https://www.instagram.com/')
 8 
 9 login_link = browser.find_element_by_xpath("//a[text()='Log in']")
10 login_link.click()
11 
12 sleep(5)
13 
14 browser.close()


12 sleep(2)
13 
14 username_input = browser.find_element_by_css_selector("input[name='username']")
15 password_input = browser.find_element_by_css_selector("input[name='password']")
16 
17 username_input.send_keys("<your username>")
18 password_input.send_keys("<your password>")
19 
20 login_button = browser.find_element_by_xpath("//button[@type='submit']")
21 login_button.click()
22 
23 sleep(5)
24 
25 browser.close()


# def test_login_page(browser):
#     browser.get('https://www.instagram.com/accounts/login/')
#     username_input = browser.find_element_by_css_selector("input[name='username']")
#     password_input = browser.find_element_by_css_selector("input[name='password']")
#     username_input.send_keys("<your username>")
#     password_input.send_keys("<your password>")
#     login_button = browser.find_element_by_xpath("//button[@type='submit']")
#     login_button.click()

#     errors = browser.find_elements_by_css_selector('#error_message')
#     assert len(errors) == 0