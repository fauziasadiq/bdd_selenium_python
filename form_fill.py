from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open URL
    driver.get("https://practice-automation.com/form-fields/")

    wait = WebDriverWait(driver, 10)

    # Fill Name
    name = wait.until(EC.visibility_of_element_located((By.ID, "name-input")))
    name.send_keys("Fauzia Sadiq")

    # Fill Password
    password = driver.find_element(By.XPATH,'//*[@id="feedbackForm"]/label[2]/input')
    password.send_keys("Test@123")

    # Fill Email
    email = driver.find_element(By.ID, "email")
    email.send_keys("test@example.com")

    # Select Radio Button (Favorite Drink - Milk)
    milk_radio = driver.find_element(By.ID, "drink2")
    milk_radio.click()

    # Select Checkboxes (Favorite Color - Red & Yellow)
    red_checkbox = driver.find_element(By.ID, "color1")
    yellow_checkbox = driver.find_element(By.ID, "color3")
    red_checkbox.click()
    yellow_checkbox.click()

    # Select Dropdown (Automation Experience)
    experience_dropdown = Select(driver.find_element(By.ID, "automation"))
    experience_dropdown.select_by_visible_text("Yes")

    # Enter Message
    message = driver.find_element(By.ID, "message")
    message.send_keys("This is an automated Selenium test.")

    # Submit Form
    submit_button = driver.find_element(By.ID, 'confirm')
    submit_button.click()

    driver.switch_to.alert.accept()

    # Get alert text

    # Accept the alert

    # Wait for confirmation
    time.sleep(3)

finally:
    driver.quit()
