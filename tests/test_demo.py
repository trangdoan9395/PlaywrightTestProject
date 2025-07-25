from playwright.sync_api import sync_playwright, Page, expect
import pytest

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, timeout=60000)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    browser.close()

