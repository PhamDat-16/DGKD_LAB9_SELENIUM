from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Locators Step One
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")

    # Locators Step Two
    ITEM_TOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BTN = (By.ID, "finish")

    # Locators Complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_information(self, first_name, last_name, postal_code):
        self.react_input(self.FIRST_NAME_INPUT, first_name)
        self.react_input(self.LAST_NAME_INPUT, last_name)
        self.react_input(self.POSTAL_CODE_INPUT, postal_code)
        self.js_click(self.CONTINUE_BTN)
        self.wait_url_contains("/checkout-step-two.html")
        return self

    def get_summary_subtotal(self):
        text = self.get_text(self.ITEM_TOTAL_LABEL)
        return float(text.replace("Item total: $", "").strip())

    def get_summary_tax(self):
        text = self.get_text(self.TAX_LABEL)
        return float(text.replace("Tax: $", "").strip())

    def get_summary_total(self):
        text = self.get_text(self.TOTAL_LABEL)
        return float(text.replace("Total: $", "").strip())

    def click_finish(self):
        self.js_click(self.FINISH_BTN)
        self.wait_url_contains("/checkout-complete.html")
        return self

    def get_complete_header_text(self):
        return self.get_text(self.COMPLETE_HEADER)

    def is_order_complete(self):
        return self.wait_url_contains("/checkout-complete.html") and \
               self.get_complete_header_text() == "Thank you for your order!"
