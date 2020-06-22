
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

# Select the browser to run the tests
#driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Go to phptrabel login page
driver.get('https://www.phptravels.net/login')

#Enter Email
email = driver.find_element_by_name('username')
email.send_keys("user@phptravels.com")

#Enter Password
password = driver.find_element_by_name('password')
password.send_keys("demouser")

#Hit enter 
password.send_keys(Keys.RETURN)

driver.close()

