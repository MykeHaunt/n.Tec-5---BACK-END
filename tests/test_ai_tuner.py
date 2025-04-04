import unittest
from src.ai_tuner import AITuner

class TestAITuner(unittest.TestCase):
    def setUp(self):
        self.ai_tuner = AITuner(input_dim=5)
    
    def test_predict_adjustment(self):
        # Use a fixed input; since the model is untrained, output may be near zero.
        adjustment = self.ai_tuner.predict_adjustment([0.5, 0.7, 0.2, 0.3, 0.9])
        self.assertIn(adjustment, [-1, 0, 1])

if __name__ == '__main__':
    unittest.main()
