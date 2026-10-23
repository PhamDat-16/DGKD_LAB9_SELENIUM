import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestAddToCart:
    """TC04: Kiểm thử chức năng Thêm sản phẩm vào giỏ hàng."""

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(driver)
        assert self.inventory_page.is_on_inventory_page()

    def test_tc04_add_single_product_to_cart(self, driver):
        """Thêm 1 sản phẩm và kiểm tra badge giỏ hàng."""
        product_name = "Sauce Labs Backpack"
        self.inventory_page.add_product_to_cart_by_name(product_name)

        badge_count = self.inventory_page.get_cart_badge_count()
        assert badge_count == 1, \
            f"Kỳ vọng badge giỏ hàng là 1 sau khi thêm sản phẩm nhưng thực tế là: {badge_count}"

    def test_tc04_add_multiple_products_to_cart(self, driver):
        """Thêm nhiều sản phẩm và kiểm tra số lượng tăng dần."""
        self.inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")
        assert self.inventory_page.get_cart_badge_count() == 1

        self.inventory_page.add_product_to_cart_by_name("Sauce Labs Bike Light")
        assert self.inventory_page.get_cart_badge_count() == 2

        self.inventory_page.add_product_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        assert self.inventory_page.get_cart_badge_count() == 3
