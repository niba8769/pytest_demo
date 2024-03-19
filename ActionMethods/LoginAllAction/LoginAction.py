from ObjectRepo.LoginPage import LoginObjPage
from ObjectRepo.LoginPage.LoginObjPage import LoginPage


class LoginAction:

    def __init__(self, driver):
        self.driver = driver
        self.login = LoginPage(driver)

    def setUserName(self, Username):
        username = self.login.getUserName()
        username.clear()
        username.send_keys(Username)

    def setPassword(self, Password):
        password = self.login.getPassword()
        password.clear()
        password.send_keys(Password)

    def setLogin(self):
        LoginButton = self.login.getLoginButton()
        LoginButton.click()

    def LoginMethod(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        self.setLogin()
