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
1. Create a test file "firsttest.py"
2. Add the following code in the file

```from selenium import webdriver 

#driver = webdriver.Firefox()
driver = webdriver.Chrome() 
driver.get("https://google.co.in") 
```
3. Run the test file
```python firsttest.py```

2. Walk through of the example

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
