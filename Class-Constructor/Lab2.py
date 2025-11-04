#Tạo class User có 2 constructor: mặc định và có tham số.
# Viết chương trình tạo danh sách người dùng.

class User:
    def __init__(self, name=None, age=None):
        self.name = name or "Khách"
        self.age = age or 0

    def __repr__(self):
        return f"{self.name} ({self.age} tuổi)"

if __name__ == "__main__":
    user_list = [User(), User("Nguyễn Văn A", 21), User("Trần Thị B", 30)]
    print("Danh sách người dùng:", user_list)