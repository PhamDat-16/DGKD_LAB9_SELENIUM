import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestProductSorting:
    """TC03: Kiểm thử chức năng sắp xếp và lọc sản phẩm."""

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(driver)
        assert self.inventory_page.is_on_inventory_page()

    def test_tc03_sort_price_low_to_high(self, driver):
        """Kiểm tra sắp xếp theo giá từ thấp đến cao (Price: low to high)."""
        self.inventory_page.select_sort_option("lohi")
        prices = self.inventory_page.get_all_product_prices()

        assert len(prices) > 0, "Danh sách sản phẩm không được rỗng!"
        assert prices == sorted(prices), \
            f"Danh sách giá sản phẩm chưa được sắp xếp tăng dần! Thực tế: {prices}"

    def test_tc03_sort_name_z_to_a(self, driver):
        """Kiểm tra sắp xếp theo tên từ Z đến A (Name: Z to A)."""
        self.inventory_page.select_sort_option("za")
        names = self.inventory_page.get_all_product_names()

        assert len(names) > 0, "Danh sách sản phẩm không được rỗng!"
        assert names == sorted(names, reverse=True), \
            f"Danh sách tên sản phẩm chưa được sắp xếp giảm dần Z-A! Thực tế: {names}"
