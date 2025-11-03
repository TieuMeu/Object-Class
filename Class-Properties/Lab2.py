#Thiết kế class Employee 
# với các thuộc tính name, salary, department. Tính tổng lương theo phòng ban.



class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

list_nv = [
    Employee("A", 11100, "DE"),
    Employee("B", 22200, "PA"),
    Employee("C", 33300, "FE"),
    Employee("D", 44400, "PM"),
]

tluong = {}
for nv in list_nv:
    tluong[nv.department] = tluong.get(nv.department, 0) + nv.salary

for phong, tong in tluong.items():
    print(f"Phòng ban: {phong}, Tổng lương: {tong}")