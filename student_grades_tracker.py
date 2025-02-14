# Student Grades Tracker

def add_grade(grades, student, grade):
    if student in grades:
        grades[student].append(grade)
    else:
        grades[student] = [grade]

def calculate_average(grades, student):
    if student in grades:
        return sum(grades[student]) / len(grades[student])
    else:
        return None

def display_grades(grades):
    for student, grades_list in grades.items():
        print(f"{student}: {grades_list}")

def main():
    grades = {}
    
    while True:
        print("\nOptions:")
        print("1. Add grade")
        print("2. Calculate average")
        print("3. Display all grades")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            student = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            add_grade(grades, student, grade)
        elif choice == "2":
            student = input("Enter student name: ")
            average = calculate_average(grades, student)
            if average is not None:
                print(f"Average grade for {student}: {average:.2f}")
            else:
                print(f"No grades recorded for {student}.")
        elif choice == "3":
            display_grades(grades)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
