import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(autouse=True)
def cookies(page):
    page.goto("https://www.seznam.cz/")

    cookie_banner = page.locator('[data-testid="cwl-dialog-headline"]')
    cookie_banner.click()

    button_refuse = page.locator("text='Souhlasím'")
    button_refuse.click()
