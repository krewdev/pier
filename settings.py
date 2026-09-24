import os
from pathlib import Path

APP_NAME = "Pier"
APP_HOST = "127.0.0.1"
APP_PORT = 8787

ROOT = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("PIER_DATA_DIR", ROOT / "data"))
DB_PATH = Path(os.environ.get("PIER_DB", DATA_DIR / "pier.db"))
STATIC_DIR = ROOT / "static"

MAX_BODY_STORE = 1_000_000
REQUEST_TIMEOUT = 30.0
RATE_PROBE_MAX = 20
RATE_PROBE_SLEEP_S = 0.08

INTRUDER_MAX_REQUESTS = 200
INTRUDER_DEFAULT_REQUESTS = 50
INTRUDER_MAX_CONCURRENCY = 4
INTRUDER_MIN_DELAY_MS = 50
INTRUDER_MAX_DELAY_MS = 2000
INTRUDER_DEFAULT_DELAY_MS = 100
INTRUDER_MAX_PAYLOADS = 200
INTRUDER_PREVIEW_ROWS = 20

ALWAYS_ALLOWED_HOSTS = {"127.0.0.1", "localhost", "::1"}
SECRET_HEADERS = {"authorization", "cookie", "set-cookie", "x-api-key", "proxy-authorization"}
