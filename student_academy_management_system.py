# =========================
# STUDENT STORAGE
# =========================
db = {}


# =========================
# GRADE CHECKER
# =========================
def find_grade(avg):
    if avg < 40:
        return "F"
    elif avg < 50:
        return "D"
    elif avg < 65:
        return "C"
    elif avg < 75:
        return "B"
    else:
        return "A"


# =========================
# INPUT MARKS
# =========================
def input_marks():
    subjects = {}
    total_subjects = 3

    for i in range(total_subjects):
        subject = input(f"Subject name {i+1}: ")

        while True:
            try:
                mark = int(input("Enter marks: "))
                if 0 <= mark <= 100:
                    subjects[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Numbers only!")

    return subjects


# =========================
# CREATE STUDENT
# =========================
def create_student():
    sid = input("Enter ID: ")

    if sid in db:
        print("ID already exists.")
        return

    name = input("Enter name: ")
    section = input("Enter class: ")
    marks = input_marks()

    db[sid] = (name, section, marks)
    print("Student record saved.")


# =========================
# SHOW STUDENTS
# =========================
def show_list():
    if not db:
        print("No records found.")
        return

    print("\n--- STUDENT LIST ---")
    for sid in db:
        print(sid, "-", db[sid][0])


# =========================
# SHOW REPORT
# =========================
def show_report():
    sid = input("Enter ID: ")

    if sid not in db:
        print("Student not found.")
        return

    name, section, marks = db[sid]
    total = sum(marks.values())
    avg = total / len(marks)

    print("\n--- REPORT CARD ---")
    print("Name:", name)
    print("Class:", section)
    print("Marks:")
    for sub in marks:
        print(sub, ":", marks[sub])
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Grade:", find_grade(avg))


# =========================
# EDIT MARK
# =========================
def edit_mark():
    sid = input("Enter ID: ")

    if sid not in db:
        print("Invalid ID.")
        return

    subject = input("Subject name: ")
    marks = db[sid][2]

    if subject not in marks:
        print("Subject not found.")
        return

    try:
        new_mark = int(input("New marks: "))
        if 0 <= new_mark <= 100:
            marks[subject] = new_mark
            print("Marks updated.")
        else:
            print("Invalid marks.")
    except ValueError:
        print("Invalid input.")


# =========================
# DELETE RECORD
# =========================
def delete_record():
    sid = input("Enter ID to delete: ")

    if sid in db:
        db.pop(sid)
        print("Record deleted.")
    else:
        print("ID not found.")


# =========================
# MAIN LOOP
# =========================
def run_program():
    while True:
        print("""
============================
STUDENT RECORD SYSTEM
============================
1. Add Student
2. View Students
3. View Report
4. Update Marks
5. Delete Student
6. Exit
""")

        option = input("Choose option: ")

        if option == "1":
            create_student()
        elif option == "2":
            show_list()
        elif option == "3":
            show_report()
        elif option == "4":
            edit_mark()
        elif option == "5":
            delete_record()
        elif option == "6":
            print("Program closed.")
            break
        else:
            print("Invalid option.")


# =========================
# START PROGRAM
# =========================
run_program()
