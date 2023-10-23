from selenium.webdriver.common.by import By

class SearchFieldElement():
    def __init__(self, driver):
        self.driver = driver

    def fill_search_field(self, productname):
        searchFieldElementFill = self.driver.find_element(By.CLASS_NAME, "nav-search-field")
        # searchFieldElementFill.clear()
        searchFieldElementFill.send_keys(productname)

    def click_to_search_submit_button(self):
        searchSubmitButton = self.driver.find_element(By.ID, "nav-search-submit-button")
        searchSubmitButton.click()


    def click_to_first_item(self):
        # firstItemFieldElement = self.driver.find_element(By.XPATH, "(//div[@class='a-section'])[1]")
        # firstItemFieldElement.click()
        firstItemFieldElement = self.driver.find_element(By.XPATH, "(//div[@class='sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'])[1]")
        firstItemFieldElement.click()

