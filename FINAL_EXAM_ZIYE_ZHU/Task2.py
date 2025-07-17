# Task 2: Check grades and print pass/fail
def check_grades(grades):
    print("\nTask 2: Check Grades")
    for grade in grades:
        if grade >= 75:
            print("Pass")
        else:
            print("No")

# Test with sample grades
grade_list = [85, 74, 90, 65, 75]
check_grades(grade_list)
