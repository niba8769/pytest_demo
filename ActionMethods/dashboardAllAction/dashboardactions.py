from ObjectRepo.dashboardObjrepo import DashboardPage


class dashboard:

    def __init__(self, driver):
        self.driver = driver

    def ClickLogout_Dropdown(self):
        logoutdropdown = DashboardPage.logout_dropdown()
        logoutdropdown.click()
