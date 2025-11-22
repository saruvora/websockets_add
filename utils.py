import yaml
from typing import Any

def load_yaml(file_path: str) -> Any:
    """Loads a YAML file into a Python dictionary."""
    try:
        with open(file_path, 'r') as file:
            # Use safe_load to securely parse the YAML data
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")
        return None