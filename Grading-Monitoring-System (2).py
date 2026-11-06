students = []



def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None



def calculate_average(grades):
    if len(grades) == 0:
        return 0

    total = 0

    for grade in grades:
        total = total + grade["grade"]

    return total / len(grades)



def register_student():
    print("      REGISTER STUDENT      ")

    student_id = input("Student ID: ")
    name = input("Student Name: ")
    password = input("Password: ")

    if find_student(student_id) != None:
        print("Student ID already exists!")

    else:
        student = {
            "id": student_id,
            "name": name,
            "password": password,
            "grades": []
        }

        students.append(student)

        print("Student registered successfully!")



def record_grade():
    print("      RECORD GRADE        ")

    student_id = input("Student ID: ")
    student = find_student(student_id)

    if student == None:
        print("Student not found!")

    else:
        print("         SUBJECTS         ")
        print("1. Math")
        print("2. Science")
        print("3. English")
        print("4. Filipino")
        print("5. Araling Panlipunan")
        print("6. MAPEH")
        print("7. Edukasyon sa Pagkakatao (EsP)")
        print("8. Technical Livelihood Education (TLE)")

        choice = input("Choose subject: ")

        if choice == "1":
            subject = "Math"

        elif choice == "2":
            subject = "Science"

        elif choice == "3":
            subject = "English"

        elif choice == "4":
            subject = "Filipino"

        elif choice == "5":
            subject = "Araling Panlipunan"

        elif choice == "6":
            subject = "MAPEH"

        elif choice == "7":
            subject = "Edukasyon sa Pagkakatao (EsP)"

        elif choice == "8":
            subject = "Technical Livelihood Education (TLE)"

        else:
            print("Invalid subject!")
            return

        grade = input("Enter grade: ")

        if grade.isdigit():
            grade = int(grade)

            if grade >= 0 and grade <= 100:

                student["grades"].append({
                    "subject": subject,
                    "grade": grade
                })

                print("Grade recorded successfully!")

                if grade < 75:
                    print("Status: Failed")

                elif grade <= 89:
                    print("Status: Passed")

                else:
                    print("Status: Excellent")

            else:
                print("Grade must be from 0 to 100.")

        else:
            print("Please enter a number.")



def update_grade():
    print("   UPDATE GRADE    ")

    student_id = input("Student ID: ")
    student = find_student(student_id)

    if student == None:
        print("Student not found!")

    elif len(student["grades"]) == 0:
        print("No grades recorded.")

    else:
        print("\nStudent:", student["name"])

        for i in range(len(student["grades"])):
            print(
                i + 1,
                student["grades"][i]["subject"],
                ":",
                student["grades"][i]["grade"]
            )

        choice = input("Choose grade number: ")

        if choice.isdigit():
            choice = int(choice)

            if choice >= 1 and choice <= len(student["grades"]):

                new_grade = input("Enter new grade: ")

                if new_grade.isdigit():
                    new_grade = int(new_grade)

                    if new_grade >= 0 and new_grade <= 100:

                        student["grades"][choice - 1]["grade"] = new_grade

                        print("Grade updated successfully!")

                        if new_grade < 75:
                            print("Status: Failed")

                        elif new_grade <= 89:
                            print("Status: Passed")

                        else:
                            print("Status: Excellent")

                    else:
                        print("Grade must be from 0 to 100.")

                else:
                    print("Please enter a number.")

            else:
                print("Invalid grade number.")

        else:
            print("Invalid choice!")



def view_grades():
    print("      VIEW GRADES         ")

    student_id = input("Student ID: ")
    student = find_student(student_id)

    if student == None:
        print("Student not found!")

    else:
        print("\nStudent:", student["name"])

        if len(student["grades"]) == 0:
            print("No grades recorded.")

        else:
            total = 0

            for grade in student["grades"]:

                if grade["grade"] < 75:
                    status = "Failed"

                elif grade["grade"] <= 89:
                    status = "Passed"

                else:
                    status = "Excellent"

                print(
                    grade["subject"],
                    ":",
                    grade["grade"],
                    "-",
                    status
                )

                total = total + grade["grade"]

            average = total / len(student["grades"])

            if average < 75:
                average_status = "Failed"

            elif average <= 89:
                average_status = "Passed"

            else:
                average_status = "Excellent"

            print("Average:", round(average, 2))
            print("Average Status:", average_status)



def view_student_grades(student):
    print("      MY GRADES      ")

    if len(student["grades"]) == 0:
        print("No grades recorded.")

    else:
        for grade in student["grades"]:

            if grade["grade"] < 75:
                status = "Failed"

            elif grade["grade"] <= 89:
                status = "Passed"

            else:
                status = "Excellent"

            print(
                grade["subject"],
                ":",
                grade["grade"],
                "-",
                status
            )



def view_student_average(student):
    print("      MY AVERAGE      ")

    if len(student["grades"]) == 0:
        print("No grades recorded.")

    else:
        average = calculate_average(student["grades"])

        if average < 75:
            status = "Failed"

        elif average <= 89:
            status = "Passed"

        else:
            status = "Excellent"

        print("Average:", round(average, 2))
        print("Status:", status)



def teacher_menu():

    while True:
        print("      TEACHER MENU       ")
        print("1. Register Student")
        print("2. Record Grade")
        print("3. Update Grade")
        print("4. View Student Grades")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            record_grade()

        elif choice == "3":
            update_grade()

        elif choice == "4":
            view_grades()

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid choice!")



def student_menu(student):

    while True:
        print("      STUDENT MENU       ")
        print("1. View Grades")
        print("2. View Average")
        print("3. Logout")

        choice = input("Choose: ")

        if choice == "1":
            view_student_grades(student)

        elif choice == "2":
            view_student_average(student)

        elif choice == "3":
            print("Logging out...")
            break

        else:
            print("Invalid choice!")



def teacher_login():

    print("      TEACHER LOGIN        ")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login successful!")
        teacher_menu()

    else:
        print("Wrong username or password!")



def student_login():

    print("      STUDENT LOGIN        ")

    student_id = input("Student ID: ")
    password = input("Password: ")

    student = find_student(student_id)

    if student == None:
        print("Student not found!")

    elif password == student["password"]:
        print("Login successful!")
        print("Welcome,", student["name"])
        student_menu(student)

    else:
        print("Wrong password!")

def login():

    while True:
        print("      GRADING MONITORING SYSTEM        ")
        print("1. Teacher Login")
        print("2. Student Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            teacher_login()

        elif choice == "2":
            student_login()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


login()