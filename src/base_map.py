import os
import yaml
from typing import Any, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseMap:
    def __init__(self, config_path: str = 'configs/base_map.yaml') -> None:
        self.config_path = config_path
        self.map: Dict[str, Any] = {}
        self.load_map()

    def load_map(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_path):
            logger.error(f"Base map file not found at {self.config_path}")
            raise FileNotFoundError(f"Base map file not found at {self.config_path}")
        with open(self.config_path, 'r') as f:
            self.map = yaml.safe_load(f)
        logger.info("Base map loaded successfully.")
        return self.map

    def get_map(self) -> Dict[str, Any]:
        return self.map

    def update_map(self, new_map: Dict[str, Any]) -> None:
        self.map = new_map
        with open(self.config_path, 'w') as f:
            yaml.dump(self.map, f)
        logger.info("Base map updated and saved.")
