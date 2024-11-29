def login(): # Login page for the teacher and student    #Mahmood Ashraf
    userName = input("Enter your userName: ")           
    password = input("Enter your password: ")
    if userName == "loginteacher" and password == "teacher": # Password and username for the teacher
        return "Logged in successfully as Teacher."
    elif userName == "loginstudent" and password == "student": # Password and username for the student
        return "Logged in successfully as Student."
    else:
        return "Login failed."

def addStudentDetails(students): # Details that the teacher can add about the student
    addStudent = input("Enter the student's name to be added: ")
    addGrade = float(input("Enter the grade of the student: "))
    addSemester = input("Enter the student's semester: ")
    addRollNumber = input("Enter the student's roll number: ")
    addProgram = input("Enter the student's program: ")
    students[addStudent] = {"Grade": addGrade, "Semester": addSemester, "Roll Number": addRollNumber, "Program": addProgram} # This line adds the 'students' dictionary 
    print(f"Added student: {addStudent}, His/Her Grade: {addGrade}, Semester: {addSemester}, Roll Number: {addRollNumber}, Program: {addProgram}")
    print("Updated students list:", students)
    return "Student details added successfully."

def viewStudents(students): # Details that the teacher can see about the saved students
    if not students:
        print("No students to display.")
        return
    print("Students and Details:")
    for student, i in students.items():
        print(f"Name: {student}, Grade: {i['Grade']}, Semester: {i['Semester']}, Roll Number: {i['Roll Number']}, Program: {i['Program']}")

def viewOwnDetails(student_name, students): # Details that a student can see about theirself when they enter  the saved name
    if not students:
        print("No students to display.")
        return
    if student_name not in students:
        print("No student found with that name.")
        return
    print(f"Your details: Grade: {students[student_name]['Grade']}, Semester: {students[student_name]['Semester']}, Roll Number: {students[student_name]['Roll Number']}, Program: {students[student_name]['Program']}")

def main():
    students = {}  # An empty dictionary to store student details
    while True:
        login_result = login()
        print(login_result)

        if login_result == "Logged in successfully as Teacher.":
            while True:
                print("\nTeacher Options:") # Options the teacher get after logging in
                print("1. Add student details") 
                print("2. View students and details")
                print("3. Logout")

                choice = input("Enter your choice: ")

                if choice == '1':
                    addStudentDetails(students)  # Option that the teacher can see to add and view student details
                elif choice == '2':
                    viewStudents(students)
                elif choice == '3':
                    print("Logging out.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif login_result == "Logged in successfully as Student.":
            student_name = input("Enter your name: ")

            print("\nStudent Options:") # Options that the student can see about theirself
            print("1. View your details")
            print("2. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                viewOwnDetails(student_name, students)  # Students dictionary 
            elif choice == '2':
                print("Logging out.")
                break
            else:
                print("Invalid choice. Please try again.")

        else:
            print("\nLogin Options:") # new line character is to break the line
            print("1. Login")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                continue
            elif choice == '2':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

main()
