
class DashboardPage:
    logout_dropdown = (By.XPATH ,"//span[@class='oxd-userdropdown-tab']/ancestor::div[@id='app']//preceding::header//following::div//span/img")

    def __init__(self,driver):
        self.driver=driver

    def getLogout_dropdown(self):
        return self.driver.find_element(*DashboardPage.logout_dropdown)
