import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCartAndCheckout:
    """TC05: Kiểm thử toàn diện quy trình Giỏ hàng và Thanh toán đơn hàng."""

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.inventory_page = InventoryPage(driver)
        assert self.inventory_page.is_on_inventory_page()

    def test_tc05_complete_checkout_flow(self, driver):
        # 1. Thêm sản phẩm vào giỏ
        product_1 = "Sauce Labs Backpack"
        product_2 = "Sauce Labs Fleece Jacket"
        self.inventory_page.add_product_to_cart_by_name(product_1)
        self.inventory_page.add_product_to_cart_by_name(product_2)
        assert self.inventory_page.get_cart_badge_count() == 2

        # 2. Điều hướng vào trang giỏ hàng
        self.inventory_page.go_to_cart()
        cart_page = CartPage(driver)
        assert cart_page.is_on_cart_page(), "Không chuyển hướng được tới trang giỏ hàng /cart.html"

        # 3. Xác minh các sản phẩm trong giỏ
        cart_items = cart_page.get_cart_item_names()
        assert product_1 in cart_items, f"Thiếu {product_1} trong giỏ hàng!"
        assert product_2 in cart_items, f"Thiếu {product_2} trong giỏ hàng!"

        # 4. Tiến hành Checkout Step 1
        cart_page.click_checkout()
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_information("Dat", "Pham", "100000")

        # 5. Xác minh Step 2 (Tổng tiền & Thuế)
        subtotal = checkout_page.get_summary_subtotal()
        tax = checkout_page.get_summary_tax()
        total = checkout_page.get_summary_total()

        assert round(subtotal + tax, 2) == round(total, 2), \
            f"Tổng tiền tính toán sai: Subtotal({subtotal}) + Tax({tax}) != Total({total})"

        # 6. Hoàn tất đơn hàng
        checkout_page.click_finish()

        # 7. Xác nhận thông báo hoàn tất
        assert checkout_page.is_order_complete(), \
            f"Đơn hàng chưa hoàn tất thành công! Header: {checkout_page.get_complete_header_text()}"
