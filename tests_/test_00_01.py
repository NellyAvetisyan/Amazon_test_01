from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

userNameFieldElement = driver.find_element(By.ID, "ap_email")
userNameFieldElement.clear()
userNameFieldElement.send_keys("nellikoko91@gmail.com")

continueButton = driver.find_element(By.ID, "continue")
continueButton.click()

passwordFieldElement = driver.find_element(By.ID, "ap_password")
passwordFieldElement.clear()
passwordFieldElement.send_keys("Karl2022")
sleep(6)

signinButton = driver.find_element(By.XPATH, "//input[@id='signInSubmit']")
signinButton.click()
sleep(10)