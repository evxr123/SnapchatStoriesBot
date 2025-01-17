import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "27861872"))
    API_HASH = os.environ.get("API_HASH", "29a5d982bfd2b0a06dddb1f85361cfa9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7505512532:AAFp3nTU6iw9DOGITcaWrgsHAUgTfpR15Mg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Kali_Devbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
