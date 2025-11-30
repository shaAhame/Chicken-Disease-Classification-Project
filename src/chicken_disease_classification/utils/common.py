import os
from box.exceptions import BoxValueError
import yaml
from chicken_disease_classification import logger
import json
import joblib
from box import config_box
from pathlib import Path
from typing import Any
import base64


def read_yaml_file(file_path: Path) -> config_box:
    """Reads a YAML file and returns a ConfigBox object."""
    try:
        with open(file_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {file_path} loaded successfully")
            return config_box.ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading the YAML file: {file_path}. Error: {e}")
        raise e


def save_json(path: Path, data: dict) -> None:
    """Saves a dictionary to a JSON file."""
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"JSON file: {path} saved successfully")
    except Exception as e:
        logger.error(f"Error saving the JSON file: {path}. Error: {e}")
        raise e


def save_bin(path: Path, data: Any) -> None:
    """Saves data to a binary file using joblib."""
    try:
        joblib.dump(data, path)
        logger.info(f"Binary file: {path} saved successfully")
    except Exception as e:
        logger.error(f"Error saving the binary file: {path}. Error: {e}")
        raise e


def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib."""
    try:
        data = joblib.load(path)
        logger.info(f"Binary file: {path} loaded successfully")
        return data
    except Exception as e:
        logger.error(f"Error loading the binary file: {path}. Error: {e}")
        raise e


def get_size(path: Path) -> str:
    """Gets the size of a file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"


def decode_image(image_base64: str) -> bytes:
    """Decodes a base64 encoded image string to bytes."""
    image_bytes = base64.b64decode(image_base64)
    return image_bytes


def encode_image(image_bytes: bytes) -> str:
    """Encodes image bytes to a base64 string."""
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    return image_base64


def create_directories(path_list: list[Path]) -> None:
    """Creates directories for the given list of paths."""
    for path in path_list:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")
