#Viết class Laptop với các getter/setter kiểm soát hợp lệ: price > 0, brand không rỗng.

class Laptop:
    def __init__(self, brand, price):
        self._brand = None
        self._price = None
        self.brand = brand
        self.price = price

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value.strip():
            self._brand = value
        else:
            print("không để trống")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Gias bes hown 0 ?????")

if __name__ == "__main__":
    may_tinh = Laptop("Asus", 18500000)
    print(f"Thương hiệu: {may_tinh.brand}, Giá: {may_tinh.price:,} VND")

    may_tinh.price = -464  
    may_tinh.brand = ""     