import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from elements import RegistrationFormElements
from error_massages import ErrorMassages


# Open the Registration form in Google Chrome browser
class RegisterChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://signup.com/Register')

        # Set up the waiting time for page to load. Wait
        ts = int(3)
        time.sleep(ts)

    def test_r4(self):
        # Set up the waiting time for page to load
        ts = int(5)

        # Execute the test case R4:
        # Fill the fields. Enter a text instead of E-mail address and click Continue

        # Fill the fields with data
        self.driver.find_element(*RegistrationFormElements.first_name).send_keys('test')
        self.driver.find_element(*RegistrationFormElements.last_name).send_keys('test')
        self.driver.find_element(*RegistrationFormElements.email).send_keys('signtest@getnada.com')
        self.driver.find_element(*RegistrationFormElements.password).send_keys('test')

        # Click Continue button - had to do it twice, sometimes once didn't work
        self.driver.find_element(*RegistrationFormElements.button).click()
        self.driver.find_element(*RegistrationFormElements.button).click()

        # Wait and check if error is displayed
        time.sleep(ts)

        message = self.driver.find_element(*ErrorMassages.pass_few_char)

        self.assertTrue((message).is_displayed())
        print("Passed. After putting too few characters in the password field, the correct error appeared")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()