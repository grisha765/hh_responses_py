import asyncio
from core.screenshot import take_screenshot
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

async def login_hh(page):
    email_text = Config.hh_login

    logging.debug(f'Write the text {email_text} in the login field.')
    await asyncio.sleep(2)
    await page.fill('input[name="login"]', email_text)

    await page.locator("button:has-text('Продолжить')").click()
    await asyncio.sleep(3)

    captcha_locator = page.locator('input[name="captchaText"]')

    if await captcha_locator.is_visible():
        logging.warning("Capcha is detect!")
        await take_screenshot(page, "capcha.png")
        capcha_text = input("Enter the text from the image: ")
        await page.fill('input[name="captchaText"]', capcha_text)

        await page.locator("button:has-text('Продолжить')").click()

    await take_screenshot(page, "img.png")

    otp_text = input("Email otp: ")

    logging.debug(f'Write the text {otp_text} in the otp field.')
    await asyncio.sleep(2)
    await page.fill('input[name="otp-code-input"]', otp_text)

    await page.locator("button:has-text('Подтвердить')").click()
    await asyncio.sleep(2)
    await take_screenshot(page, "img.png")

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
