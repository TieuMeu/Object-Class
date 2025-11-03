# object mới, biến count tăng lên. In ra tổng số đối tượng đã tạo.

class Counter:
    count = 0  

    def __init__(self):
        Counter.count += 1


if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    obj4 = Counter()

    print("sô lượng tạo ra:", Counter.count)