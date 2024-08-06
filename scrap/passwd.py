import asyncio
from core.screenshot import take_screenshot
from config import logging_config
logging = logging_config.setup_logging(__name__)
async def login_password(page):
    try:
        logging.debug("Click login button...")
        await page.click('button[data-qa="account-login-submit"]')
    except Exception as e:
        logging.error(f"Error click button login: {e}")
        await take_screenshot(page, "tests/error_login.png")
    await asyncio.sleep(5)
    error_message = await page.query_selector('[data-qa="account-login-error"]')
    if error_message:
        logging.error("Error message found: Incorrect login details. Please try again.")
        await take_screenshot(page, "tests/error_password.png")
        return
    capcha_message = await page.query_selector('[data-qa="account-captcha-picture"]')
    if capcha_message:
        logging.error("Capcha message found")
        await take_screenshot(page, "tests/error_capcha.png")
        return
