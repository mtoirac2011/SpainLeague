
import unittest
from ligatools import farToCelcious, if_integer, milesToKm, feetToMeter, meterToCm, nationNames

class Liga_tests(unittest.TestCase):
    
    def test_farToCelcious(self):
        self.assertTrue(farToCelcious(32) == '0.0')
        
    def test_ifinteger(self):
        self.assertTrue(if_integer('1') == True)
        
    def test_milesToKm(self):
        self.assertEqual(milesToKm(3), '4.83')
        
    def test_feetToMeter(self):
        self.assertNotEqual(feetToMeter(10), '3.06')
        
    def test_meterToCm(self):
        self.assertTrue(meterToCm(5) == '500')
        
    def test_nationNames(self):
        self.assertEqual(nationNames('AUT'), 'Austria')        
        
    def test_increment(self):
        self.assertAlmostEqual(4, 4)
        
if __name__ == '__main__':
    unittest.main()