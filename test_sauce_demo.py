import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to read test data from CSV using Pandas
def read_test_data():
    data = pd.read_csv('test_data.csv')
    test_data = [(row['username'], row['password']) for index, row in data.iterrows()]
    return test_data

# Function to perform login using Selenium
def login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    
    # Find and fill in the username field
    username_field = driver.find_element(By.ID, "user-name")
    username_field.clear()
    username_field.send_keys(username)
    
    # Find and fill in the password field
    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys(password)
    
    # Click login button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(2)

    # Check if login was successful by checking for a logout button or inventory page
    if "inventory" in driver.current_url:
        print(f"Login successful for {username}")
    else:
        print(f"Login failed for {username}")

# Main function to run tests
def run_tests():
    driver = webdriver.Chrome()

    # Read test data
    test_data = read_test_data()

    # Loop through the test data and perform login for each
    for username, password in test_data:
        login(driver, username, password)
        time.sleep(3)  # Adding delay between logins

    driver.quit()

if __name__ == "__main__":
    run_tests()
