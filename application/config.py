import os
from collections import defaultdict

from pydantic import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    WORKERS: int = 1


class ProdConfig(Config):
    ...


class DevConfig(Config):
    ...


class TestConfig(Config):
    TESTING = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    WORKERS: int = 1



def get_config():
    config_dict = defaultdict(lambda: TestConfig)
    config_dict["prod"] = ProdConfig
    config_dict["dev"] = DevConfig

    config_name = os.environ.get("FASTAPI_CONFIG")
    return config_dict[config_name]()