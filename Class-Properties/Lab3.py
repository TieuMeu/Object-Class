#Xây dựng class Book với title, author, price, yearPublished.
# Viết chương trình lọc sách xuất bản sau năm 2020.


class Book:
    def __init__(self, title, author, price, yearPublished):
        self.title = title
        self.author = author
        self.price = price
        self.yearPublished = yearPublished

books_list = [
    Book("Lập Trình Python", "Nguyễn Văn A", 18.5, 2019),
    Book("Lập Trình jAVA", "Trần Thị B", 25.0, 2021),
    Book("Lập Trình CC", "Phạm Minh C", 30.0, 2022),
    Book("Lập Trình DE", "Lê Quốc D", 27.5, 2023),
    Book("Lập Trình FE", "Ngô Thanh E", 20.0, 2018)
]

locsach = [book for book in books_list if book.yearPublished > 2020]

print("📚 Danh sách sách xuất bản sau năm 2020:")
for book in locsach:
    print(f"- {book.title} | Tác giả: {book.author} | Năm: {book.yearPublished} | Giá: ${book.price}")