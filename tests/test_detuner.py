import unittest
from src.detuner import Detuner

class TestDetuner(unittest.TestCase):
    def setUp(self):
        self.base_map = {'fuel_map': 1.0, 'boost_map': 1.0}
        self.detuner = Detuner(self.base_map, gradient_step=0.01)
    
    def test_apply_detune(self):
        new_val = self.detuner.apply_detune("fuel_map")
        self.assertAlmostEqual(new_val, 0.99, places=2)

if __name__ == '__main__':
    unittest.main()
