import os
from  box.exceptions import BoxValueError
import yaml
from chicken_disease_classification import logger
import jason
import joblib
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any
import base64

@ensure_annotations

def read_yaml_file(file_path:Path)->config_box:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        file_path (Path): Path to the yaml file

    Raises:
        e: Raises exception if there is an error reading the file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file data
    """
    try:
        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {file_path} loaded successfully")
            return config_box.ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading the YAML file: {file_path}. Error: {e}")
        raise e
    

@ensure_annotations
def save_jason(path:Path,data:dict)->None:
    """Saves a dictionary to a json file

    Args:
        path (Path): Path to the json file
        data (dict): Dictionary to be saved

    Raises:
        e: Raises exception if there is an error saving the file
    """
    try:
        with open(path,'w') as json_file:
            jason.dump(data,json_file,indent=4)
        logger.info(f"JSON file: {path} saved successfully")
    except Exception as e:
        logger.error(f"Error saving the JSON file: {path}. Error: {e}")
        raise e
    
    @ensure_annotations
    def save_bin(path:Path,data:Any)->None:
        """Saves data to a binary file using joblib

        Args:
            path (Path): Path to the binary file
            data (Any): Data to be saved

        Raises:
            e: Raises exception if there is an error saving the file
        """
        try:
            joblib.dump(data,path)
            logger.info(f"Binary file: {path} saved successfully")
        except Exception as e:
            logger.error(f"Error saving the binary file: {path}. Error: {e}")
            raise e
        
        @ensure_annotations
        def load_bin(path:Path)->Any:
            """Loads data from a binary file using joblib

            Args:
                path (Path): Path to the binary file

            Raises:
                e: Raises exception if there is an error loading the file

            Returns:
                Any: Loaded data
            """
            try:
                data = joblib.load(path)
                logger.info(f"Binary file: {path} loaded successfully")
                return data
            except Exception as e:
                logger.error(f"Error loading the binary file: {path}. Error: {e}")
                raise e
            
@ensure_annotations
def get_size(path:Path)->str:
    """Gets the size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024,2)
    return f"{size_in_kb} KB"

@ensure_annotations
def decode_image(image_base64:str)->bytes:
    """Decodes a base64 encoded image string to bytes

    Args:
        image_base64 (str): Base64 encoded image string

    Returns:
        bytes: Decoded image bytes
    """
    image_bytes = base64.b64decode(image_base64)
    return image_bytes          

@ensure_annotations
def encode_image(image_bytes:bytes)->str:
    """Encodes image bytes to a base64 string

    Args:
        image_bytes (bytes): Image bytes

    Returns:
        str: Base64 encoded image string
    """
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    return image_base64 