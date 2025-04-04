import time
import logging
from base_map import BaseMap
from tuning import Tuner
from ai_tuner import AITuner
from detuner import Detuner
from aero_controller import AeroController
from lamda_controller import ActiveLamdaController

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    # Load the base calibration map.
    base_map_instance = BaseMap()
    base_map = base_map_instance.get_map()
    
    # Initialize modules with configuration parameters.
    tuner = Tuner(base_map, gradient_step=0.01)
    ai_tuner = AITuner(input_dim=5)
    detuner = Detuner(base_map, gradient_step=0.01)
    aero_controller = AeroController()
    lamda_controller = ActiveLamdaController(target_lambda=1.0, adjustment_step=0.01)
    
    # Main control loop.
    while True:
        # Simulated sensor data (replace with real sensor inputs).
        sensor_data = {
            'steering_angle': 0.5,
            'throttle_position': 0.7,
            'brake_pressure': 0.2,
            'accelerometer': [0.3, 0.4, 0.5],
            'wheel_speeds': [90, 92, 88, 91],
            'vehicle_speed': 100,
            'lap_time': 75  # seconds
        }
        
        # AI-based tuning for "fuel_map".
        sensor_input = [0.5, 0.7, 0.2, 0.3, 0.9]  # Replace with actual sensor input.
        adjustment_direction = ai_tuner.predict_adjustment(sensor_input)
        if adjustment_direction != 0:
            try:
                new_value = tuner.apply_gradient_increment("fuel_map", direction=adjustment_direction)
                logger.info(f"[Tuning] Adjusted 'fuel_map' to {new_value:.3f} (direction: {adjustment_direction})")
            except KeyError:
                logger.warning("Parameter 'fuel_map' not found in base map. Skipping tuning.")
        
        # Check for part degradation and apply detuning.
        part_status = {
            'turbocharger': True,      # Simulated degradation.
            'fuel_injectors': False
        }
        detune_params = detuner.check_part_degradation(part_status)
        for param in detune_params:
            try:
                new_detuned_value = detuner.apply_detune(param)
                logger.info(f"[Detune] Detuned '{param}' to {new_detuned_value:.3f} due to degradation.")
            except KeyError:
                logger.warning(f"Parameter '{param}' not found in base map. Skipping detune.")
        
        # Update base map file after tuning/detuning.
        base_map_instance.update_map(tuner.get_updated_map())
        
        # Aero Controller: update DRS and braking stability.
        drs_state = aero_controller.update_drs(sensor_data['vehicle_speed'], sensor_data['lap_time'])
        logger.info(f"[Aero] DRS State: {'Active' if drs_state else 'Inactive'}")
        brake_adjustments = aero_controller.update_braking_stability(sensor_data['wheel_speeds'])
        logger.info(f"[Aero] Brake Stability Adjustments: {brake_adjustments}")
        aero_status = aero_controller.get_aero_status()
        logger.info(f"[Aero] Aero Status: {aero_status}")
        
        # Active Lambda Control: simulate lambda sensor reading.
        simulated_lambda_sensor = 1.05  # Example: slightly lean condition.
        updated_lambda_target = lamda_controller.update_lambda(simulated_lambda_sensor)
        logger.info(f"[Lambda] Updated target lambda: {updated_lambda_target:.3f} (Sensor reading: {simulated_lambda_sensor})")
        
        # Sleep to simulate a real-time control loop.
        time.sleep(2)

if __name__ == "__main__":
    main()
