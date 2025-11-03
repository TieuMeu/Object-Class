# Tạo class GradeSystem có method calculateGPA nhận danh sách điểm trả về GPA trung bình.


class GradeSystem:
    def calculateGPA(self, scores):
        def convert(score):
            if score >= 90:
                return 4.0
            elif score >= 80:
                return 3.0
            elif score >= 70:
                return 2.0
            elif score >= 60:
                return 1.0
            else:
                return 0.0

        gpa_values = [convert(diem) for diem in scores]
        return round(sum(gpa_values) / len(gpa_values), 2)


if __name__ == "__main__":
    system = GradeSystem()
    diem_sinh_vien = [88, 91, 73, 67, 84] 
    print(f"GPA trung bình: {system.calculateGPA(diem_sinh_vien)}")