# 2Captcha Extension Python

2Captcha Extension Python helps you easily use 2Captcha Extension in Botasaurus, Selenium, and Playwright.

You can easily configure 2Captcha with an API key without needing to download the 2Captcha Extension, update config files, etc.


## Installation

```bash 
python -m pip install twocaptcha_extension_python
```

## Usage with [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)

```python
from botasaurus import *
from twocaptcha_extension_python import TwoCaptcha

@browser(
    extensions=[TwoCaptcha(api_key="TWO_CAPTCHA_KEY")], # TODO: Replace with your own 2Captcha Key
)  
def solve_captcha(driver: AntiDetectDriver, data):
    driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    driver.prompt()

solve_captcha()
```

## Usage with Selenium 

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_autoinstaller import install
from twocaptcha_extension_python import TwoCaptcha

# Set Chrome options
options = Options()
options.add_argument(TwoCaptcha(api_key="TWO_CAPTCHA_KEY").load()) # TODO: Replace with your own 2Captcha Key
# Install and set up the driver
driver_path = install()
driver = webdriver.Chrome(driver_path, options=options)

# Navigate to the desired URL
driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")

# Prompt for user input
input("Press Enter to exit...")

# Clean up
driver.quit()
```

## Usage with Playwright

```python
from playwright.sync_api import sync_playwright
from twocaptcha_extension_python import TwoCaptcha
import random

def generate_random_profile():
    return str(random.randint(1, 1000))

with sync_playwright() as p:
    extension_path = TwoCaptcha(api_key="TWO_CAPTCHA_KEY").load(with_command_line_option=False) # TODO: Replace with your own 2Captcha Key
    browser = p.chromium.launch_persistent_context(
        user_data_dir=generate_random_profile(),
        headless=False,
        args=[
            '--disable-extensions-except='+ extension_path,
            '--load-extension=' + extension_path,
        ],
    )
    page = browser.new_page()
    page.goto("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    input("Press Enter to exit...")
    browser.close()
```

## Love It? [Star It ⭐!](https://github.com/omkarcloud/twocaptcha-extension-python)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

[![Stargazers for @omkarcloud/twocaptcha-extension-python](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=omkarcloud&repo=twocaptcha-extension-python)](https://github.com/omkarcloud/twocaptcha-extension-python/stargazers)
