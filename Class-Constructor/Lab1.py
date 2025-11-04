#Viết class Car có constructor nhận vào brand, model, year. In thông tin xe khi tạo.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        print(f"Xe đã được tạo: {self.brand} {self.model} ({self.year})")

if __name__ == "__main__":
    car = Car("Hang1", "mohinh2", 2023)
