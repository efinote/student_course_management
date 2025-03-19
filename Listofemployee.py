
employees = [
    (201, "John Doe", "HR"),
    (202, "Jane Smith", "Finance"),
    (203, "Emily Davis", "IT"),
]

while True:
    print("\n1. Display Employees")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  
        print("\nEmployee Records:")
        print("----------------------")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}")
        print("----------------------\n")

    elif choice == "2":  
        search_id = input("Enter Employee ID to Search: ")
        if search_id.isdigit():
            search_id = int(search_id)
            found = False
            for emp in employees:
                if emp[0] == search_id:
                    print(f"\nEmployee Found: ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}\n")
                    found = True
                    break
            if not found:
                print("\nEmployee Not Found!\n")
        else:
            print("\nInvalid Input! Please enter a valid numeric ID.\n")

    elif choice == "3": 
        emp_id = input("Enter Employee ID: ")
        
        if not emp_id.isdigit():
            print("\nInvalid Input! Employee ID must be a number.\n")
            continue
        
        emp_id = int(emp_id)
        
        
        exists = any(emp[0] == emp_id for emp in employees)
        if exists:
            print("\nError: Employee ID already exists!\n")
            continue

        name = input("Enter Employee Name: ").strip()
        if not name:
            print("\nError: Name cannot be empty!\n")
            continue

        department = input("Enter Employee Department: ").strip()
        if not department:
            print("\nError: Department cannot be empty!\n")
            continue

        employees.append((emp_id, name, department))
        print("\nEmployee Added Successfully!\n")

    elif choice == "4":  
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")
