# Tạo class GradeSystem có method calculateGPA nhận danh sách điểm trả về GPA trung bình.


class GradeSystem:
    def calculateGPA(self, scores):
        def convert(diem):
            if diem >= 90:
                return 4.0
            elif diem >= 80:
                return 3.0
            elif diem >= 70:
                return 2.0
            elif diem >= 60:
                return 1.0
            else:
                return 0.0

        list_gpa = [convert(diem) for diem in scores]
        return round(sum(list_gpa) / len(list_gpa), 2)

system = GradeSystem()
diem_sinh_vien = [88, 91, 73, 67, 84] 
print(f"GPA trung bình: {system.calculateGPA(diem_sinh_vien)}")