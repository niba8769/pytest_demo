from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class LoginPage:
    userTxt = (By.XPATH,"//input[@name='username']")
    password = (By.XPATH,"//input[@name='password']")
    login = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def getUserName(self):
        username = self.driver.find_element(*LoginPage.userTxt)
        return username


    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)


    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.login)
