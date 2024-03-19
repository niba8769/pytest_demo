import pytest


class Testplayground:

    @pytest.mark.parametrize("i", range(50))
    def test_Num(self,i):
        if i in (17, 25):
            pytest.fail("bad luck")

