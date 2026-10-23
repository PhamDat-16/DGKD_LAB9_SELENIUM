import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogout:
    """TC07: Kiểm thử chức năng Đăng xuất an toàn và hủy phiên làm việc."""

    def test_tc07_logout_successfully(self, driver):
        # 1. Đăng nhập vào hệ thống
        login_page = LoginPage(driver).open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_on_inventory_page()

        # 2. Thực hiện đăng xuất qua menu
        inventory_page.open_menu_and_logout()

        # 3. Xác minh đã trở về trang đăng nhập
        assert login_page.is_login_button_displayed(), \
            "Trang đăng nhập chưa hiển thị nút Login sau khi đăng xuất!"
        assert "inventory.html" not in driver.current_url, \
            f"Vẫn còn ở trang inventory sau khi đăng xuất! URL: {driver.current_url}"

        # 4. Thử truy cập lại trực tiếp vào trang inventory xem có bị chặn không
        driver.get("https://www.saucedemo.com/inventory.html")
        assert login_page.is_login_button_displayed() or "inventory.html" not in driver.current_url, \
            "Lỗ hổng bảo mật: Người dùng có thể quay lại trang sản phẩm sau khi đã đăng xuất!"
