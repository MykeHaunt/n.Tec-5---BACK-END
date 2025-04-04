import os
import yaml
import unittest
from src.base_map import BaseMap

class TestBaseMap(unittest.TestCase):
    def setUp(self):
        # Create a temporary base map file.
        self.test_file = 'configs/test_base_map.yaml'
        with open(self.test_file, 'w') as f:
            yaml.dump({'fuel_map': 1.0, 'boost_map': 1.0}, f)
    
    def test_load_map(self):
        bm = BaseMap(config_path=self.test_file)
        self.assertEqual(bm.get_map()['fuel_map'], 1.0)
    
    def tearDown(self):
        os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
