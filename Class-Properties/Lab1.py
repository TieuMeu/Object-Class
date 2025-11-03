#Tạo class Rectangle có fields width, height. Viết hàm tính diện tích, chu vi.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def dientich(self):
        return self.width * self.height
    def chuvi(self):
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    r = Rectangle(6, 2)
    print("Diện tịch :", r.dientich())
    print("Chu vi :", r.chuvi())