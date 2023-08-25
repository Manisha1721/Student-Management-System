import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import mysql.connector

root = tk.Tk()
root.title("Management")
root.configure(bg="#CF9FFF")

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
                     f"{STUDENT_COURSE_DURATION} INT, " \
                     f"{STUDENT_DEPARTMENT} VARCHAR(255), " \
                     f"{STUDENT_PROJECT_WORK} VARCHAR(255), " \
                     f"{STUDENT_EXTRA_CURRICULUM} VARCHAR(255));"

connection.cursor().execute(create_table_query)

appLabel = tk.Label(root, text="Student Management System", fg="#FFFFFF", bg="#CF9FFF", width=55)
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

    def __init__(self, studentName, collegeName, phoneNumber, address, semester, courseduration, department,
                 projectwork, extracurriculum):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address
        self.semester = semester
        self.courseduration = courseduration
        self.department = department
        self.projectwork = projectwork
        self.extracurriculum = extracurriculum


# Create a PanedWindow to organize the fields horizontally
pane_horizontal = ttk.PanedWindow(root, height=300, width=1235, orient=tk.HORIZONTAL)
pane_horizontal.grid(row=1, column=0, padx=20, pady=20, sticky='ew')

# Left pane: Personal information
pane_left = ttk.Frame(pane_horizontal, style="LeftPane.TFrame")
pane_horizontal.add(pane_left, weight=1)

# Set the background color for the left pane
style = ttk.Style()
style.configure("LeftPane.TFrame", background="#DFC7FF")

personal_info_label = ttk.Label(pane_left, text="Personal Information", font=("Cambria", 15, "bold"), background="#DFC7FF")
personal_info_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

nameLabel = ttk.Label(pane_left, text="Enter your name:", background="#DFC7FF")
collegeLabel = ttk.Label(pane_left, text="Enter your college:", background="#DFC7FF")
phoneLabel = ttk.Label(pane_left, text="Enter your phone:", background="#DFC7FF")
addressLabel = ttk.Label(pane_left, text="Enter your address:", background="#DFC7FF")
semesterLabel = ttk.Label(pane_left, text="Enter your semester:", background="#DFC7FF")

nameEntry = ttk.Entry(pane_left, width=30)
collegeEntry = ttk.Entry(pane_left, width=30)
phoneEntry = ttk.Entry(pane_left, width=30)
addressEntry = ttk.Entry(pane_left, width=30)
semesterEntry = ttk.Entry(pane_left, width=30)

nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
collegeLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
phoneLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
addressLabel.grid(row=4, column=0, padx=10, pady=5, sticky="w")
semesterLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")

nameEntry.grid(row=1, column=1, padx=10, pady=5)
collegeEntry.grid(row=2, column=1, padx=10, pady=5)
phoneEntry.grid(row=3, column=1, padx=10, pady=5)
addressEntry.grid(row=4, column=1, padx=10, pady=5)
semesterEntry.grid(row=5, column=1, padx=10, pady=5)


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


# Right pane: Academic information
pane_right = ttk.Frame(pane_horizontal, style="RightPane.TFrame")
pane_horizontal.add(pane_right, weight=1)

# Set the background color for the left pane
style = ttk.Style()
style.configure("RightPane.TFrame", background="#DFC7FF")

academic_info_label = ttk.Label(pane_right, text="Academic Information", font=("Cambria", 15, "bold"),
                                background="#DFC7FF")
academic_info_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

durationLabel = ttk.Label(pane_right, text="Enter your course duration:", background="#DFC7FF")
departmentLabel = ttk.Label(pane_right, text="Enter your department:", background="#DFC7FF")
projectLabel = ttk.Label(pane_right, text="Enter your project work:", background="#DFC7FF")
curriculumLabel = ttk.Label(pane_right, text="Enter your extra curriculum:", background="#DFC7FF")

durationEntry = ttk.Entry(pane_right, width=30)
departmentEntry = ttk.Entry(pane_right, width=30)
projectEntry = ttk.Entry(pane_right, width=30)
curriculumEntry = ttk.Entry(pane_right, width=30)

durationLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
departmentLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
projectLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")
curriculumLabel.grid(row=4, column=0, padx=10, pady=5, sticky="w")

durationEntry.grid(row=1, column=1, padx=10, pady=5)
departmentEntry.grid(row=2, column=1, padx=10, pady=5)
projectEntry.grid(row=3, column=1, padx=10, pady=5)
curriculumEntry.grid(row=4, column=1, padx=10, pady=5)

# Add a new label for image input
imageLabel = ttk.Label(pane_right, text="upload your profile photo", width=40, anchor='w', font=("Cambria", 10),
                       background="#DFC7FF")
imageLabel.grid(row=5, column=0, padx=10, pady=(15, 0), columnspan=1)

# Function to handle image selection
def selectImage():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        # Display the selected image on the GUI
        image = Image.open(file_path)
        image.thumbnail((100, 100))  # Resize the image to fit the label
        photo = ImageTk.PhotoImage(image)
        imageLabel.image = photo
        imageLabel.config(image=photo)


# Add a button to trigger the image selection
imageButton = ttk.Button(pane_right, text="Select Image", command=selectImage, style='Fancy.TButton')
imageButton.grid(row=5, column=1, padx=5, pady=20)

style = ttk.Style()
style.configure('Fancy.TButton', foreground='black', background='blue', font=('Helvetica', 12, 'bold'))


# Create the "Take Input" button inside the left pane
button = ttk.Button(pane_left, text="Take Input", command=lambda: takeNameInput(), style='Fancy.TButton')
button.grid(row=6, column=0, columnspan=2, pady=70)


def destroyRootWindow():
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="#CF9FFF", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

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


# Create the "Display Result" button inside the right pane
displayButton = ttk.Button(pane_right, text="Display Result", command=lambda: destroyRootWindow(), style='Fancy.TButton')
displayButton.grid(row=8, column=0, columnspan=2, pady=30)

root.mainloop()
