import tkinter as tk
import mysql.connector
from tkinter import ttk, messagebox
from tkinter import PhotoImage

root = tk.Tk()
root.title("Management")
root.configure(bg="lightblue")

# Update the following with your MySQL database credentials
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "manisha123"
MYSQL_DATABASE = "manisha"

# Establishing a connection to MySQL
connection = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

TABLE_NAME = "sms"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
STUDENT_SEMESTER = "student_semester"
STUDENT_COURSE_DURATION = "student_course_duration"
STUDENT_DEPARTMENT = "student_department"
STUDENT_PROJECT_WORK = "student_project_work"
STUDENT_EXTRA_CURRICULUM = "student_extra_curriculum"


# Create the table in MySQL if it does not exist
create_table_query = f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (" \
                     f"{STUDENT_ID} INT AUTO_INCREMENT PRIMARY KEY, " \
                     f"{STUDENT_NAME} VARCHAR(255), " \
                     f"{STUDENT_COLLEGE} VARCHAR(255), " \
                     f"{STUDENT_ADDRESS} VARCHAR(255), " \
                     f"{STUDENT_PHONE} BIGINT, " \
                     f"{STUDENT_SEMESTER} INT, " \
                     f"{STUDENT_COURSE_DURATION} INT);" \
                     f"{STUDENT_DEPARTMENT} VARCHAR(255), " \
                     f"{STUDENT_PROJECT_WORK} VARCHAR(255), " \
                     f"{STUDENT_EXTRA_CURRICULUM} VARCHAR(255));"

connection.cursor().execute(create_table_query)

appLabel = tk.Label(root, text="Student Management System", fg="#0000FF", width=55)
appLabel.config(font=("Bahnschrift SemiBold SemiConden", 35))
appLabel.grid(row=0, columnspan=2, padx=(50, 10), pady=(20, 0))

class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""
    semester = 0
    courseduration = 0
    department = ""
    projectwork = ""
    extracurriculum = ""

    def __init__(self, studentName, collegeName, phoneNumber, address, semester, courseduration, department, projectwork, extracurriculum):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address
        self.semester = semester
        self.courseduration = courseduration
        self.department = department
        self.projectwork = projectwork
        self.extracurriculum = extracurriculum

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                font= ("Cambria",10)).grid(row=1, column=0, padx=(30,0),
                pady=(30,0))

collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                font= ("Cambria",10)).grid(row=2, column=0, padx=(30,0),
                pady=(30,0))

phoneLabel = tk.Label(root, text="Enter your phone", width=40, anchor='w',
                font= ("Cambria",10)).grid(row=3, column=0, padx=(30,0),
                pady=(30,0))

addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                font= ("Cambria",10)).grid(row=4, column=0, padx=(30,0),
                pady=(30,0))
                
semesterLabel = tk.Label(root, text="Enter your semester", width=40, anchor='w',
                font= ("Cambria",10)).grid(row=5, column=0, padx=(30,0),
                pady=(30,0))  
                
durationLabel = tk.Label(root, text="Enter your course duration", width=40, anchor='w',
                font= ("Cambria",10)).grid(row=6, column=0, padx=(30, 0), 
                pady=(30, 0)) 

departmentLabel = tk.Label(root, text="Enter your department", width=40, anchor='w',
                font=("Cambria", 10)).grid(row=7, column=0, padx=(30, 0),
                pady=(30, 0))

projectLabel = tk.Label(root, text="Enter your project work", width=40, anchor='w',
                font=("Cambria", 10)).grid(row=8, column=0, padx=(30, 0),
                pady=(30, 0))

curriculumLabel = tk.Label(root, text="Enter your extra curriculum", width=40, anchor='w',
                font=("Cambria", 10)).grid(row=9, column=0, padx=(30, 0),
                pady=(30, 0))                           

nameEntry = tk.Entry(root, width=30)
nameEntry.grid(row=1, column=1,padx=(30,0), pady=(30,0))

