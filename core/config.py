import os 
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / '.env'
load_dotenv(dotenv_path= env_path)

class Settings():
    PROJECT_NAME:str = "PROYECTO-FAST-API"
    PROJECT_VERSION:str = "1.0"
    POSTGRES_DB:str = os.getenv("POSTGRES_DB")
    POSTGRES_USER:str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT:str = os.getenv("POSTGRES_PORT")
    DATBASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()

class Settings_get():
    PROJECT_NAME:str = "PROYECTO-FAST-API"
    PROJECT_VERSION:str = "1.0"
    POSTGRES_DB1:str = os.getenv("POSTGRES_DB1")
    POSTGRES_USER1:str = os.getenv("POSTGRES_USER1")
    POSTGRES_PASSWORD1:str = os.getenv("POSTGRES_PASSWORD1")
    POSTGRES_SERVER1:str = os.getenv("POSTGRES_SERVER1")
    POSTGRES_PORT1:str = os.getenv("POSTGRES_PORT1")
    DATABASE_GET = f"postgresql://{POSTGRES_USER1}:{POSTGRES_PASSWORD1}@{POSTGRES_SERVER1}:{POSTGRES_PORT1}/{POSTGRES_DB1}"

settings_get = Settings_get()