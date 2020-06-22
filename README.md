# Installation

## Install Selenium library

1. Method I: Open Terminal/cmd and enter command as:

```python -m pip install selenium```

2. Method II: You can download the source distribution [here](https://pypi.org/project/selenium/), unarchive it, and run the command below:

```python setup.py install```

## Install Webdrivers
### Download Chomedriver to drive Chrome or Chromium
Go to [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads). Find the latest version of the driver for your platform and download it.

In Linux:
- Extract the file
- Make it executable
```chmod +x chromedriver_linux64.zip```
- Move file to usr/local/bin
```sudo mv chromedriver_linux64.zip /usr/local/bin```

### Download geckodriver to drive Firefox 
It works with Firefox 48 and newer.


In Linux:

- Go to [Geckodriver Downloads](https://github.com/mozilla/geckodriver). Find the latest version of the driver for your platform and download it.
- Extract the file with:
```tar -xvzf geckodriver*```
- Make it executable:
```chmod +x geckodriver```
- Move file to usr/local/bin
```sudo mv geckodriver /usr/local/bin/```

In Windows:
- Download the GeckoDriver
- Extract it using WinRar or any application you may have.
- Add it to Path using Command Prompt
```setx path "%path%;GeckoDriver Path"```

For Example:-

```setx path "%path%;c:/user/Nischal/Desktop/geckodriver-v0.26.0-win64/geckodriver.exe"```

### [Other driver requirements](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)

Once, the webdrivers are installed, you can run the tests in browsers (Chrome, Chromium and Firefox).

# Getting Started
## Using Selenium to write tests
1. Create a test file "firstTest.py"
2. Add the following code in the file

```python
from selenium import webdriver 

#driver = webdriver.Firefox()
driver = webdriver.Chrome() 
driver.get("https://www.lftechnology.com/") 
```
3. Run the test file
```python firstTest.py```

Leapfrog homepage should open in Chrome browser. 
## Updating the test
Example: Login in phpTravels demo app

```python

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
```
## Organizing the test

1. Importing basic modules
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```
- 'unittest' module is a built-in Python based on Java's JUnit. It provides the frameworkfor organizing the test cases.
- The 'selenium.webdriver' module provides all the Webdriver implementation.
- The 'Keys' class provide keys in the keyboard like RETURN, F1, ALT etc.

2. ```class PythonOrgSearch(unittest.TestCase):```
- The test case class is inherited from 'unittest.TestCase'. It is the way to tell 'unittest' module that this is a test case.

3. Initialization
```python
    def setUp(self):
        self.driver = webdriver.Firefox()
```
- The setUp is the part of initialization. It will be called before every test function which we are going write in the test case class. Here we are creating the instance of Forefox Webdriver.

4. Test Case
```python
def test_demo_user_login(self):
driver = self.driver    
```
- This is the test case method. The first line inside this method createa a local reference to the driver object created in 'setUp' method.
Note: It should always start with characters 'test'.

5. Test steps:
- Go to login form
- Enter username
- Enter password ahd hit enter
- Close the browser after successful login

6. Teardown method
```python
def tearDown(self):
self.driver.close()
```
- The tearDown method will get called after every test method. In the current method, the browser window is closed.
-  The quit will exit the entire browser, whereas close will close a tab, but if it is the only tab opened, by default most browser will exit entirely.:

```python
if __name__ == "__main__":
    unittest.main()
```
These are some boiler plate code to run the test suite.

# Navigating
1. Interacting with the page
2. Filling in the forms
3. Drag and Drop
4. Moving between the windows and frames
5. Popup dialogs
6. Navigation: history and location

# Locating Elements
1. Locating by Id
2. Locating by Name
3. Locating by XPath
4. Locating Hyperlinks by Link Text
5. Locating Elements by Tag Name
6. Locating Elements by Class Name
7. Locating Elements by CSS Selectors

# Waits
1. Explicit Waits
2. Implicit Waits
