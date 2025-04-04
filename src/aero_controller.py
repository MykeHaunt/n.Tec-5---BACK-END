from typing import List, Dict
import logging

logger = logging.getLogger(__name__)

class AeroController:
    def __init__(self) -> None:
        self.drs_active = False
        self.brake_stability_active = False

    def update_drs(self, vehicle_speed: float, lap_time: float, race_mode: bool = True) -> bool:
        """
        Control DRS (Drag Reduction System) based on conditions.
        :param vehicle_speed: Current vehicle speed.
        :param lap_time: Current lap time.
        :param race_mode: Flag indicating if race mode is active.
        :return: DRS state.
        """
        if race_mode and vehicle_speed > 80:
            self.drs_active = True
        else:
            self.drs_active = False
        logger.info(f"DRS state updated: {self.drs_active}")
        return self.drs_active

    def update_braking_stability(self, wheel_speeds: List[float]) -> Dict[str, float]:
        """
        Adjust braking stability based on wheel speed differences.
        :param wheel_speeds: List of wheel speeds [FL, FR, RL, RR].
        :return: Dictionary with braking adjustments.
        """
        avg_speed = sum(wheel_speeds) / len(wheel_speeds)
        adjustments = {}
        for idx, speed in enumerate(wheel_speeds):
            adjustments[f'wheel_{idx+1}'] = max(0.0, 1 - abs(speed - avg_speed) / avg_speed)
        self.brake_stability_active = any(val < 0.9 for val in adjustments.values())
        logger.info(f"Brake stability adjustments computed: {adjustments}")
        return adjustments

    def get_aero_status(self) -> Dict[str, bool]:
        return {
            "DRS": self.drs_active,
            "BrakeStability": self.brake_stability_active
        }
