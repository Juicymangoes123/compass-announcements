from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys
import time

username = sys.argv[1]
password = sys.argv[2]

# Open up the Compass page
driverOptions = Options()
driverOptions.add_argument('--headless')
driver = webdriver.Firefox(options=driverOptions)

driver.get('https://mhs-vic.compass.education/login.aspx?sessionstate=disabled')

# Get in with proper credentials
usernameField = driver.find_element_by_id('username')
usernameField.send_keys(username)
passwordField = driver.find_element_by_id('password')
passwordField.send_keys(password)
button = driver.find_element_by_id('button1')
time.sleep(1)
button.click()

element = EC.presence_of_element_located((By.CLASS_NAME, 'x-container x-box-item x-container-default x-box-layout-ct'))
WebDriverWait(driver, 10).until(element)
page = driver.page_source

# Convert page into beautiful soup
# soup = BeautifulSoup(page, features='html5lib')
