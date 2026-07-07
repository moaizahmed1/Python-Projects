
# Build a small command-line *Student Marks Manager* that ties everything together:

# 1. Keep a dictionary where the key is a student name and the value is their marks.
# 2. Show a menu in a loop with these options:
#    - 1 Add a student and their marks
#    - 2 View all students and marks
#    - 3 Show the topper (highest marks)
#    - 4 Show the class average
#    - 5 Exit
# 3. Keep running until the user chooses 5.
# 4. Handle invalid input without crashing (wrong menu number, non-numeric marks).



students = {}  

while True:

    print("\n===== Student Marks Manager =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Show Topper")
    print("4. Show Class Average")
    print("5. Exit")

  
    choice = input("Enter your choice (1-5): ")

    
    # Option 1 - Add Student
  
    if choice == "1":

        name = input("Enter student name: ")

        try:
            marks = float(input("Enter student marks: "))
            students[name] = marks
            print(name, "added successfully!")

        except ValueError:
            print("Invalid input! Marks must be a number.")

    
    # Option 2 - View Students
   
    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            print("\nStudent Records")
            print("----------------")

            for name, marks in students.items():
                print(name,":",marks)

    # Option 3 - Show Topper
   
    elif choice == "3":

        if len(students) == 0:
            print("No student records available.")

        else:
            topper = max(students, key=students.get)
            print("Topper:", topper)
            print("Marks:", {students[topper]})


    # Option 4 - Show Average
   
    elif choice == "4":

        if len(students) == 0:
            print("No student records available.")

        else:
            average = sum(students.values()) / len(students)
            print("Class Average:", round(average, 2))


    elif choice == "5":

        print("Thank you for using Student Marks Manager!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
        