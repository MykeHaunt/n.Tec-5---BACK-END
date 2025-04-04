from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

class Detuner:
    def __init__(self, base_map: Dict[str, Any], gradient_step: float = 0.01) -> None:
        """
        :param base_map: A dictionary representing the calibration values.
        :param gradient_step: The small decrement value for detuning.
        """
        self.map = base_map
        self.gradient_step = gradient_step

    def check_part_degradation(self, part_status: Dict[str, bool]) -> List[str]:
        """
        Simulate part degradation confirmation.
        :param part_status: Dictionary with part names and degradation flags.
        :return: List of parameters to detune.
        """
        detune_params = []
        for part, degraded in part_status.items():
            if degraded:
                if part == 'turbocharger':
                    detune_params.append('boost_map')
                elif part == 'fuel_injectors':
                    detune_params.append('fuel_map')
                # Add additional mappings as needed.
        return detune_params

    def apply_detune(self, parameter: str) -> float:
        """
        Apply a negative gradient increment to detune a parameter.
        :param parameter: The key in the base map to adjust.
        :return: Updated parameter value.
        """
        if parameter not in self.map:
            logger.error(f"{parameter} not found in the base map.")
            raise KeyError(f"{parameter} not found in the base map.")
        current_value = self.map[parameter]
        new_value = current_value - self.gradient_step
        self.map[parameter] = new_value
        logger.info(f"Parameter '{parameter}' detuned from {current_value} to {new_value}.")
        return new_value

    def get_updated_map(self) -> Dict[str, Any]:
        return self.map
