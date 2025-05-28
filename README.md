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

https://github.com/user-attachments/assets/66abe772-5801-432f-b7e9-d87fa1156551



https://github.com/user-attachments/assets/2193e625-aed2-4b76-ac46-6499485f27ee

![IMG_9852](https://github.com/user-attachments/assets/b19d5f80-d837-47be-84a0-4429bd9a4445)
![8051C332-E21F-4F94-A04E-0FD21D487EDC](https://github.com/user-attachments/assets/5671ed62-db51-4a1d-82e5-f154ed5c5e07)
![IMG_9865](https://github.com/user-attachments/assets/665bc732-c130-48fc-b32f-2cb3bc3fca82)
![IMG_9863](https://github.com/user-attachments/assets/66149681-128b-4d1c-80c2-11c40f9a4334)
