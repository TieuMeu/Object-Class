# object mới, biến count tăng lên. In ra tổng số đối tượng đã tạo.

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

for _ in range(4):
    Counter()

print("Số lượng tạo ra:", Counter.count)