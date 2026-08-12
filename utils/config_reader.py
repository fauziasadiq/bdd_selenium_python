import os
import yaml


def load_config():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    if os.getenv("CI") == "true":
        config["headless"] = True

    return config