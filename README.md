# n.Tec-5---BACK-END

![Build](https://github.com/MykeHaunt/n.Tec-5---BACK-END/actions/workflows/conda-package.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/github/license/MykeHaunt/n.Tec-5---BACK-END)
![Status](https://img.shields.io/badge/status-Beta-blue.svg)
![Release](https://img.shields.io/github/v/release/MykeHaunt/n.Tec-5---BACK-END)

> **WORK IN PROGRESS BY: H. Pandit**

# n.Tec-5 Back-End Documentation

**n.Tec-5** is a modular, AI-driven engine tuning and control platform. It functions like a custom Electronic Control Unit (ECU) that manages engine performance through adaptive calibration updates based on real-time sensor data. Inspired by MoTeC-style systems, this back end forms the brain of the tuning architecture.

---

## 1. Overview and Goals

- **Adaptive Engine Calibration**: AI-guided updates to boost/fuel/ignition maps.
- **Modular Structure**: Independent modules for tuning, detuning, lambda control, and aerodynamics.
- **Configuration via YAML**: Tuning parameters, thresholds, and targets are externally configurable.
- **Diagnostics & Logging**: Safe detuning on part degradation, with full traceable logs.
- **Cross-Platform Deployment**: Runs on PC, Raspberry Pi, or embedded Linux.

---

## 2. Architecture

### Major Modules

- `BaseMap`: Holds calibration parameters (`fuel_map`, `boost_map`, etc.).
- `Tuner`: Applies gradient updates (+/-ε) based on AI tuner decisions.
- `AITuner`: Neural net decision engine; predicts tuning direction (`+1`, `0`, `-1`).
- `Detuner`: Applies safe detune steps based on part health (e.g. reduce boost if turbo degraded).
- `ActiveLamdaController`: Adjusts lambda (AFR) setpoint based on sensor feedback.
- `AeroController`: Controls DRS and brake stability from speed/wheel data.

### Real-Time Data Loop

1. Collect sensor input  
2. Predict adjustment via `AITuner`  
3. Tune or detune parameters  
4. Update aero and lambda targets  
5. Log state & write back updated map  

---

## 3. Real-Time Tuning Algorithms

### Gradient Tuning

```python
new_val = tuner.apply_gradient_increment("fuel_map", direction=+1)
```

### Detuning

```python
part_status = {'turbocharger': True}
params = detuner.check_part_degradation(part_status)
```

### AI Tuner

```python
input_vec = [steering, throttle, accel, brake, lambda_err]
direction = ai_tuner.predict_adjustment(input_vec)

# • +1 = enrich/increase
# • -1 = lean/decrease
# • 0  = no change
```

---

## 4. Base Map & Lambda Controller

### Base Map (YAML Example)

```yaml
fuel_map: 1.0
boost_map: 1.0
```

### Lambda Control

```python
lamda_ctrl = ActiveLamdaController(target_lambda=1.0, adjustment_step=0.01)
new_target = lamda_ctrl.update_lambda(current_lambda=1.1)
```

- If AFR too lean → enrich  
- If AFR too rich → lean out  

---

## 5. Configuration (YAML)

**`configs/tuning_config.yaml`**:

```yaml
gradient_step: 0.01
detune_gradient_step: 0.01
lambda_target: 1.0
lambda_adjustment_step: 0.01
tolerance: 0.05
```

**Load Config Example**:

```python
with open("configs/tuning_config.yaml", 'r') as f:
    cfg = yaml.safe_load(f)
```

---

## 6. Sensor Input Integration

### Simulated Example

```python
sensor_data = {
  'steering': 0.5,
  'throttle': 0.7,
  'lambda': 1.05,
  'vehicle_speed': 100.0,
  'wheel_speeds': [90, 91, 89, 92],
}
```

### Real Sensor Integration (via CAN)

```python
msg = can_bus.recv()
if msg.arbitration_id == SPEED_CAN_ID:
    sensor_data['vehicle_speed'] = decode_speed(msg.data)
```

---

## 7. Aero Control System

### DRS Logic

```python
drs_active = aero_controller.update_drs(vehicle_speed=100, lap_time=60, race_mode=True)
```

### Brake Stability Logic

```python
adjustments = aero_controller.update_braking_stability([90, 92, 88, 91])
```

---

## 8. Logging and Output

All modules log decisions and map changes. Example output:

```
[Tuning] 'fuel_map' adjusted to 1.01  
[Detune] 'boost_map' detuned to 0.95  
[Lambda] target lambda=0.990  
[Aero] DRS=Active, BrakeAdjust=0.97  
```

---

## 9. System Integration

The **n.Tec-5 Back-End** can integrate with:

- MoTeC dash or ECU  
- Python front-end GUI  
- Embedded control loop on vehicle  
- Logging servers (via REST/WebSocket)  

The back end operates headless and exposes internal states via logs or API. It is designed for robustness in motorsport or simulation environments.

---

## 10. Credits

**WORK IN PROGRESS BY**: H. Pandit  
Part of the **n.Tec-5 Performance AI Tuning Suite**.

---

https://github.com/user-attachments/assets/66abe772-5801-432f-b7e9-d87fa1156551
https://github.com/user-attachments/assets/2193e625-aed2-4b76-ac46-6499485f27ee
![IMG_9852](https://github.com/user-attachments/assets/b19d5f80-d837-47be-84a0-4429bd9a4445)
![8051C332-E21F-4F94-A04E-0FD21D487EDC](https://github.com/user-attachments/assets/5671ed62-db51-4a1d-82e5-f154ed5c5e07)
![IMG_9865](https://github.com/user-attachments/assets/665bc732-c130-48fc-b32f-2cb3bc3fca82)
![IMG_9863](https://github.com/user-attachments/assets/66149681-128b-4d1c-80c2-11c40f9a4334)
