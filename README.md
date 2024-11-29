# Student-Data-System
Teacher-Student Management System
A Python-based console application that allows teachers to manage student details and provides students access to their own information. The system features a secure login process for both teachers and students and includes functionality for managing and viewing student data.

Features
Teacher Features
Login as Teacher:
Use loginteacher as the username and teacher as the password.
Add Student Details:
Add details such as the student's name, grade, semester, roll number, and program.
View All Student Details:
Display a list of all students with their respective details.
Logout:
Safely logout to prevent unauthorized access.
Student Features
Login as Student:
Use loginstudent as the username and student as the password.
View Own Details:
Access personal details by entering the saved name in the system.
Logout:
Safely logout after viewing details.
Getting Started
Prerequisites
Python 3.6 or higher installed on your system.
How to Run the Program
Clone or download the project files to your local machine.
Open a terminal or command prompt.
Navigate to the folder containing the project file.
Run the program using the command:
bash
Copy code
python <filename>.py
Replace <filename> with the name of your Python file (e.g., main.py).
Usage Instructions
Login
Teachers and students must log in with the correct username and password:
Teacher Login: Username: loginteacher, Password: teacher
Student Login: Username: loginstudent, Password: student
Teacher Options
Add Student Details: Enter student information including name, grade, semester, roll number, and program.
View Students and Details: Display all stored student details.
Logout: Return to the main login menu.
Student Options
View Your Details: Access personal details by entering your saved name.
Logout: Return to the main login menu.
Code Structure
login(): Handles user authentication for teachers and students.

addStudentDetails(students): Allows teachers to add details about students to the students dictionary.

viewStudents(students): Displays all stored student details to the teacher.

viewOwnDetails(student_name, students): Displays a specific student's details based on their name.

main(): Entry point of the program that manages user interactions and calls appropriate functions.

Example Output
Teacher Login and Add Student
plaintext
Copy code
Enter your userName: loginteacher
Enter your password: teacher
Logged in successfully as Teacher.

Teacher Options:
1. Add student details
2. View students and details
3. Logout
Enter your choice: 1
Enter the student's name to be added: John
Enter the grade of the student: 85
Enter the student's semester: 3rd
Enter the student's roll number: 21-CS-001
Enter the student's program: Computer Science
Added student: John, His/Her Grade: 85.0, Semester: 3rd, Roll Number: 21-CS-001, Program: Computer Science
Updated students list: {'John': {'Grade': 85.0, 'Semester': '3rd', 'Roll Number': '21-CS-001', 'Program': 'Computer Science'}}
Contributors
Mahmood Ashraf
