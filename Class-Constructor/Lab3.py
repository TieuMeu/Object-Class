#Xây class Order có constructor khởi tạo danh sách sản phẩm và tổng giá trị đơn hàng.

class Order:
    def __init__(self, products):
        self.products = products
        self.total = sum(p['price'] for p in products)

    def show_order(self):
        print("Chi tiết đơn hàng:")
        for p in self.products:
            print(f"- {p['name']}: {p['price']:,} VND")
        print(f"Tổng cộng: {self.total:,} VND")

if __name__ == "__main__":
    don_hang = Order([
        {'name': 'something1', 'price': 850000},
        {'name': 'something2', 'price': 450000}
    ])
    don_hang.show_order()