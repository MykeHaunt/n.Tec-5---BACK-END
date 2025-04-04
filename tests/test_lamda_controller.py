import unittest
from src.lamda_controller import ActiveLamdaController

class TestLamdaController(unittest.TestCase):
    def setUp(self):
        self.lamda_controller = ActiveLamdaController(target_lambda=1.0, adjustment_step=0.01)
    
    def test_update_lambda(self):
        # Simulate a lambda sensor reading slightly above target.
        new_target = self.lamda_controller.update_lambda(1.05)
        self.assertLess(new_target, 1.0)
    
    def test_no_adjustment_within_tolerance(self):
        new_target = self.lamda_controller.update_lambda(1.02)
        self.assertAlmostEqual(new_target, 1.0, places=2)

if __name__ == '__main__':
    unittest.main()
