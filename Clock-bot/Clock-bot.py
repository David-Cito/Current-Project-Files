from selenium import webdriver
from time import sleep
""" import BotEngine """
from pathlib import Path, PureWindowsPath
from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
# Open the Website
browser.get('https://clients.mindbodyonline.com/LoginLaunch?studioid=173969')
sleep(3)
#Bypass Log in
browser.find_element_by_id('username').send_keys('davidcito')
browser.find_element_by_id('password').send_keys('Jwy2djwy2d')
browser.find_element_by_class_name('Button_button_YWMBp1OK04').click()
sleep(5)
#click buttons to clock in/out
browser.find_element_by_xpath("//span[@class='time-clock-icon icon']").click()
sleep(4)
clockTextElement = browser.find_element_by_xpath("//p[@id='clock-info']")
clockText = clockTextElement.text
clockButton = browser.find_element_by_id('clockIn')
if 'out' in clockText:
    print('currently clocked out')
    #Click clock in 
    #clockButton.click() 
else:
    print('Else was reached')
