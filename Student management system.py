# Student Management System
students={}
while True:
    print("\n1.Add Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Exit")

    choice=input("Choose option: ")
    if choice=="1":
        name=input("Enter student name: ")
        marks=int(input("Enter marks: "))
        students[name]=marks
        print("Student added!")
    elif choice=="2":
        print("\nStudent Details:")
        for name,marks in students.items():
            print(name,"-",marks)
    elif choice=="3":
        name=input("Search student name: ")
        if name in students:
            print("Marks:",students[name])
        else:
            print("Student not found")
    elif choice=="4":
        print("Exit")
        break
    else:
        print("Invaild choice")

    
    
    