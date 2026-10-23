import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestRemoveFromCart:
    """TC06: Kiểm thử chức năng Xóa sản phẩm khỏi giỏ hàng."""

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(driver)
        assert self.inventory_page.is_on_inventory_page()

    def test_tc06_remove_product_on_inventory_page(self, driver):
        """Xóa sản phẩm ngay trên trang sản phẩm và kiểm tra badge giỏ hàng."""
        product_name = "Sauce Labs Backpack"
        # Thêm sản phẩm
        self.inventory_page.add_product_to_cart_by_name(product_name)
        assert self.inventory_page.get_cart_badge_count() == 1

        # Xóa sản phẩm
        self.inventory_page.remove_product_from_inventory_by_name(product_name)
        assert self.inventory_page.get_cart_badge_count() == 0, \
            "Badge giỏ hàng phải bằng 0 sau khi xóa sản phẩm duy nhất."

    def test_tc06_remove_product_inside_cart_page(self, driver):
        """Xóa sản phẩm bên trong trang Giỏ hàng /cart.html."""
        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Bike Light"

        self.inventory_page.add_product_to_cart_by_name(product_1)
        self.inventory_page.add_product_to_cart_by_name(product_2)
        assert self.inventory_page.get_cart_badge_count() == 2

        self.inventory_page.go_to_cart()
        cart_page = CartPage(driver)
        assert cart_page.is_on_cart_page()

        # Xóa product_1 khỏi giỏ
        cart_page.remove_item_by_name(product_1)
        remaining_items = cart_page.get_cart_item_names()

        assert product_1 not in remaining_items, f"{product_1} vẫn còn tồn tại trong giỏ hàng!"
        assert product_2 in remaining_items, f"{product_2} không được phép bị xóa nhầm!"
        assert self.inventory_page.get_cart_badge_count() == 1, \
            "Số lượng trên badge giỏ hàng phải giảm còn 1."
