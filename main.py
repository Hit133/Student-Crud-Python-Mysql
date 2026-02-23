from db_connection import connect_db
conn=connect_db()

if conn:
    print("Database ready to use")
    conn.close()
    
else:
    print("connection failed")
    
    
    
    
from student_operations import add_student, view_students, update_student, delete_student

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid choice")
    