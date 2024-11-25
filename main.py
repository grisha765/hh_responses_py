import asyncio
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

logging.info(f"Script initialization, logging level: {Config.log_level}")
logging.debug(f"tests: {Config.tests}")
logging.debug(f"chrome_path: {Config.chrome_path}")
logging.debug(f"tgbot_pass: {Config.tgbot_pass}")

if __name__ == '__main__':
    if Config.tests == "True":
        from tests.run import run
        asyncio.run(run())
    else:
        from core.base import main
        asyncio.run(main())
