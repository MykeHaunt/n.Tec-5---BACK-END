from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class Tuner:
    def __init__(self, base_map: Dict[str, Any], gradient_step: float = 0.01) -> None:
        """
        :param base_map: A dictionary representing the calibration values.
        :param gradient_step: The small increment value for adjustments.
        """
        self.map = base_map
        self.gradient_step = gradient_step

    def apply_gradient_increment(self, parameter: str, direction: int = 1) -> float:
        """
        Adjusts a parameter by a small gradient increment.
        :param parameter: The key in the base map to adjust.
        :param direction: +1 for increase, -1 for decrease.
        :return: Updated parameter value.
        """
        if parameter not in self.map:
            logger.error(f"{parameter} not found in the base map.")
            raise KeyError(f"{parameter} not found in the base map.")
        current_value = self.map[parameter]
        new_value = current_value + direction * self.gradient_step
        self.map[parameter] = new_value
        logger.info(f"Parameter '{parameter}' adjusted from {current_value} to {new_value}.")
        return new_value

    def get_updated_map(self) -> Dict[str, Any]:
        return self.map
