# n.Tec‑5 Back‑End

**n.Tec‑5 Back‑End** is the core of the **n.Tec** (Next‑generation Tuning Technology) automotive system—a modular, AI‑driven engine‑tuning and control platform. It combines advanced calibration techniques with real‑time sensor feedback to dynamically optimize engine performance.  

---

## Table of Contents

1. [Overview](#overview)  
2. [System Architecture](#system-architecture)  
3. [Technology Stack & Libraries](#technology-stack--libraries)  
4. [Modules & Components](#modules--components)  
   - [BaseMap (Calibration Loader)](#basemap-calibration-loader)  
   - [AI Tuner (Machine Learning)](#ai-tuner-machine-learning)  
   - [Tuner (Gradient Adjustment)](#tuner-gradient-adjustment)  
   - [Detuner (Safety Adjustment)](#detuner-safety-adjustment)  
   - [Aero Controller (Active Aero)](#aero-controller-active-aero)  
   - [Lambda Controller (AFR Control)](#lambda-controller-afr-control)  
5. [Configuration Files](#configuration-files)  
6. [Logging & Monitoring](#logging--monitoring)  
7. [Setup & Installation](#setup--installation)  
   - [Development Environment](#development-environment)  
   - [Production Environment](#production-environment)  
8. [Docker Containerization](#docker-containerization)  
9. [PyInstaller Packaging](#pyinstaller-packaging)  
10. [Continuous Integration (CI/CD)](#continuous-integration-cicd)  
11. [Usage (CLI)](#usage-cli)  
12. [Developer Notes](#developer-notes)  
13. [License](#license)  

---

## Overview

n.Tec‑5 Back‑End manages engine calibration data and uses sensor inputs to automatically tune an engine’s performance in real time. Key features:

- **Base Map Loading**: Reads and persists calibration maps from YAML files.  
- **AI‑Based Gradient Tuning**: Uses neural networks to recommend calibration adjustments.  
- **Safety Detuning**: Automatically reduces parameters when parts degrade.  
- **Active Aero Control**: Manages DRS and brake stability flags.  
- **Lambda Control**: Maintains target air–fuel ratio via closed‑loop adjustments.  
- **Modular Design**: Each component runs independently and communicates via shared data structures.  
- **Real‑Time Loop**: Continuously executes: read sensors → tune/detune → persist → update aero & lambda.

---

## System Architecture

```text
         [ Sensor Inputs ]
                │
         ┌──────┴──────┐
         │             │
         │ [ AI Tuner ] ──▶ [ Tuner ] ──▶ Update BaseMap
         │             │
         │ [ Detuner ] ─┘
         │
         │ [ Aero Ctrl ]    [ Lambda Ctrl ]
         └────────────┴────────────┘

1. **Sensor Inputs**: Simulated or live (CAN, files, etc.)  
2. **AI Tuner**: Predicts +1/0/–1 adjustment for calibration keys  
3. **Tuner**: Applies gradient step to increase performance  
4. **Detuner**: Applies negative step for safety  
5. **BaseMap**: Persists updates to `configs/base_map.yaml`  
6. **Aero Controller**: Toggles DRS and brake‑stability  
7. **Lambda Controller**: Adjusts target λ based on sensor read  

---

## Technology Stack & Libraries

- **Python 3.8+**  
- **TensorFlow ≥2.8** (Keras API)  
- **TensorFlow Probability** (Bayesian models)  
- **Keras Tuner** (hyperparameter search)  
- **Spektral** (Graph Neural Networks)  
- **PyYAML** (config parsing)  
- **NumPy** (numerical computing)  
- **logging** (runtime logs)  
- **pytest** (unit tests)  
- **GitHub Actions** (CI/CD)  
- **Docker** (containerization)  
- **PyInstaller** (executable packaging)  

---

## Modules & Components

### BaseMap (Calibration Loader)

- **Location**: `src/base_map.py`  
- **Purpose**: Load, update, and persist the calibration map.  
- **Key Methods**:  
  - `load_map()`  
  - `get_map()`  
  - `update_map(new_map)`  

---

### AI Tuner (Machine Learning)

- **Location**: `src/ai_tuner.py`  
- **Purpose**: Build and run inference on various neural models.  
- **Supported Models**:  
  - `default`, `lstm`, `attention`, `bayesian`,  
  - `hybrid_cnn_lstm`, `reinforcement`, `automl`,  
  - `transformer`, `quantile`, `graph`, `autoencoder`  
- **Key Methods**:  
  - `__init__(input_dim, model_type)`  
  - `build_model()`  
  - `predict_adjustment(sensor_data)`  

---

### Tuner (Gradient Adjustment)

- **Location**: `src/tuning.py`  
- **Purpose**: Apply positive gradient steps to calibration keys.  
- **Key Methods**:  
  - `apply_gradient_increment(parameter, direction)`  
  - `get_updated_map()`  

---

### Detuner (Safety Adjustment)

- **Location**: `src/detuner.py`  
- **Purpose**: Apply negative adjustments on part degradation.  
- **Key Methods**:  
  - `check_part_degradation(part_status)`  
  - `apply_detune(parameter)`  

---

### Aero Controller (Active Aero)

- **Location**: `src/aero_controller.py`  
- **Purpose**: Manage DRS and brake stability.  
- **Key Methods**:  
  - `update_drs(vehicle_speed, lap_time, race_mode=True)`  
  - `update_braking_stability(wheel_speeds)`  
  - `get_aero_status()`  

---

### Lambda Controller (AFR Control)

- **Location**: `src/lamda_controller.py`  
- **Purpose**: Maintain target air–fuel ratio.  
- **Key Methods**:  
  - `update_lambda(sensor_lambda, tolerance=0.05)`  
  - `get_current_target()`  

---

## Configuration Files

- **`configs/base_map.yaml`**  
  ```yaml
  fuel_map: 1.0
  boost_map: 1.0
  # add your own parameters here

	•	configs/tuning_config.yaml

gradient_step: 0.01
detune_gradient_step: 0.01
lambda_target: 1.0
lambda_adjustment_step: 0.01
tolerance: 0.05



⸻

Logging & Monitoring
	•	Uses Python’s built‑in logging (default INFO).
	•	Logs by module: BaseMap, Tuner, Detuner, AI Tuner, Aero, Lambda.
	•	Switch to DEBUG for verbose stack traces and model summaries.

⸻

Setup & Installation

Development Environment

git clone https://github.com/MykeHaunt/n.Tec-5---BACK-END.git
cd n.Tec-5---BACK-END
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install tensorflow tensorflow-io PyYAML numpy
# Optional:
pip install keras-tuner spektral tensorflow-probability
pytest tests/

Run in dev mode:

python -m src.main


⸻

Production Environment
	•	Console script: after pip install ., run ntec
	•	Or use Docker / PyInstaller (see below)

⸻

Docker Containerization

# Dockerfile
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
# Executable in dist/ntec_backend
./dist/ntec_backend


⸻

Continuous Integration (CI/CD)

GitHub Actions workflows (.github/workflows/):
	•	codescan.yml: Flake8 lint + pytest
	•	codeql.yml: Security analysis
	•	dependency-review.yml: Vulnerability detection
	•	python-package-conda.yml: Conda build & test

⸻

Usage (CLI)
	•	Via Python: python -m src.main
	•	Via Script: ntec
	•	Configuration: Edit configs/*.yaml

⸻

Developer Notes
	•	Project Layout:

src/
configs/
tests/
.github/workflows/
setup.py
README.md


	•	Extending:
	•	Add calibration keys to base_map.yaml
	•	Extend main.py for new sensor inputs
	•	Add new ML models in AITuner
	•	Write tests in tests/, run pytest
	•	Style: Follow PEP 8, CI enforces lint rules.

⸻

License

This project is licensed under the MIT License. See LICENSE for details.

> **Next Steps:**  
> 1. Copy this content into your repository’s `README.md`.  
> 2. Commit & push to GitHub—your README will render beautifully.  
> 3. Adjust any section as needed (e.g. add real example sensor data or code snippets).
