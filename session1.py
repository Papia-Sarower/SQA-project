from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up the WebDriver
driver = webdriver.Chrome()


# Open Google
driver.get("https://www.google.com")

# Print the page title to the console
print("Page title is:", driver.title)

# Close the browser
driver.quit()