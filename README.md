# NTec

NTec is a modular, AI-driven auto tuning system that combines advanced calibration techniques with real-time sensor feedback. It integrates features from traditional auto tuning systems (inspired by MoTeC) with AI-based gradient tuning, detuning on part degradation, active aero controls (DRS and braking stability), and an active lambda controller for maintaining the optimal air–fuel ratio.

## Features

- **Base Map Loading:** Reads and manages engine calibration maps.
- **Gradient Tuning:** Slowly adjusts calibration parameters using AI recommendations.
- **Detuning:** Applies negative gradient increments when parts are degraded.
- **Active Aero Control:** Manages DRS and braking stability based on dynamic sensor data.
- **Active Lambda Control:** Continuously adjusts the lambda target to maintain stoichiometric balance.
- **Modular Design:** Each module is independent and configurable via YAML files.

## Setup

1. Clone the repository.
2. Install the requirements with:
```bash
   pip install -r requirements.txt
```
3.	Configure your settings in configs/base_map.yaml and configs/tuning_config.yaml.
4.	Run the system:
```bash
   python -m src.main
```
