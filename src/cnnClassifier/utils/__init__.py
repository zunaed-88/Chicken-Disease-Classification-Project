import os
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier.utils import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def real_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads a yaml file and returns a ConfigBox object
    
    Args: path_to_yaml(str): path like input
    
    Raises:
    ValueError: if yaml file is empty
    e: empty file

    Returns:
    ConfigBox: ConfigBox object
    
    """
    try:
        with open(path_to_yaml, "r") as file:
            data = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml}loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """"
    create list of directories
    
    Args:
    path_to_directories (list): list of path of directories
    ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to false

    
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"directory created: {path}")
        except Exception as e:
            logger.error(f"directory not created: {path}")
            raise e
        
@ensure_annotations
def save_json(oath: Path, data: dict):
    """
    save json file
    
    Args:
    Path(path): path to save json file
    data(dict): data to be saved in json file

    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
        logger.info(f"json file saved: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """
    load json file
    
    Args:
    Path(path): path to load json file

    Returns:
    ConfigBox (ConfigBox object) : data as a class attributes instead of dict 

    """
    with open(path, "r") as file:
        data = json.load(file)
        logger.info(f"json file is load from : {path}")
        return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file

    Args:
    data(Any):data to saved as binary
    path(Path): Path to binary file

    """
    joblib.dump(value = data, filename=path)
    logger.info(f"binary file saved at:{path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    
    """
    load binary data

    Args:
        path(Path): Path to binary file
    Returns:
        Any: Object stored in file
    
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path: Path)-> str:
    """
    get size in KB

    Args:
    path(Path): path of the file

    str : size in KB
    
    """
    size_in_KB = round(os.path.getsize(path)/1024)
    return f"~{size_in_KB} KB"

@ensure_annotations
def decodeImage(imgsrting, filename):
    imgdata = base64.b64decode(imgsrting)
    with open(filename, 'wb') as file:
        file.write(imgdata)
        file.close()

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as file:
        return base64.b64encode(file.read())
