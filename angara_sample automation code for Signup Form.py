from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.angara.in/customer/account/create/")
driver.implicitly_wait(15)
driver.maximize_window()

firstname = driver.find_element_by_xpath('//*[@id="firstname"]')
firstname.send_keys("userName")
lastname= driver.find_element_by_xpath('//*[@id="lastname"]')
lastname.send_keys("LastName")
email= driver.find_element_by_xpath('//*[@id="email_address"]')
email.send_keys("email@xyz.com")
password= driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Asl@1234")
cpassword= driver.find_element_by_xpath('//*[@id="confirmation"]')
cpassword.send_keys("Asl@1234")
nextButton = driver.find_elements_by_xpath('//*[@id="form-validate"]/div[3]/button')
nextButton[0].click()



