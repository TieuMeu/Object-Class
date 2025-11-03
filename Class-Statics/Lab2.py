#Viết class MathUtil chứa các phương thức static isPrime, factorial, gcd.

class MathUtil:
    @staticmethod
    def isPrime(n):
        """Kiểm tra xem n có phải là số nguyên tố không"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        """Tính giai thừa của n"""
        ket_qua = 1
        for i in range(1, n + 1):
            ket_qua *= i
        return ket_qua

    @staticmethod
    def gcd(a, b):
        """Tìm ước chung lớn nhất giữa a và b"""
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    print("Kiểm tra số nguyên tố:", MathUtil.isPrime(7))
    print("Kiểm tra giai thừa :", MathUtil.factorial(5))
    print("Ước chung lớn nhất :", MathUtil.gcd(24, 18))