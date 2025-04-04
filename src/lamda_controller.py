from typing import Any
import logging

logger = logging.getLogger(__name__)

class ActiveLamdaController:
    def __init__(self, target_lambda: float = 1.0, adjustment_step: float = 0.01) -> None:
        """
        Initialize the Active Lambda Controller.
        :param target_lambda: Desired lambda value (1.0 is typically stoichiometric).
        :param adjustment_step: The gradient step for adjusting the lambda target.
        """
        self.target_lambda = target_lambda
        self.adjustment_step = adjustment_step

    def update_lambda(self, sensor_lambda: float, tolerance: float = 0.05) -> float:
        """
        Adjust the lambda target based on the sensor reading.
        :param sensor_lambda: Current measured lambda.
        :param tolerance: Allowable margin before adjustment.
        :return: Updated lambda target.
        """
        error = sensor_lambda - self.target_lambda
        if abs(error) > tolerance:
            if error > 0:
                self.target_lambda -= self.adjustment_step  # Enrich by lowering target
            else:
                self.target_lambda += self.adjustment_step  # Lean out by raising target
            logger.info(f"Lambda target adjusted to {self.target_lambda:.3f} (error: {error:.3f})")
        return self.target_lambda

    def get_current_target(self) -> float:
        return self.target_lambda
