import os
from pathlib import Path
from typing import Final
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT: Final[Path] = Path(__file__).parent.parent.parent
DATA_DIR: Final[Path] = PROJECT_ROOT / 'data'

RPA_CHALLENGE_URL: Final[str] = os.getenv("RPA_CHALLENGE_URL", "https://www.rpachallenge.com/")
DEFAULT_TIMEOUT: Final[int] = int(os.getenv("DEFAULT_TIMEOUT", "5000"))
SUBMIT_TIMEOUT: Final[int] = int(os.getenv("SUBMIT_TIMEOUT", "5000"))