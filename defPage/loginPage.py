# defPage/LoginPage.py
from playwright.sync_api import Page, expect

class LoginPage:
# Thay đổi 'login' để sử dụng Playwright locators và fill/click
    def __init__(self, page: Page):
        self.page = page
    def navigate_to_login_page(self):
        # Sử dụng phương thức goto() để điều hướng đến trang đăng nhập
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    def login(self, username: str, password: str):
        # Sử dụng Playwright locators để tìm các trường nhập liệu và nút đăng nhập
        self.page.fill("//input[@placeholder ='Username']", username)
        self.page.fill("//input[@placeholder ='Password']", password)
        self.page.click("//button[text()= ' Login ']")

        # Kiểm tra xem đăng nhập có thành công không bằng cách xác nhận tiêu đề trang
        expect(self.page).to_have_title("OrangeHRM")

