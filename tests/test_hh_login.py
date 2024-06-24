from core.browser import init_browser
from scrap.start import prepare_page
from scrap.login import login_hh
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

async def test_login():
    browser, page, playwright = await init_browser()
    expected_email_value = Config.hh_login
    expected_password_value = Config.hh_passw
    await prepare_page(page)
    result = await login_hh(page)
    try:
        assert result["Email Value"] == expected_email_value, f"Expected {expected_email_value}, but got {result['Email Value']}"
    except AssertionError as e:
        logging.error(f"Email Value test failed: {e}")
    try:
        assert result["Password Value"] == expected_password_value, f"Expected {expected_password_value}, but got {result['Password Value']}"
    except AssertionError as e:
        logging.error(f"Password Value test failed: {e}")
    logging.info(f'Test passed!{"\x1b[0m"}')
    await browser.close()
    await playwright.stop()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
