# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NavigationBar():
    def __init__(self, driver):
        self.driver = driver

    def click_to_navigation_bar(self):
        cartButtonElement = self.driver.find_element(By.ID, "nav-cart-text-container")
        cartButtonElement.click()

    def click_to_logo_bar(self):
        logoBarSelect = self.driver.find_element(By.ID, "nav-logo-sprites")
        logoBarSelect.click()

    def click_to_customersmostloved_field(self):
        customersMostLovedButton = self.driver.find_element(By.ID, "DaoU8F0BjAAFRW9Cc17iHQ")
        customersMostLovedButton.click()







