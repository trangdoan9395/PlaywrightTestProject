from typing import Any, Generator

import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from playwright.sync_api import Playwright, expect

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests with: chromium, firefox, or webkit",
    )

@pytest.fixture(scope="session")
def browser(request):
     with sync_playwright() as playwright:
        browser_name = request.config.getoption("--browser")
        if browser_name == "firefox":
            browser = playwright.firefox.launch(headless=False, timeout=60000)
        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=False, timeout=60000)
        else: # Mặc định là Chromium
            browser = playwright.chromium.launch(headless=False, timeout=60000)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, Any, None]:
    page = browser.new_page()
    yield page
    page.close()

