import unittest
import Price_mon

class LearnTest(unittest.TestCase):

    def test_pricetofloatcomreais(self):
        string="R$1.234"
        expected=1234.0
        result=Price_mon.pricetofloat(string)
        self.assertEqual(result,expected) 

    def test_pricetofloatcomespaço(self):
        string="R$ 12.345"
        expected=12345.0
        result=Price_mon.pricetofloat(string)
        self.assertEqual(result,expected)

    def test_pricetofloat_trocavirgulaespaço(self):
        string="1234,56"
        expected=1234.56
        result=Price_mon.pricetofloat(string)
        self.assertEqual(result,expected)
    
if __name__ == '__main__':

    unittest.main()

    from mockito import when, mock, unstub



