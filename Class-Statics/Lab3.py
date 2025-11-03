#Tạo class Config với các biến static lưu thông tin cấu hình hệ thống (APP_NAME, VERSION).
# Viết hàm in cấu hình.


class Config:
    APP_NAME = "Hệ thống Quản lý Nigga"
    VERSION = "1.1.1.11.1.1.1.1.1.1.1"

    @staticmethod
    def show_config():
        print(f"Tên ứng dụng: {Config.APP_NAME}, Phiên bản: {Config.VERSION}")

# Kiểm tra
if __name__ == "__main__":
    Config.show_config()