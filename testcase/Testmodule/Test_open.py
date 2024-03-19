import time

import pytest

from ActionMethods.LoginAllAction.LoginAction import LoginAction
from utilities.readconfig import readconfig


class Testdemodriver:

    @pytest.mark.parametrize("username,password", [(readconfig.getUsername(), readconfig.getPassword())])
    def test_e2e(self, setup, username, password):
        self.driver = setup
        self.LoginAction = LoginAction(self.driver)
        self.driver.get(readconfig.getappUrl())
        self.LoginAction.LoginMethod(username, password)
        time.sleep(2)
        assert self.driver.current_url.__contains__("dashboard/index")==True
        yield

