from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    URL_PATH = "/cart.html"

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def is_on_cart_page(self):
        return self.wait_url_contains(self.URL_PATH) and self.get_text(self.PAGE_TITLE) == "Your Cart"

    def get_cart_item_names(self):
        if not self.is_visible(self.CART_ITEMS, timeout=3):
            return []
        elements = self.find_all(self.CART_ITEM_NAMES)
        return [elem.text.strip() for elem in elements]

    def remove_item_by_name(self, product_name):
        remove_btn = (
            By.XPATH,
            f"//div[contains(@class, 'cart_item') and .//div[contains(@class, 'inventory_item_name') and text()='{product_name}']]//button[text()='Remove']"
        )
        self.js_click(remove_btn)
        return self

    def click_checkout(self):
        self.js_click(self.CHECKOUT_BTN)
        self.wait_url_contains("/checkout-step-one.html")
        return self

    def click_continue_shopping(self):
        self.js_click(self.CONTINUE_SHOPPING_BTN)
        return self
