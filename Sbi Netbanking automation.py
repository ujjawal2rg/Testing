from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://retail.onlinesbi.com/retail/login.htm")
driver.implicitly_wait(15)
driver.maximize_window()
con=driver.find_element_by_class_name('continue_btn').click()
loginBox = driver.find_element_by_xpath('//*[@id="username"]')
loginBox.send_keys("userName")
loginBox = driver.find_element_by_xpath('//*[@id="label2"]')
loginBox.send_keys("passWorD")

time.sleep(20)
nextButton = driver.find_elements_by_xpath('//*[@id="Button2"]')
nextButton[0].click()
time.sleep(25)
nextButton = driver.find_elements_by_xpath('//*[@id="btContinue"]')
nextButton[0].click()
