import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class UserLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_demo_user_valid_login(self):
        driver = self.driver
        driver.get('https://www.phptravels.net/login')
        
        # Enter email
        email = driver.find_element_by_name('username')
        email.send_keys("user@phptravels.com")
        
        #Enter password and hit enter
        password = driver.find_element_by_name('password')
        password.send_keys("demouser")
        password.send_keys(Keys.RETURN)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()