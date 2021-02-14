from selenium.webdriver.common.by import By

class RegistrationFormElements(object):
    # Registration form fields
    first_name = (By.NAME, 'firstName')
    last_name = (By.NAME, 'lastName')
    email = (By.NAME, 'email')
    password = (By.NAME, 'password')
    button = (By.XPATH, '//*[text()="Continue »"]')