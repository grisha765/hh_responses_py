import asyncio
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

async def prepare_page(page, login: str = Config.hh_login, password: str = Config.hh_passw):
    logging.info("Navigating to hh.ru...")
    await page.goto('https://spb.hh.ru/account/login', wait_until='domcontentloaded')
    await page.wait_for_selector('button[data-qa="expand-login-by-password"]', timeout=60000)
    logging.debug('Click the button "Войти с паролем"')
    await page.click('button[data-qa="expand-login-by-password"]')
    email_text = login
    password_text = password
    logging.debug(f'Write the text {email_text} in the login field.')
    await asyncio.sleep(2)
    await page.fill('input[data-qa="login-input-username"]', email_text)
    logging.debug(f'Write the text {password_text} in the password field.')
    await asyncio.sleep(2)
    await page.fill('input[data-qa="login-input-password"]', password_text)
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
