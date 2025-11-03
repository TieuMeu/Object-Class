#Tạo class Calculator có các methods add, subtract, multiply, divide.

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Lỗi: Không thể chia cho 0"
        return a / b

if __name__ == "__main__":
    may_tinh = Calculator()

    print("Kết quả :")
    print(f"Cộng: {may_tinh.add(7, 2)}")
    print(f"Trừ: {may_tinh.subtract(7, 2)}")
    print(f"Nhân: {may_tinh.multiply(7, 2)}")
    print(f"Chia: {may_tinh.divide(7, 0)}")