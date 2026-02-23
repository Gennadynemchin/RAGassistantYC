import os

from dotenv import load_dotenv
from yandex_ai_studio_sdk import AIStudio

load_dotenv()

FOLDER_ID = os.getenv("FOLDER_ID")
API_KEY = os.getenv("API_KEY")

DATA_DIR = "rebrain"
STATE_FILE = "state.json"

ASSISTANT_INSTRUCTION = (
    "Ты - опытный специалист, задача которого - консультировать пользователя "
    "в вопросах Kubernetes. Для ответов на вопросы используй только имеющуюся у тебя информацию."
)

sdk = AIStudio(folder_id=FOLDER_ID, auth=API_KEY)
sdk.setup_default_logging(log_level="INFO")
model = sdk.models.completions("yandexgpt", model_version="rc")
