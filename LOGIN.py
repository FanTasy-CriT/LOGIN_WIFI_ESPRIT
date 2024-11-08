import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Load the environment variables from the DETAILS.env file
load_dotenv('DETAILS.env')

# Retrieve values from the DETAILS.env file
username = os.getenv('username1')
password = os.getenv('password1')
firefox_binary_path = os.getenv('firefox_path')


# Get the directory of the current script and specify geckodriver path
script_dir = os.path.dirname(os.path.abspath(__file__))
gecko_path = os.path.join(script_dir, 'geckodriver.exe')

# Set up Firefox options with the binary location
options = Options()
options.binary_location = firefox_binary_path

# Use Service to pass the geckodriver path
service = Service(gecko_path)
driver = webdriver.Firefox(service=service, options=options)

# Open the redirect URL
driver.get("http://www.msftconnecttest.com/redirect")

# Wait for the login page to load by waiting for the username field to be present
try:
    # Set a maximum wait time (e.g., 10 seconds) for the element to be located
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Perform login actions once the page is fully loaded
    driver.find_element(By.NAME, "username").send_keys(username)
    # Enter password and press Enter to submit
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password + Keys.RETURN)

finally:
    time.sleep(1)  # Optional: Short pause to confirm login before quitting
    driver.quit()
