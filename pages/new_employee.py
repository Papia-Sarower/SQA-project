from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class new_employee_page:
    def __init__(self, driver):
        self.driver = driver
        self.add_name=driver.find_element(By.XPATH, "//input[@name='fingerprint_no']").send_keys("1234567")
        self.add_password =driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Password123@")
        self.add_con_pass=driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys("Password123@")
        self.add_fullname=driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("John Doe")
        self.add_dob=driver.find_element(By.XPATH, "//input[@placeholder='Date of Birth']").send_keys("1990-01-01")
        self.add_emer_con=driver.find_element(By.XPATH, "//input[@placeholder='Emergency Contact No']").send_keys("01234567890")
        self.add_rel=driver.find_element(By.XPATH, "//input[@placeholder='Relation with Emergency Contact']").send_keys("Brother")
        self.add_per_phn=driver.find_element(By.XPATH, "//input[@placeholder='Phone (Personal)']").send_keys("09876543210")
        self.add_sal=driver.find_element(By.XPATH, "//input[@placeholder='Salary']").send_keys("50000")
        self.save_button=driver.find_element(By.ID, "saveButton").click()
    def open(self):
        self.driver.get("https://amaderit.net/demo/hr/employee")

    def click_add_name(self):
        self.driver.find_element(*self.add_name).send_keys("John Doe")

    def enter_pass(self, name):
        self.driver.find_element(*self.add_password).send_keys()

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def get_success_message(self):
        return self.driver.wait.until(EC.visibility_of_element_located(self.success_toast)).text
