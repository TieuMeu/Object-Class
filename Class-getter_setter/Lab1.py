#Tạo class Person có thuộc tính name, age. Viết getter/setter để đảm bảo age > 0.

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age  

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Tuổi phải là số dương!")

if __name__ == "__main__":
    nguoi = Person("Nguyễn Văn A", 643)
    print(f"Họ tên: {nguoi.name}, Tuổi: {nguoi.age}")
    nguoi.age = -7 