import unittest
import Utils

class LearnTest(unittest.TestCase):

    def test_pricetofloat_comreais(self):
        string="R$1.234"
        expected=1234.0
        result=Utils.pricetofloat(string)
        self.assertEqual(result,expected) 

    def test_pricetofloat_comespaco(self):
        string="R$ 12.345"
        expected=12345.0
        result=Utils.pricetofloat(string)
        self.assertEqual(result,expected)

    def test_pricetofloat_trocavirgulaponto(self):
        string="1234,56"
        expected=1234.56
        result=Utils.pricetofloat(string)
        self.assertEqual(result,expected)

    def test_pricetofloat_trocavirgulaponto(self):
        string="1234,56"
        expected=1234.56
        result=Utils.pricetofloat(string)
        self.assertEqual(result,expected)
    

if __name__ == '__main__':

    unittest.main()





