# test_division_create.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E
def test_division_create(driver):
    # Test case for creating a new division in AmaderHR.

    # Navigate to the Division page
    driver.get("https://amaderit.net/demo/hr/division")

    # Click the 'Add Division' button
    add_division_button = driver.find_element(By.XPATH, "//a[normalize-space()='Add Division']")
    add_division_button.click()

    # Enter division name
    division_name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter division name here']")
    division_name_input.send_keys("TEST DIVISION3")

    # Click the 'Save' button
    save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    save_button.click()

    # Wait for the success toast and assert message
    success_toast = driver.wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='toast toast-success']"))
    )
    assert "Division Created Successfully" in success_toast.text
