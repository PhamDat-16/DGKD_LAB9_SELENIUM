from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    """Lớp cơ sở đóng gói các thao tác thường dùng trên trình duyệt với Explicit Waits."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()
        return elem

    def js_click(self, locator):
        elem = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", elem)
        return elem

    def react_input(self, locator, value):
        """Nhập liệu tương thích với React controlled components bằng Native Value Setter."""
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("""
            var element = arguments[0];
            var value = arguments[1];
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeInputValueSetter.call(element, value);
            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
        """, elem, value)
        return elem

    def input_text(self, locator, text, clear_first=True):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            elem.clear()
        elem.send_keys(text)
        return elem

    def get_text(self, locator):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        return elem.text.strip()

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def wait_url_contains(self, partial_url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))

    def take_screenshot(self, filepath):
        self.driver.save_screenshot(filepath)
