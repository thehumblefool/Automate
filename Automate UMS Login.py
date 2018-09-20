'''
This script is used to automate the 
Lovely Professional University's UMS Login.

Requirements
* Python 2.7 and above
* Selenium
* Chrome web driver

'''

from selenium import webdriver

#Enter your Registration Number
userRegNo = ''

#Enter your Password here
userPassword = ''


browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get("https://ums.lpu.in/lpuums/")

regNo = browser.find_element_by_id('txtU')
regNo.send_keys(userRegNo)

password = browser.find_element_by_id('Txtpw')
password.send_keys(' ')

select=' '
while select!=' ':
    try:
        select = browser.find_element_by_id('ddlStartWith')
    except:
        print('Waiting for other fields to load')

password = browser.find_element_by_id('Txtpw')
password.send_keys(userPassword)

login = browser.find_element_by_id('iBtnLogins')
login.click()

home=browser.find_element_by_id('ums')
home.click();