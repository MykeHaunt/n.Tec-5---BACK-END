import unittest
from src.tuning import Tuner

class TestTuning(unittest.TestCase):
    def setUp(self):
        self.base_map = {'fuel_map': 1.0}
        self.tuner = Tuner(self.base_map, gradient_step=0.01)
    
    def test_apply_gradient_increment(self):
        new_val = self.tuner.apply_gradient_increment("fuel_map", direction=1)
        self.assertAlmostEqual(new_val, 1.01, places=2)

if __name__ == '__main__':
    unittest.main()
