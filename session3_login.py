import time
from selenium.webdriver.common.by import By

def test_login_to_ems(driver):
    driver.get("https://ems-test.amaderit.net/")
    time.sleep(2)  # Let the page load;

    # Input credentials
    driver.find_element(By.ID, "username").send_keys("adming1")
    driver.find_element(By.ID, "password").send_keys("123456")

    # Click login
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()
    time.sleep(3)  # Wait for login to complete

    # Check if login is successful
    assert "EMS : Administer/Dashboard" in driver.title, "Login failed or URL not as expected"