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

    DOZN_URL = "https://test-gw-firm.dozn.co.kr"
    DOZN_PRIVATE_URL = "https://test-firmapi.dozn.co.kr"
    DOZN_API_KEY = "bc91572c-77bf-492b-afec-8e8ada809550"
    DOZN_ORG_CODE = "10000292"


@dataclass
class LocalConfig(Config):
    DB_ECHO: bool = True
    CONSOLE_WRITE: bool = True


@dataclass
class ProdConfig(Config):
    DOCS_URL: str = None
    DOZN_URL = "https://firmapi-pub.dozn.co.kr"
    DOZN_PRIVATE_URL = "https://firmapi.dozn.co.kr"
    DOZN_API_KEY = "90ab5b89-ecc5-4479-9c19-a3ec0f8388ef"
    DOZN_ORG_CODE = "10000292"


@dataclass
class DevConfig(Config):
    DOCS_URL: str = None


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(base=Config(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))
