import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements import RegistrationFormElements

# Open the Registration form in Google Chrome browser
class RegisterChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://signup.com/Register')

        # Wait until the field is visible
        timeout = 15
        try:
            element_present = EC.presence_of_element_located((By.NAME, 'firstName'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timeout, page didn't load within 15 seconds")

    def test_r4(self):
        # Execute the test case r4:
        # Fill the fields. Enter less than 6 characters in Password field and click Continue

        # Fill the fields
        self.driver.find_element(*RegistrationFormElements.first_name).send_keys('test')
        self.driver.find_element(*RegistrationFormElements.last_name).send_keys('test')
        self.driver.find_element(*RegistrationFormElements.email).send_keys('signtest@getnada.com')
        self.driver.find_element(*RegistrationFormElements.password).send_keys('test')

        # Click Continue button
        self.driver.find_element(*RegistrationFormElements.button).click()

        # Wait until the error is displayed and check assertion
        timeout = 15
        try:
            element_present = EC.presence_of_element_located(
                ((By.XPATH, '//*[text()="Passwords must be at least 6 characters long."]')))
            WebDriverWait(self.driver, timeout).until(element_present)
            print("OK, the correct error appeared: 'Passwords must be at least 6 characters long.'")
        except TimeoutException:
            print("Something went wrong. There's no error 'Passwords must be at least 6 characters long.' after clicking the Continue button")
            self.driver.save_screenshot('R1_no_valid_error.png')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()