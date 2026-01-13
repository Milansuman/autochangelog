from netra import Netra
from netra.instrumentation.instruments import InstrumentSet
import os
from dotenv import load_dotenv

load_dotenv()

NETRA_API_KEY = os.getenv("NETRA_API_KEY")
NETRA_ENDPOINT = os.getenv("NETRA_OTLP_ENDPOINT")

if not NETRA_API_KEY or not NETRA_ENDPOINT:
    raise ValueError("NETRA_API_KEY and NETRA_OTLP_ENDPOINT environment variables must be set.")

HEADERS = f"x-api-key={NETRA_API_KEY}"
def initialize_netra():
    Netra.init(
        app_name="kv-github-agent",
        headers=HEADERS,
        trace_content=True,
        disable_batch=True
    )