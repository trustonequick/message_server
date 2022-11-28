from dataclasses import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir
    DEBUG: bool = False
    CONSOLE_WRITE: bool = False
    TEST_MODE: bool = False
    DOCS_URL: str = "/docs"
    TRUSTED_HOST = ["*"]
    ALLOW_SITE = ["*"]


@dataclass
class LocalConfig(Config):
    DB_ECHO: bool = True
    CONSOLE_WRITE: bool = True


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(base=Config(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
