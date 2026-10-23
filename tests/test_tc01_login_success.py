import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLoginSuccess:
    """TC01: Kiểm thử Đăng nhập thành công với thông tin tài khoản hợp lệ."""

    def test_tc01_login_with_valid_credentials(self, driver):
        # 1. Khởi tạo Page Object và truy cập trang đăng nhập
        login_page = LoginPage(driver).open()

        # 2. Thực hiện đăng nhập với tài khoản hợp lệ
        login_page.login("standard_user", "secret_sauce")

        # 3. Khởi tạo Inventory Page và xác minh kết quả
        inventory_page = InventoryPage(driver)

        # Assertions
        assert inventory_page.is_on_inventory_page(), \
            f"Kỳ vọng chuyển hướng đến /inventory.html nhưng URL hiện tại là: {driver.current_url}"
        assert inventory_page.get_page_title() == "Products", \
            f"Kỳ vọng tiêu đề trang là 'Products' nhưng thực tế là: {inventory_page.get_page_title()}"
        assert inventory_page.get_cart_badge_count() == 0, \
            "Kỳ vọng giỏ hàng ban đầu chưa có sản phẩm (badge = 0)."
