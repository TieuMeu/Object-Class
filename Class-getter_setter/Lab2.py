#Xây dựng class Account có balance — chỉ cho phép thay đổi qua setter nếu số tiền > 0.

class Account:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Số dư no được âm.")

if __name__ == "__main__":
    tai_khoan = Account(100)
    print("Số dư hiện tại:", tai_khoan.balance)
    tai_khoan.balance = -234  
    tai_khoan.balance = 3456456  
    print("Số dư sau cập nhật:", tai_khoan.balance)