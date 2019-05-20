from less2.data import Math

class TestClassHomeWork3():


    def test_sumnum(self):
        self.num1 = Math(10)
        result = Math.sum_num(self.num1, 20)
        assert result == 30

