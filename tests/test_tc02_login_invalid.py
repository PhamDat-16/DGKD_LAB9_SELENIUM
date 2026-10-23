import pytest
from pages.login_page import LoginPage

class TestLoginInvalid:
    """TC02: Kiểm thử Đăng nhập thất bại (Negative Testing) với dữ liệu không hợp lệ."""

    def test_tc02_login_wrong_password(self, driver):
        """Kiểm tra khi nhập sai mật khẩu."""
        login_page = LoginPage(driver).open()
        login_page.login("standard_user", "wrong_password_123")

        err_msg = login_page.get_error_message()
        assert "Username and password do not match" in err_msg, \
            f"Kỳ vọng thông báo sai mật khẩu nhưng nhận được: {err_msg}"
        assert "inventory.html" not in driver.current_url, \
            "Hệ thống không được phép chuyển hướng khi đăng nhập sai!"

    def test_tc02_login_locked_out_user(self, driver):
        """Kiểm tra khi tài khoản bị khóa."""
        login_page = LoginPage(driver).open()
        login_page.login("locked_out_user", "secret_sauce")

        err_msg = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in err_msg, \
            f"Kỳ vọng thông báo tài khoản bị khóa nhưng nhận được: {err_msg}"
        assert "inventory.html" not in driver.current_url, \
            "Tài khoản bị khóa không được phép đăng nhập vào hệ thống!"
