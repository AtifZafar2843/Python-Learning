# challenge:
# Build a report card for a student across at least 5 subjects. Write these functions and have them call each other:
# • calculate_percentage(marks_list) -> average percentage
# • get_grade(percentage)            -> letter grade
# • get_gpa(percentage)              -> GPA on a 10-point scale
# • generate_report(name, marks_list) -> prints a full formatted report using the above

# Example:
# ===== REPORT CARD =====
# Name: Priya
# Subjects: 5
# Percentage: 84.0%
# Grade: B
# GPA: 8.4

# Solution:
def calculate_percentage(marks_list: list[float]) -> float:
    total_subject = len(marks_list)
    percentage = (sum(marks_list) / (total_subject * 100)) * 100
    return round(percentage, 2)

def get_grade(percentage: float) ->str:
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def get_gpa(percentage: float) -> float:
    return round(percentage / 10, 1)

def generate_report(name: str, marks_list: list[float]) -> None:
    pct = calculate_percentage(marks_list)
    grade = get_grade(pct)
    gpa = get_gpa(pct)

    print("===== REPORT CARD =====")
    print(f"Name: {name}")
    print(f"Subjects: {len(marks_list)}")
    print(f"Percentage: {pct}%")
    print(f"Grade: {grade}")
    print(f"GPA: {gpa}")

student_marks = [99, 96, 44, 88, 43]
generate_report("Priya", student_marks)
