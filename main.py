from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

logging.info(f"Инициализация скрипта, уровень логгирования: {Config.log_level}")
logging.debug(f"chrome_path: {Config.chrome_path}")
logging.debug(f"tgbot_pass: {Config.tgbot_pass}")
