import tensorflow as tf
import numpy as np
from typing import List
import logging

logger = logging.getLogger(__name__)

class AITuner:
    def __init__(self, input_dim: int = 5) -> None:
        # Build a simple model to predict tuning direction.
        self.model = self.build_model(input_dim)
    
    def build_model(self, input_dim: int) -> tf.keras.Model:
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(16, activation='relu', input_shape=(input_dim,)),
            tf.keras.layers.Dense(8, activation='relu'),
            tf.keras.layers.Dense(1, activation='tanh')  # Output between -1 and +1
        ], name="AITuner_Model")
        model.compile(optimizer='adam', loss='mse')
        logger.info("AI Tuner model built successfully.")
        return model

    def predict_adjustment(self, sensor_data: List[float]) -> int:
        """
        Predicts a tuning adjustment direction based on sensor data.
        :param sensor_data: A list of sensor readings.
        :return: +1 (increase), -1 (decrease), or 0 (no change).
        """
        sensor_array = np.array(sensor_data).reshape(1, -1)
        prediction = self.model.predict(sensor_array)[0][0]
        if prediction > 0.1:
            return 1
        elif prediction < -0.1:
            return -1
        else:
            return 0
