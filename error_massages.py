from selenium.webdriver.common.by import By

class ErrorMassages(object):

    # Error massage after putting a text instead of email address
    text_instead_email = (By.XPATH, '//*[text()="Please enter a valid email address."]')

    # Error massage after putting too few characters in the password field
    pass_few_char = (By.XPATH, '//*[text()="Passwords must be at least 6 characters long."]')