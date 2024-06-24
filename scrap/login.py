import asyncio
from core.screenshot import take_screenshot
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

async def login_hh(page, login: str = Config.hh_login, password: str = Config.hh_passw):
    for attempt in range(3):
        try:
            await page.click('button[data-qa="expand-login-by-password"]')
            await asyncio.sleep(2)
            if not await page.is_visible('button[data-qa="expand-login-by-password"]'):
                break
        except Exception as e:
            logging.warning(f'Attempt {attempt + 1} failed with error: {e}')
            if attempt == 3 - 1:
                raise e

    email_text = login
    password_text = password

    logging.debug(f'Write the text {email_text} in the login field.')
    await asyncio.sleep(2)
    try:
        await page.fill('input[data-qa="login-input-username"]', email_text)
    except Exception as e:
        logging.error(f"Text login writing error: {e}")
        await take_screenshot(page, "tests/error_login.png")

    logging.debug(f'Write the text {password_text} in the password field.')
    await asyncio.sleep(2)
    try:
        await page.fill('input[data-qa="login-input-password"]', password_text)
    except Exception as e:
        logging.error(f"Text password writing error: {e}")
        await take_screenshot(page, "tests/error_password.png")

    email_placeholder = await page.get_attribute('input[data-qa="login-input-username"]', 'placeholder')
    email_value = await page.get_attribute('input[data-qa="login-input-username"]', 'value')
    password_placeholder = await page.get_attribute('input[data-qa="login-input-password"]', 'placeholder')
    password_value = await page.get_attribute('input[data-qa="login-input-password"]', 'value')

    return {"Email Placeholder": f"{email_placeholder}",
            "Email Value": f"{email_value}",
            "Password Placeholder": f"{password_placeholder}",
            "Password Value": f"{password_value}"}

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
