from db_connection import connect_db

#create/add students
def add_student():
    conn=connect_db()
    
    if conn is None:
        print("database connection failed")
        return
    
    cursor=conn.cursor()
    
    
    name=input("enter student name: ")
    age=int(input("Enter age: "))
    course=input("Enter course: ")
    marks=int(input("Enter marks: "))
    
    
    #sql query
    query=""" INSERT INTO students (name,age,course,marks)
    VALUES(%s,%s,%s,%s)"""
    
    values=(name,age,course,marks)
    
    try:
        cursor.execute(query,values)
        conn.commit()
        print("Student added successfully")
    
    except Exception as e:
        print("Error: ",e)
        
    finally:
        cursor.close()
        conn.close()
        


# view students
def view_students():
    conn=connect_db()
    
    if conn is None:
        print("Database connection Failed")
        return
    cursor=conn.cursor()
    
    query="SELECT * from students"
    
    try:
        cursor.execute(query)
        records=cursor.fetchall()
        
        if len(records)==0:
            print("No students found")
            return
        print("\n===== STUDENT LIST =====")
        print("ID | Name | Age | Course | Marks")
        print("-----------------------------------")
        
        for row in records:
             print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4])
    
    except Exception as e:
        print("Error: ",e)       
        
    finally:
        cursor.close()
        conn.close()
        
        
#update - modify student details
def update_student():
    conn=connect_db()
    
    if conn is None:
        print("Database connection Failed")
        return
    
    cursor=conn.cursor()
    #ask which student to update
    student_id=int(input("Enter student ID to update: "))
    
    name=input("Enter new name: ")
    age=int(input("Enter new age: "))
    course=input("Enter new course: ")
    marks=int(input("Enter new marks: "))
    
    query="""
    update students
    set name=%s,age=%s,course=%s,marks=%s
    where id=%s
    """
    
    values=(name,age,course,marks,student_id)
    
    try:
        cursor.execute(query,values)
        conn.commit()
        
        
        if cursor.rowcount==0:
            print("No studnet found with this ID")
        else:
            print("Student updated successfully")
            
    except Exception as e:
        print("error: ",e)
        
    finally:
        cursor.close()
        conn.close()
        
        
        
# DELETE - Remove student
def delete_student():
    conn = connect_db()

    if conn is None:
        print("Database connection failed")
        return

    cursor = conn.cursor()

    # Ask which student to delete
    student_id = int(input("Enter student ID to delete: "))

    query = "DELETE FROM students WHERE id=%s"

    try:
        cursor.execute(query, (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print("No student found with this ID.")
        else:
            print("✅ Student deleted successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        conn.close()
        
