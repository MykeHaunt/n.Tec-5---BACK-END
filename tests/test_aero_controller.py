import unittest
from src.aero_controller import AeroController

class TestAeroController(unittest.TestCase):
    def setUp(self):
        self.aero = AeroController()
    
    def test_update_drs(self):
        drs_state = self.aero.update_drs(vehicle_speed=90, lap_time=75, race_mode=True)
        self.assertTrue(drs_state)
    
    def test_update_braking_stability(self):
        adjustments = self.aero.update_braking_stability([90, 92, 88, 91])
        self.assertTrue(isinstance(adjustments, dict))

if __name__ == '__main__':
    unittest.main()
