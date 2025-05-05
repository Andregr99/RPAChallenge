import os
from pathlib import Path

class Settings:
    BASE_URL = "http://rpachallenge.com"
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # Paths
    DATA_DIR = BASE_DIR / "data"
    LOGS_DIR = BASE_DIR / "logs"
    RESULTS_DIR = BASE_DIR / "results"
    
    # Files
    DOWNLOAD_PATH = DATA_DIR / "challenge.xlsx"
    RESULTS_PATH = RESULTS_DIR / "results.xlsx"
    
    # Timeouts
    TIMEOUT = 5000  
    DELAY = 0.5  
    SHUTDOWN_DELAY = 3 
    
    # Browser
    HEADLESS = False
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
    def __init__(self):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        os.makedirs(self.LOGS_DIR, exist_ok=True)
        os.makedirs(self.RESULTS_DIR, exist_ok=True)