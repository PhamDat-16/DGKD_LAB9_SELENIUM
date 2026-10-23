# BÁO CÁO THỰC HÀNH LAB 9: KIỂM THỬ TỰ ĐỘNG WEB VỚI SELENIUM WEBDRIVER

---

## 📌 THÔNG TIN SINH VIÊN & BÀI THỰC HÀNH
- **Họ và tên:** Phạm Văn Đạt
- **Mã sinh viên (MSSV):** 23017150
- **Lớp / Khóa:** K17-KHMT
- **Học phần:** Đảm bảo Chất lượng & Kiểm thử Phần mềm (Software Testing & QA)
- **Repository GitHub:** [https://github.com/PhamDat-16/DGKD_LAB9_SELENIUM](https://github.com/PhamDat-16/DGKD_LAB9_SELENIUM)
- **Website mục tiêu kiểm thử:** [Swag Labs (SauceDemo)](https://www.saucedemo.com/)
- **Công nghệ & Thư viện sử dụng:** `Python 3.11`, `Selenium WebDriver 4.x`, `Pytest 9.x`, `pytest-html`, `webdriver-manager`, `Chrome Headless/Headed`.

---

## 📖 1. TỔNG QUAN VỀ CÔNG CỤ SELENIUM & KIẾN TRÚC KIỂM THỬ

### 1.1. Giới thiệu Selenium WebDriver
**Selenium WebDriver** là công cụ kiểm thử tự động mã nguồn mở hàng đầu thế giới dành cho các ứng dụng web. Selenium cho phép lập trình viên mô phỏng chính xác các thao tác của người dùng thực tế trên trình duyệt (nhấp chuột, nhập liệu, cuộn trang, điều hướng, chọn dropdown, xử lý popup, kiểm tra cookie và phiên đăng nhập).
- **Giao thức chuẩn hóa W3C:** Selenium giao tiếp trực tiếp với trình duyệt thông qua ChromeDriver/GeckoDriver theo chuẩn WebDriver W3C, mang lại độ ổn định cao và tương thích đa nền tảng.
- **Hỗ trợ Headless Browser:** Cho phép thực thi toàn bộ kịch bản kiểm thử ngầm không cần hiển thị giao diện đồ họa, tối ưu tốc độ và sẵn sàng tích hợp vào pipeline CI/CD (GitHub Actions, Jenkins, GitLab CI).

### 1.2. Mô hình thiết kế Page Object Model (POM)
Dự án được xây dựng tuân thủ nghiêm ngặt theo mẫu thiết kế chuẩn công nghiệp **Page Object Model (POM)**:
- **Tách biệt giao diện và logic kiểm thử:** Mỗi trang web (hoặc thành phần giao diện) được đóng gói thành một class Python riêng biệt trong thư mục `pages/` (chứa các định vị Locators và phương thức tương tác).
- **Dễ bảo trì và tái sử dụng:** Khi giao diện người dùng thay đổi (đổi ID, Class, XPath), lập trình viên chỉ cần cập nhật ở duy nhất Page Object tương ứng mà không phải sửa hàng chục Test Script.
- **Khắc phục triệt để vấn đề React 18 State:** Triển khai cơ chế *Native Value Setter* trong `BasePage` để kích hoạt sự kiện `input` và `change` của các React Controlled Inputs, đảm bảo form nhập liệu luôn được đồng bộ trạng thái chính xác.

---

## 🎯 2. DANH SÁCH & ĐẶC TẢ CHI TIẾT CÁC TEST CASES

Dự án triển khai **07 Test Cases** hoàn chỉnh (vượt mức tối thiểu 05 TC theo yêu cầu đề bài), bao gồm cả kiểm thử chức năng tích cực (Positive Testing) và kiểm thử phủ định (Negative Testing).

### 2.1. Bảng tổng hợp Test Cases

| Mã TC | Tên Kịch Bản Kiểm Thử | Mục Tiêu & Chức Năng | Loại Test | Kết Quả Thực Tế | Trạng Thái |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **TC01** | `test_tc01_login_with_valid_credentials` | Đăng nhập tài khoản hợp lệ (`standard_user`) | Chức năng (Positive) | Chuyển hướng sang `/inventory.html`, tiêu đề "Products" | **PASSED** |
| **TC02** | `test_tc02_login_wrong_password`<br>`test_tc02_login_locked_out_user` | Đăng nhập sai mật khẩu & Đăng nhập tài khoản bị khóa (`locked_out_user`) | Phủ định (Negative) | Báo lỗi đúng thông điệp, chặn chuyển hướng | **PASSED** |
| **TC03** | `test_tc03_sort_price_low_to_high`<br>`test_tc03_sort_name_z_to_a` | Sắp xếp sản phẩm theo Giá (Thấp $\to$ Cao) và Tên (Z $\to$ A) | Chức năng & Dữ liệu | Danh sách sản phẩm được sort chuẩn xác 100% | **PASSED** |
| **TC04** | `test_tc04_add_single_product_to_cart`<br>`test_tc04_add_multiple_products_to_cart` | Thêm 1 sản phẩm & Thêm nhiều sản phẩm vào giỏ hàng | Chức năng & Giỏ hàng | Badge giỏ hàng cập nhật tăng dần chính xác (1, 2, 3) | **PASSED** |
| **TC05** | `test_tc05_complete_checkout_flow` | Toàn bộ quy trình Giỏ hàng $\to$ Điền Form $\to$ Tính Thuế/Tổng $\to$ Đặt hàng | E2E Flow (Quy trình) | Hoàn tất đơn hàng với thông báo "Thank you for your order!" | **PASSED** |
| **TC06** | `test_tc06_remove_product_on_inventory_page`<br>`test_tc06_remove_product_inside_cart_page` | Xóa sản phẩm khỏi giỏ hàng ngay tại trang Inventory và trong trang Cart | Chức năng & Giỏ hàng | Sản phẩm bị loại bỏ, badge giảm và ẩn khi về 0 | **PASSED** |
| **TC07** | `test_tc07_logout_successfully` | Đăng xuất an toàn qua Burger Menu và bảo mật phiên đăng nhập | Bảo mật & Phiên | Về trang Login, xóa phiên, chặn truy cập trực tiếp | **PASSED** |

---

### 2.2. Đặc tả chi tiết từng Test Case

#### 🔹 TC01: Đăng nhập thành công với tài khoản hợp lệ
- **Tiền điều kiện:** Trình duyệt mở trang `https://www.saucedemo.com/`.
- **Các bước thực hiện:**
  1. Nhập Username: `standard_user`.
  2. Nhập Password: `secret_sauce`.
  3. Nhấp nút **Login**.
- **Kết quả mong đợi:** 
  - URL chuyển hướng đến `https://www.saucedemo.com/inventory.html`.
  - Tiêu đề trang hiển thị chuỗi `"Products"`.
  - Icon giỏ hàng hiển thị trạng thái ban đầu (badge = 0).

#### 🔹 TC02: Đăng nhập thất bại (Negative Testing)
- **Tiền điều kiện:** Mở trang đăng nhập.
- **Kịch bản 2.1 (Sai mật khẩu):**
  - Nhập `standard_user` và mật khẩu không đúng: `wrong_password_123`.
  - Nhấp nút **Login**.
  - **Kỳ vọng:** Hiển thị thông báo lỗi `Epic sadface: Username and password do not match any user in this service`, giữ nguyên URL tại trang đăng nhập.
- **Kịch bản 2.2 (Tài khoản bị khóa):**
  - Nhập tài khoản bị khóa: `locked_out_user` và mật khẩu `secret_sauce`.
  - Nhấp nút **Login**.
  - **Kỳ vọng:** Hiển thị thông báo lỗi `Epic sadface: Sorry, this user has been locked out.`, không cho phép truy cập hệ thống.

#### 🔹 TC03: Lọc và Sắp xếp danh sách sản phẩm
- **Tiền điều kiện:** Đã đăng nhập vào trang `/inventory.html`.
- **Kịch bản 3.1 (Lọc giá từ Thấp đến Cao):**
  - Chọn option `lohi` trên dropdown sắp xếp (`.product_sort_container`).
  - Lấy toàn bộ danh sách giá sản phẩm hiển thị.
  - **Kỳ vọng:** Danh sách giá sau khi lọc thỏa mãn điều kiện tăng dần: $P_1 \le P_2 \le \dots \le P_n$.
- **Kịch bản 3.2 (Sắp xếp Tên từ Z đến A):**
  - Chọn option `za` trên dropdown sắp xếp.
  - Lấy toàn bộ danh sách tên sản phẩm hiển thị.
  - **Kỳ vọng:** Danh sách tên tuân theo thứ tự bảng chữ cái giảm dần từ Z đến A.

#### 🔹 TC04: Thêm sản phẩm vào giỏ hàng & Cập nhật số lượng
- **Tiền điều kiện:** Người dùng đang ở trang danh mục sản phẩm.
- **Các bước thực hiện:**
  1. Nhấp nút **Add to cart** cho sản phẩm `Sauce Labs Backpack` $\to$ Kiểm tra badge giỏ hàng hiển thị số `1`.
  2. Nhấp nút **Add to cart** cho sản phẩm `Sauce Labs Bike Light` $\to$ Kiểm tra badge giỏ hàng cập nhật lên số `2`.
  3. Nhấp nút **Add to cart** cho sản phẩm `Sauce Labs Bolt T-Shirt` $\to$ Kiểm tra badge giỏ hàng cập nhật lên số `3`.
- **Kết quả mong đợi:** Icon giỏ hàng hiển thị badge đồng bộ đúng số lượng sản phẩm được thêm vào.

#### 🔹 TC05: Kiểm tra giỏ hàng và Quy trình đặt hàng hoàn tất (Checkout End-to-End)
- **Tiền điều kiện:** Đã thêm 2 sản phẩm vào giỏ hàng.
- **Các bước thực hiện:**
  1. Nhấp vào icon giỏ hàng $\to$ Điều hướng tới `/cart.html`.
  2. Xác nhận đúng tên 2 sản phẩm trong giỏ: `Sauce Labs Backpack` và `Sauce Labs Fleece Jacket`.
  3. Nhấp nút **Checkout** $\to$ Chuyển sang `/checkout-step-one.html`.
  4. Điền thông tin giao hàng: First Name (`Dat`), Last Name (`Pham`), Zip/Postal Code (`100000`).
  5. Nhấp **Continue** $\to$ Chuyển sang trang xem lại đơn hàng `/checkout-step-two.html`.
  6. Kiểm tra công thức tài chính: $\text{Item total} + \text{Tax} = \text{Total}$.
  7. Nhấp nút **Finish** $\to$ Chuyển sang `/checkout-complete.html`.
- **Kết quả mong đợi:** Màn hình hiển thị thông báo chúc mừng `Thank you for your order!` và nút `Back Home`.

#### 🔹 TC06: Xóa sản phẩm khỏi giỏ hàng
- **Kịch bản 6.1 (Xóa tại trang Inventory):**
  - Thêm sản phẩm $\to$ Nút chuyển thành `Remove`.
  - Nhấp nút `Remove` ngay tại sản phẩm $\to$ Badge giỏ hàng biến mất (về 0).
- **Kịch bản 6.2 (Xóa bên trong trang Cart):**
  - Thêm 2 sản phẩm, vào trang `/cart.html`.
  - Nhấp `Remove` của sản phẩm thứ nhất.
  - **Kỳ vọng:** Sản phẩm thứ nhất biến mất khỏi bảng, sản phẩm thứ hai được giữ nguyên, badge giỏ hàng giảm từ 2 xuống 1.

#### 🔹 TC07: Đăng xuất an toàn & Hủy phiên làm việc
- **Tiền điều kiện:** Đang đăng nhập trong hệ thống.
- **Các bước thực hiện:**
  1. Nhấp vào nút mở Menu Burger bên góc trái.
  2. Chờ hiệu ứng chuyển động và nhấp vào liên kết **Logout**.
- **Kết quả mong đợi:**
  - Trình duyệt chuyển hướng về trang chủ `https://www.saucedemo.com/`.
  - Nút **Login** hiển thị trở lại.
  - Khi cố tình gõ trực tiếp URL `https://www.saucedemo.com/inventory.html`, hệ thống tự động ngăn chặn và yêu cầu đăng nhập lại (bảo vệ Session).

---

## 📂 3. CẤU TRÚC THƯ MỤC DỰ ÁN

```
DGKD_LAB9_SELENIUM/
│
├── README.md                              # Báo cáo thực hành chi tiết (File này)
├── requirements.txt                       # Danh sách thư viện phụ thuộc
├── conftest.py                            # Cấu hình Pytest Fixtures, WebDriver & Screenshot
├── pytest.ini                             # File cấu hình Pytest & HTML Reporting
├── run_tests.py                           # Script thực thi toàn bộ kịch bản kiểm thử một chạm
│
├── pages/                                 # Page Object Model (POM)
│   ├── __init__.py
│   ├── base_page.py                       # Base Page đóng gói Explicit Waits & React Input
│   ├── login_page.py                      # Trang Đăng nhập (Locators & Actions)
│   ├── inventory_page.py                  # Trang Danh sách sản phẩm & Menu
│   ├── cart_page.py                       # Trang Giỏ hàng
│   └── checkout_page.py                   # Trang Thanh toán & Hoàn tất đơn hàng
│
├── tests/                                 # Thư mục chứa 07 Test Cases tự động
│   ├── __init__.py
│   ├── test_tc01_login_success.py         # TC01: Đăng nhập thành công
│   ├── test_tc02_login_invalid.py         # TC02: Đăng nhập thất bại (Negative Test)
│   ├── test_tc03_product_sorting.py       # TC03: Sắp xếp sản phẩm theo Giá và Tên
│   ├── test_tc04_add_to_cart.py           # TC04: Thêm sản phẩm vào giỏ hàng
│   ├── test_tc05_cart_and_checkout.py     # TC05: Kiểm tra giỏ hàng và Thanh toán E2E
│   ├── test_tc06_remove_from_cart.py      # TC06: Xóa sản phẩm khỏi giỏ hàng
│   └── test_tc07_logout.py                # TC07: Đăng xuất an toàn & Kiểm tra phiên
│
└── reports/                               # Thư mục lưu kết quả kiểm thử tự động
    ├── test_report.html                   # File báo cáo HTML sinh động trực quan
    └── screenshots/                       # Ảnh chụp màn hình bằng chứng từng Test Case
        ├── test_tc01_login_with_valid_credentials_*.png
        ├── test_tc02_login_locked_out_user_*.png
        ├── test_tc02_login_wrong_password_*.png
        ├── test_tc03_sort_name_z_to_a_*.png
        ├── test_tc03_sort_price_low_to_high_*.png
        ├── test_tc04_add_multiple_products_to_cart_*.png
        ├── test_tc04_add_single_product_to_cart_*.png
        ├── test_tc05_complete_checkout_flow_*.png
        ├── test_tc06_remove_product_inside_cart_page_*.png
        ├── test_tc06_remove_product_on_inventory_page_*.png
        └── test_tc07_logout_successfully_*.png
```

---

## 🚀 4. HƯỚNG DẪN CÀI ĐẶT & CHẠY KIỂM THỬ

### 4.1. Chuẩn bị môi trường
1. Máy tính đã cài đặt **Python 3.10+** và trình duyệt **Google Chrome**.
2. Clone repository về máy tính:
   ```bash
   git clone https://github.com/PhamDat-16/DGKD_LAB9_SELENIUM.git
   cd DGKD_LAB9_SELENIUM
   ```
3. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

### 4.2. Chạy kiểm thử tự động

- **Cách 1: Chạy nhanh qua script tự động (Khuyến nghị - Headless mode):**
  ```bash
  python run_tests.py
  ```
  *Hệ thống sẽ chạy toàn bộ 11 test steps ngầm trong background và tự động xuất báo cáo HTML.*

- **Cách 2: Chạy kiểm thử có hiển thị giao diện trình duyệt (Headed mode):**
  ```bash
  python run_tests.py --headed
  ```
  *Người kiểm thử có thể trực tiếp quan sát trình duyệt Chrome tự động mở, nhập liệu và click.*

- **Cách 3: Chạy trực tiếp thông qua Pytest:**
  ```bash
  pytest -v -s --html=reports/test_report.html --self-contained-html
  ```

---

## 📊 5. KẾT QUẢ KIỂM THỬ THỰC TẾ

### 5.1. Bảng tổng kết số liệu
- **Tổng số kịch bản kiểm thử (Test functions):** `11 tests` (thuộc 7 nhóm Test Cases lớn).
- **Số test case Passed (Thành công):** `11 / 11 (100%)`.
- **Số test case Failed (Thất bại):** `0`.
- **Thời gian thực thi trung bình:** `~80 - 85 giây`.
- **Báo cáo trực quan HTML:** Đã tạo thành công tại `reports/test_report.html`.

### 5.2. Nhật ký thực thi (Execution Log)
```text
============================= test session starts =============================
platform win32 -- Python 3.11.5, pytest-9.1.1, pluggy-1.7.0
rootdir: D:\DGKD_LAB9_SELENIUM
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.9.0, html-4.2.0, metadata-3.1.1
collected 11 items

tests/test_tc01_login_success.py::TestLoginSuccess::test_tc01_login_with_valid_credentials PASSED
tests/test_tc02_login_invalid.py::TestLoginInvalid::test_tc02_login_wrong_password PASSED
tests/test_tc02_login_invalid.py::TestLoginInvalid::test_tc02_login_locked_out_user PASSED
tests/test_tc03_product_sorting.py::TestProductSorting::test_tc03_sort_price_low_to_high PASSED
tests/test_tc03_product_sorting.py::TestProductSorting::test_tc03_sort_name_z_to_a PASSED
tests/test_tc04_add_to_cart.py::TestAddToCart::test_tc04_add_single_product_to_cart PASSED
tests/test_tc04_add_multiple_products_to_cart PASSED
tests/test_tc05_cart_and_checkout.py::TestCartAndCheckout::test_tc05_complete_checkout_flow PASSED
tests/test_tc06_remove_from_cart.py::TestRemoveFromCart::test_tc06_remove_product_on_inventory_page PASSED
tests/test_tc06_remove_from_cart.py::TestRemoveFromCart::test_tc06_remove_product_inside_cart_page PASSED
tests/test_tc07_logout.py::TestLogout::test_tc07_logout_successfully PASSED

- Generated html report: file:///D:/DGKD_LAB9_SELENIUM/reports/test_report.html -
======================== 11 passed in 84.65s (0:01:24) ========================
```

---

## 💡 6. KẾT LUẬN & BÀI HỌC KINH NGHIỆM

1. **Hiểu sâu về cơ chế đồng bộ hóa bất đồng bộ (Asynchronous Web):**
   - Hạn chế tối đa sử dụng `time.sleep()` cố định. Thay vào đó, áp dụng **Explicit Waits (`WebDriverWait` kết hợp `expected_conditions`)** giúp kịch bản kiểm thử chạy nhanh hơn, không bị giật lag và chỉ chờ khi phần tử thực sự sẵn sàng.
2. **Kỹ thuật xử lý Single Page Application (SPA & React):**
   - Các ứng dụng hiện đại sử dụng React Controlled Components kiểm soát `value` qua state. Việc kết hợp Javascript Executor và `Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set` giải quyết triệt để lỗi mất dữ liệu khi nhập form.
3. **Lợi ích to lớn của tự động hóa:**
   - Thay vì kiểm thử thủ công tốn hàng chục phút mỗi lần phát hành sản phẩm mới, bộ kiểm thử Selenium tự động chạy toàn bộ quy trình chỉ trong hơn 1 phút, phát hiện sớm các lỗi hồi quy (Regression Bugs), đảm bảo chất lượng phần mềm luôn đạt chuẩn cao nhất.
