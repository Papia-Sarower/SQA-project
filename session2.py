import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Fixture to initialize driver based on browser name
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_search(driver):
    # Step 1: Open Google
    driver.get("https://www.google.com")

    # Step 2: Locate search input using XPath
    search_input = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")

    # Step 3: Enter query and press Enter
    search_input.send_keys("pytest tutorial")
    search_input.send_keys(Keys.RETURN)

    # Print the page title to the console
    print("Page title is:", driver.title)