collegeEntry = tk.Entry(root, width=30)
collegeEntry.grid(row=2, column=1, padx=(30,0), pady=(30,0))

phoneEntry = tk.Entry(root, width=30)
phoneEntry.grid(row=3, column=1, padx=(30,0),  pady=(30,0))

addressEntry = tk.Entry(root, width=30)
addressEntry.grid(row=4, column=1,padx=(30,0),  pady=(30,0))

semesterEntry = tk.Entry(root, width=30)
semesterEntry.grid(row=5, column=1,padx=(30,0), pady=(30,0))

durationEntry = tk.Entry(root, width=30)
durationEntry.grid(row=6, column=1,padx=(30,0), pady=(30,0))

departmentEntry = tk.Entry(root, width=30)
departmentEntry.grid(row=7, column=1,padx=(30,0), pady=(30,0))

projectEntry = tk.Entry(root, width=30)
projectEntry.grid(row=8, column=1,padx=(30,0), pady=(30,0))

curriculumEntry = tk.Entry(root, width=30)
curriculumEntry.grid(row=9, column=1,padx=(30,0), pady=(30,0))

def takeNameInput():
    global nameEntry, collegeEntry, departmentEntry, phoneEntry, addressEntry, semesterEntry, durationEntry, projectEntry, curriculumEntry
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_DEPARTMENT, STUDENT_ADDRESS, STUDENT_PHONE, STUDENT_SEMESTER, STUDENT_COURSE_DURATION, STUDENT_PROJECT_WORK, STUDENT_EXTRA_CURRICULUM
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)
    semester = int(semesterEntry.get())
    semesterEntry.delete(0, tk.END)
    courseduration = int(durationEntry.get())
    durationEntry.delete(0, tk.END)
    department = departmentEntry.get()
    departmentEntry.delete(0, tk.END)
    projectwork = projectEntry.get()
    projectEntry.delete(0, tk.END)
    extracurriculum = curriculumEntry.get()
    curriculumEntry.delete(0, tk.END)

    connection.cursor().execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                                STUDENT_COLLEGE + ", " + ", " +
                                STUDENT_ADDRESS + ", " + STUDENT_PHONE + ", " +
                                STUDENT_SEMESTER + ", " + STUDENT_COURSE_DURATION + ", " + STUDENT_DEPARTMENT +
                                STUDENT_PROJECT_WORK + ", " + STUDENT_EXTRA_CURRICULUM +
                                ") VALUES ( '" + username + "', '" + collegeName + "', '" +
                                department + "', '" + address + "', " + str(phone) + ", " +
                                str(semester) + ", " + str(courseduration) + ", '" + projectwork +
                                "', '" + extracurriculum + "');")

    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")



def destroyRootWindow():
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                    fg="#0000FF", width=40)
    appLabel.config(font=("Sylfaen",30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five", "six, seven, eight, nine")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")
    tree.heading("five", text="Semester")
    tree.heading("six", text="Duration")
    tree.heading("seven", text="Department")
    tree.heading("eight", text="Projectwork")
    tree.heading("nine", text="extracurriculum")

    select_query = f"SELECT * FROM {TABLE_NAME};"
    cursor = connection.cursor()
    cursor.execute(select_query)
    data = cursor.fetchall()

    if not data:
        messagebox.showinfo("No Data", "No data found in the table.")
        return

    i = 0
    for row in data:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()
    
style = ttk.Style()
style.configure('Fancy.TButton', foreground='black', background='blue', font=('Helvetica', 12, 'bold'))    

button = ttk.Button(root, text="Take Input", command=lambda: takeNameInput(), style='Fancy.TButton')
button.grid(row=10, column=0, pady=40)

# Create the "Display Result" button
displayButton = ttk.Button(root, text="Display Result", command=lambda: destroyRootWindow(), style='Fancy.TButton')
displayButton.grid(row=10, column=1, pady=40)

root.mainloop()
