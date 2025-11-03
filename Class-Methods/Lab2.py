#Tạo class Temperature có method chuyển đổi giữa Celsius và Fahrenheit.

class Temperature:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit

    def to_fahrenheit(self):
        if self.unit == "C":
            return (self.value * 9/5) + 32
        return self.value  

    def to_celsius(self):
        if self.unit == "F":
            return (self.value - 32) * 5/9
        return self.value  

if __name__ == "__main__":
    do_hanoi = Temperature(32, "C")      
    do_newyork = Temperature(95, "F")   

    print("Kết quả chuyển đổi nhiệt độ:")
    print(f"{do_hanoi.value}°C  = {do_hanoi.to_fahrenheit():.2f}°F")
    print(f"{do_newyork.value}°F  = {do_newyork.to_celsius():.2f}°C")