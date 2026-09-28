import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ENVIRONMENT = os.getenv("ENVIRONMENT", "cloud")

USE_AI = ENVIRONMENT == "local"

AI_ENABLED = os.getenv("AI_ENABLED", "false").lower() == "true"

LLM_MODEL = os.getenv("LLM_MODEL", "qwen3:8b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "bge-m3:latest")

BASE_DIR = os.getenv("BASE_DIR", Path(__file__).resolve().parents[1])

DB_PATH = Path(
    os.getenv("DB_PATH", str(BASE_DIR / "chroma_db"))
)