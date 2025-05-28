NTec Back-End

NTec Back-End is the core of the NTec (Next‑generation Tuning Technology) automotive system, a modular, AI‑driven engine tuning and control platform. It combines advanced calibration techniques with real‑time sensor feedback to dynamically optimize engine performance. The back‑end provides the underlying services for base map management, AI‑based gradient tuning, safety detuning, active aerodynamic control, and closed‑loop lambda (air–fuel) control. Written in Python, this package can run as a standalone command‑line application (entry point ntec) or be integrated into larger systems. It is designed for automotive/motorsport applications (inspired by systems like MoTeC) but is adaptable to any scenario requiring dynamic calibration control.
	•	Modular Design: Each functional component (BaseMap loader, AI Tuner, Tuner, Detuner, Aero Controller, Lambda Controller) is implemented as an independent module. Modules are connected in a data loop via YAML‑configurable interfaces.
	•	Real‑Time Sensor Feedback: The system reads simulated or live sensor data (throttle, speed, wheel speeds, etc.) in a loop and uses it to adjust tuning parameters continuously.
	•	AI/ML Integration: An advanced AI Tuner module can use various neural network architectures (feedforward, LSTM, Transformer, Bayesian, CNN‑LSTM, GNN, etc.) to recommend tuning adjustments based on sensor inputs.
	•	Safety Detuning: If parts are detected as degraded, the system automatically detunes (reduces) calibration parameters to preserve engine safety and longevity.
	•	Active Aerodynamics & Lambda Control: Separate controllers manage aerodynamic aids (e.g. DRS, brake stability) and continuously adjust the target air–fuel ratio (lambda) for optimal combustion.
	•	Configurable via YAML: All core parameters and behavior (base maps, tuning steps, lambda targets, etc.) are specified in simple YAML files under configs/, making the system highly configurable without changing code.

This documentation covers the system architecture, technologies, setup (development & production), containerization, packaging, CI/CD pipelines, and other developer‑oriented details. It assumes basic familiarity with Python and automotive tuning concepts.

⸻

Table of Contents
	1.	Overview
	2.	System Architecture
	3.	Technology Stack and Libraries
	4.	Modules and Components
	•	BaseMap (Calibration Loader)
	•	AI Tuner (Machine Learning)
	•	Tuner (Gradient Adjustment)
	•	Detuner (Safety Adjustment)
	•	Aero Controller (Active Aero)
	•	Lambda Controller (AFR Control)
	5.	Configuration Files
	6.	Logging and Monitoring
	7.	Setup and Installation
	•	Development Environment
	•	Production Environment
	8.	Docker Containerization
	9.	PyInstaller Packaging
	10.	Continuous Integration (CI/CD)
	11.	Usage (Command‑Line Interface)
	12.	Developer Notes
	13.	License

⸻

Overview

The NTec Back‑End manages engine calibration data and uses sensor inputs to automatically tune an engine’s performance in real time. It integrates several advanced features:
	1.	Base Map Loading: Reads and maintains engine calibration maps from YAML configuration files.
	2.	AI‑Based Gradient Tuning: Uses machine learning models to recommend tuning adjustments.
	3.	Safety Detuning: Automatically reduces calibration parameters when parts degrade.
	4.	Active Aero Control: Dynamically manages aerodynamic devices (DRS, brake stability).
	5.	Active Lambda Control: Continuously adjusts the target air–fuel ratio for optimal combustion.
	6.	Modular Architecture: Components run independently and communicate via shared data structures.
	7.	Real‑Time Loop: Executes a continuous control cycle: read sensors → tune/detune → update config → control aero & lambda.

NTec Back‑End can run as a standalone process (python -m src.main or ntec console script) or be integrated into a larger system.

⸻

System Architecture

NTec Back‑End follows a modular, event‑driven architecture. Each component is a Python module/class with well‑defined inputs and outputs. The system operates in a feedback‑control loop:

[ Sensor Inputs ]
       │
┌──────┴──────┐
│             │
│  [ AI Tuner ] ──▶ [ Tuner ] ──▶ Update BaseMap
│             │
│  [Detuner] ──▶─┘
│             │
│ [ Aero Ctrl ]      [ Lambda Ctrl ]
└────────────┴────────────┘

	•	Sensor Inputs: Read from simulated or live sources (CAN, files, etc.).
	•	AI Tuner: Predicts adjustment direction (+1, 0, –1) for calibration parameters.
	•	Tuner: Applies gradient steps to increase performance.
	•	Detuner: Applies negative steps to ensure safety.
	•	BaseMap: Persists calibration values to configs/base_map.yaml.
	•	Aero Controller: Manages DRS and brake stability flags.
	•	Lambda Controller: Adjusts lambda target based on sensor readings.

⸻

