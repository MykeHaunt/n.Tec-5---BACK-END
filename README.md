# NTec Web Interface with Real Sensor Integration and Advanced AI Decision-Making

NTec is an AI-driven auto tuning system that integrates real sensor data (via CAN bus), advanced AI for dynamic adjustment decisions, and an interactive web front end.

## Features

- **Real Sensor Integration:** Uses the `python-can` library to read sensor data from a CAN bus. If no CAN interface is available, simulated sensor data is used.
- **Advanced AI Decision-Making:** A TensorFlow model predicts adjustment directions based on real-time sensor input.
- **Enhanced Front-End Interactivity:** A Flask-based web application with AJAX calls provides a responsive interface to view calibration parameters and send tuning commands.
- **Calibration Map Persistence:** Engine calibration parameters are stored in a YAML file (`base_map.yaml`) and updated live.

## Repository Structure
