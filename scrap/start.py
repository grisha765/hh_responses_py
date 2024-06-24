from config import logging_config
logging = logging_config.setup_logging(__name__)

async def prepare_page(page):
    logging.info("Navigating to hh.ru...")
    await page.goto('https://spb.hh.ru/account/login', wait_until='domcontentloaded')

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