Technology Stack and Libraries
	•	Python 3.8+
	•	TensorFlow >=2.8 (Keras API for AI Tuner)
	•	TensorFlow Probability (Bayesian models)
	•	Keras Tuner (hyperparameter search)
	•	Spektral (Graph Neural Networks)
	•	PyYAML (configuration parsing)
	•	NumPy (numeric computing)
	•	Python logging (runtime logs)
	•	pytest (unit testing)
	•	GitHub Actions (CI/CD workflows)
	•	Docker (containerization)
	•	PyInstaller (executable packaging)

⸻

Modules and Components

BaseMap (Calibration Loader)
	•	File: src/base_map.py
	•	Purpose: Load, update, and persist calibration maps (base_map.yaml).
	•	Key Methods:
	•	load_map()
	•	get_map()
	•	update_map(new_map)

AI Tuner (Machine Learning)
	•	File: src/ai_tuner.py
	•	Purpose: Build and run inference on various neural network architectures.
	•	Model Types: default, lstm, attention, bayesian, hybrid_cnn_lstm, reinforcement, automl, transformer, quantile, graph, autoencoder.
	•	Key Methods:
	•	__init__(input_dim, model_type)
	•	build_model()
	•	predict_adjustment(sensor_data)

Tuner (Gradient Adjustment)
	•	File: src/tuning.py
	•	Purpose: Apply positive gradient steps to calibration parameters.
	•	Key Methods:
	•	apply_gradient_increment(parameter, direction)
	•	get_updated_map()

Detuner (Safety Adjustment)
	•	File: src/detuner.py
	•	Purpose: Apply negative steps when part degradation is detected.
	•	Key Methods:
	•	check_part_degradation(part_status)
	•	apply_detune(parameter)

Aero Controller (Active Aero)
	•	File: src/aero_controller.py
	•	Purpose: Manage DRS and brake stability.
	•	Key Methods:
	•	update_drs(vehicle_speed, lap_time, race_mode=True)
	•	update_braking_stability(wheel_speeds)
	•	get_aero_status()

Lambda Controller (AFR Control)
	•	File: src/lamda_controller.py
	•	Purpose: Maintain target air–fuel ratio.
	•	Key Methods:
	•	update_lambda(sensor_lambda, tolerance=0.05)
	•	get_current_target()

⸻

Configuration Files
	•	configs/base_map.yaml

fuel_map: 1.0
boost_map: 1.0


	•	configs/tuning_config.yaml

gradient_step: 0.01
detune_gradient_step: 0.01
lambda_target: 1.0
lambda_adjustment_step: 0.01
tolerance: 0.05



⸻

Logging and Monitoring
	•	Uses Python’s logging module (INFO level).
	•	Module‑specific logs: BaseMap, Tuner/Detuner, AI Tuner, Aero/Lambda controllers.
	•	Can increase verbosity to DEBUG for troubleshooting.

⸻

Setup and Installation

Development Environment

git clone https://github.com/MykeHaunt/n.Tec-5---BACK-END.git
cd n.Tec-5---BACK-END
python3 -m venv venv
source venv/bin/activate    # or .\venv\Scripts\activate on Windows
pip install --upgrade pip
pip install tensorflow tensorflow-io PyYAML numpy
# Optional extras:
pip install keras-tuner spektral tensorflow-probability
pytest tests/

Run in dev mode:

python -m src.main

Production Environment
	•	Via console script: ntec (after pip install .)
	•	Or Docker / PyInstaller as below.

⸻

Docker Containerization

FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install -e .
CMD ["ntec"]

Build & run:

docker build -t ntec-backend:latest .
docker run --rm ntec-backend:latest


⸻

PyInstaller Packaging

pip install pyinstaller
pyinstaller --onefile --name ntec_backend src/main.py
# Executable at dist/ntec_backend
./dist/ntec_backend


⸻

Continuous Integration (CI/CD)

GitHub Actions workflows in .github/workflows/:
	•	codescan.yml: Lint (Flake8), pytest
	•	codeql.yml: Security analysis
	•	dependency-review.yml: Vulnerability scanning
	•	python-package-conda.yml: Build/test in Conda

⸻

Usage (Command‑Line Interface)
	•	Via Python: python -m src.main
	•	Via Script: ntec
	•	Current: No CLI flags; configure via YAML files.

⸻

Developer Notes
	•	Structure:

src/
configs/
tests/
.github/workflows/
setup.py
README.md


	•	Adding Features:
	•	Calibration parameters → add to base_map.yaml
	•	New sensors → extend main.py input dict
	•	New AI models → extend AITuner
	•	Testing: Add tests in tests/ and run pytest.
	•	Logging: Use module logger at INFO/DEBUG.
	•	Style: Follow PEP 8; CI enforces linting.

⸻

License

MIT License — see LICENSE for details.