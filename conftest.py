import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Chạy trình duyệt có giao diện (headed mode), mặc định là headless"
    )

@pytest.fixture(scope="session")
def report_dirs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reports_dir = os.path.join(base_dir, "reports")
    screenshots_dir = os.path.join(reports_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    return {"reports": reports_dir, "screenshots": screenshots_dir}

@pytest.fixture(scope="function")
def driver(request, report_dirs):
    is_headed = request.config.getoption("--headed")
    
    options = Options()
    if not is_headed:
        options.add_argument("--headless=new")
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")

    service = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=service, options=options)
    _driver.implicitly_wait(5)

    yield _driver

    # Chụp ảnh bằng chứng trước khi đóng trình duyệt
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(report_dirs["screenshots"], f"{test_name}_{timestamp}.png")
    try:
        _driver.save_screenshot(screenshot_path)
    except Exception:
        pass

    _driver.quit()
