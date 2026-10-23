import sys
import subprocess
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

project_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_root)
if project_root not in sys.path:
    sys.path.insert(0, project_root)



def main():
    print("=" * 70)
    print("  CHẠY TỰ ĐỘNG BỘ KIỂM THỬ SELENIUM - LAB 9 (SWAG LABS)")
    print("  Sinh viên: Phạm Văn Đạt - MSSV: 23017150 - Lớp: K17-KHMT")
    print("=" * 70)

    # Đảm bảo thư mục reports tồn tại
    os.makedirs("reports/screenshots", exist_ok=True)

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-v",
        "-s",
        "--html=reports/test_report.html",
        "--self-contained-html"
    ]

    # Nhận cờ --headed nếu người dùng muốn bật giao diện trình duyệt
    if "--headed" in sys.argv:
        cmd.append("--headed")

    result = subprocess.run(cmd)
    
    print("\n" + "=" * 70)
    if result.returncode == 0:
        print("  KẾT QUẢ: TẤT CẢ TEST CASES ĐỀU ĐẠT (ALL PASSED)! ")
    else:
        print(f"  KẾT QUẢ: CÓ TEST CASE THẤT BẠI (Mã lỗi: {result.returncode})")
    print("  Báo cáo HTML chi tiết được lưu tại: reports/test_report.html")
    print("  Ảnh chụp màn hình được lưu tại     : reports/screenshots/")
    print("=" * 70)

    return result.returncode

if __name__ == "__main__":
    sys.exit(main())
