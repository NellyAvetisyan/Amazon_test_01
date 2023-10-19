from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

        pass

    def fill_username_field(self,username):
        userNameFieldElement = self.driver.find_element(By.ID, "ap_email")
        userNameFieldElement.clear()
        userNameFieldElement.send_keys(username)

    def click_to_continue_button(self):
        continueButton = self.driver.find_element(By.ID, "continue")
        continueButton.click()

    def fill_password_button(self,password):
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)
        sleep(6)

    def click_signin_button(self):
        signinButton = self.driver.find_element(By.XPATH, "//input[@id='signInSubmit']")
        signinButton.click()
        sleep(10)

