student = []

def addinfo():
    student_id = int(input("Enter student id: "))
    name = input("Enter the name: ")
    grade = input("Enter the grade: ")
    age = int(input("Enter the age of student: "))
    stud = {"id": student_id, "name": name, "grade": grade, "age": age}
    student.append(stud)
    print("Student added successfully!")

def display():
    if len(student) == 0:
        print("No student found 😈")
    else:
        for i in student:
            print(i)

def updateinfo():
    student_id = int(input("Enter student id for change: "))
    for i in student:
        if student_id == i["id"]:
            print("Select options for Update:\n 1. Update name\n 2. Update grade\n 3. Update age")
            match input("Enter option 1, 2, or 3: "):
                case "1":
                    i["name"] = input("Enter the updated name: ")
                    print("Name updated successfully")
                case "2":
                    i["grade"] = input("Enter the updated grade: ")
                    print("Grade updated successfully")
                case "3":
                    i["age"] = int(input("Enter the updated age: "))
                    print("Age updated successfully")
                case _:
                    print("Invalid update option")
            return
    print("Student NOT FOUND")

def deleteinfo():
    student_id = int(input("Enter student id for delete operation: "))
    for i in student:
        if student_id == i["id"]:
            student.remove(i)
            print("Student deleted successfully")
            return
    print("Student NOT FOUND")

while True:
    print("\nStudent Management System \n 1. ADD STUDENT INFO\n 2. DISPLAY STUDENT INFO\n 3. UPDATE STUDENT INFO\n 4. DELETE STUDENT INFO\n 5. EXIT")
    
    match input("Select the Above Options '1', '2', '3', '4', '5': "):
        case "1":
            addinfo()
        case "2":
            display()
        case "3":
            updateinfo()
        case "4":
            deleteinfo()
        case "5":
            print("Exiting program...")
            break
        case _:
            print("Invalid option")
