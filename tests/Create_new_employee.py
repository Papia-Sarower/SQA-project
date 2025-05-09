from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Wait for the login page to load

    def test_login_to_ems(driver):
        driver.get("https://ems-test.amaderit.net/")
        time.sleep(2)  # Let the page load;

        # Input credentials
        driver.find_element(By.ID, "username").send_keys("adming1")
        driver.find_element(By.ID, "password").send_keys("123456")

        # Click login
        driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
        time.sleep(3)  # Wait for login to complete


    # Step 1.1: Verify login success by checking the dashboard URL
    try:
        WebDriverWait(driver, 20).until(EC.url_contains("/dashboard"))
        print("Logged in successfully.")
    except:
        print("Login failed: Dashboard not loaded.")
        driver.quit()
        exit()

    # Step 2: Navigate to Employee Management
    driver.find_element(By.XPATH, "//div[@data-original-title='Employee']//a[@class='btn btn-icon btn-bg-primary btn-hover-white btn-hover-icon-primary btn-circle']").click()

    # Step 3: Click on 'Add Employee'
    add_employee_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='navi-text'][normalize-space()='Employee']"))
    )
    add_employee_button.click()
    add_employee_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary font-weight-bolder']"))
    )
    add_employee_button.click()

    # Step 4: Fill out the form using XPath
    driver.find_element(By.XPATH, "//input[@name='fingerprint_no']").send_keys("1234567")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Password123@")
    driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("Password123@")
    driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("John Doe")
    driver.find_element(By.XPATH, "//input[@placeholder='Date of Birth']").send_keys("1990-01-01")
    driver.find_element(By.XPATH, "//input[@placeholder='Emergency Contact No']").send_keys("01234567890")
    driver.find_element(By.XPATH, "//input[@placeholder='Relation with Emergency Contact']").send_keys("Brother")
    driver.find_element(By.XPATH, "//input[@placeholder='Phone (Personal)']").send_keys("09876543210")
    driver.find_element(By.XPATH, "//input[@placeholder='Salary']").send_keys("50000")
    driver.find_element(By.ID, "saveButton").click()

    # Step 5: Verify the success message and database update
    success_message = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    if "Employee added successfully" in success_message.text:
        print("Test Passed: Employee creation successful.")
    else:
        print("Test Failed: Success message not displayed.")

finally:
    # Close the browser
    time.sleep(2)
    driver.quit()
