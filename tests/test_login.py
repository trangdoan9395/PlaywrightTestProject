# test_login.py
from pydoc import pager

from conftest import page # Import the page fixture from conftest.py
from playwright.sync_api import Page, expect, BrowserContext  # Chỉ cần Page và expect
import pytest

from defPage.loginPage import LoginPage # Đảm bảo import đúng đường dẫn và tên file (LoginPage.py)

# test_login cần nhận 'page' từ fixture, không phải 'browser'
@pytest.mark.usefixtures("page")  # Sử dụng fixture 'page' từ conftest.py
def test_login(page: Page):
    # Truyền đối tượng 'page' vào constructor của LoginPage
    login_page = LoginPage(page)

    # Gọi phương thức để điều hướng đến trang đăng nhập
    login_page.navigate_to_login_page()
    # Thực hiện các bước đăng nhập
    login_page.login("Admin", "admin123")  # Thay thế bằng thông tin




