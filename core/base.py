from core.browser import init_browser
from scrap.start import prepare_page

async def main():
    browser, page, playwright = await init_browser()
    await prepare_page(page)
    await browser.close()
    await playwright.stop()

if __name__ == '__main__':
    raise RuntimeError("This module should be run only via main.py")