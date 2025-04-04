# NTec Architecture

NTec is composed of the following modules:

- **Base Map Module:** Loads the base calibration map from a YAML configuration file.
- **Tuning Module:** Applies small gradient increments to adjust calibration parameters based on AI input.
- **AI Tuner Module:** Uses a simple neural network to determine the optimal adjustment direction.
- **Detuner Module:** Applies negative gradient increments to detune parameters when part degradation is confirmed.
- **Aero Controller Module:** Controls active aero features such as DRS and braking stability.
- **Active Lambda Controller:** Monitors lambda sensor readings and adjusts the target lambda to maintain the optimal air–fuel ratio.
- **Main Module:** Integrates all modules into a real-time control loop.

Each module is independently testable and configurable via YAML files.
