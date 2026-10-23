import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    URL_PATH = "/inventory.html"

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_SIDEBAR_LINK = (By.ID, "logout_sidebar_link")

    def is_on_inventory_page(self):
        return self.wait_url_contains(self.URL_PATH) and self.get_text(self.PAGE_TITLE) == "Products"

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def select_sort_option(self, option_value):
        """
        option_value:
          'az'   : Name (A to Z)
          'za'   : Name (Z to A)
          'lohi' : Price (low to high)
          'hilo' : Price (high to low)
        """
        dropdown = self.find(self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(option_value)
        return self

    def get_all_product_names(self):
        elements = self.find_all(self.ITEM_NAMES)
        return [elem.text.strip() for elem in elements]

    def get_all_product_prices(self):
        elements = self.find_all(self.ITEM_PRICES)
        return [float(elem.text.replace("$", "").strip()) for elem in elements]

    def add_product_to_cart_by_name(self, product_name):
        btn_locator = (
            By.XPATH,
            f"//div[contains(@class, 'inventory_item') and .//div[contains(@class, 'inventory_item_name') and text()='{product_name}']]//button"
        )
        self.js_click(btn_locator)
        return self

    def remove_product_from_inventory_by_name(self, product_name):
        btn_locator = (
            By.XPATH,
            f"//div[contains(@class, 'inventory_item') and .//div[contains(@class, 'inventory_item_name') and text()='{product_name}']]//button[text()='Remove']"
        )
        self.js_click(btn_locator)
        return self

    def get_cart_badge_count(self):
        if self.is_visible(self.CART_BADGE, timeout=2):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.js_click(self.CART_LINK)
        self.wait_url_contains("/cart.html")
        return self

    def open_menu_and_logout(self):
        self.js_click(self.BURGER_MENU_BTN)
        time.sleep(0.6)
        self.js_click(self.LOGOUT_SIDEBAR_LINK)
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        return self
