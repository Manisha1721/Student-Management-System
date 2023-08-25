import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import mysql.connector

root = tk.Tk()
root.title("Management")
root.configure(bg="lightpink")

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

appLabel = tk.Label(root, text="Student Management System", fg="#0000FF", bg="lightblue", width=55)
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

# Create a PanedWindow to organize the fields vertically
pane_vertical = ttk.PanedWindow(root, orient=tk.VERTICAL)
pane_vertical.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='ew')

pane_top = ttk.PanedWindow(pane_vertical, orient=tk.HORIZONTAL)
pane_bottom = ttk.PanedWindow(pane_vertical, orient=tk.HORIZONTAL)

pane_vertical.add(pane_top)
pane_vertical.add(pane_bottom)

# Top pane: Personal information
pane_top.grid(sticky='ew')
personal_info_label = ttk.Label(pane_top, text="Personal Information", font=("Cambria", 12, "bold"))
personal_info_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

nameLabel = ttk.Label(pane_top, text="Enter your name:")
collegeLabel = ttk.Label(pane_top, text="Enter your college:")
phoneLabel = ttk.Label(pane_top, text="Enter your phone:")
addressLabel = ttk.Label(pane_top, text="Enter your address:")
semesterLabel = ttk.Label(pane_top, text="Enter your semester:")

nameEntry = ttk.Entry(pane_top, width=30)
collegeEntry = ttk.Entry(pane_top, width=30)
phoneEntry = ttk.Entry(pane_top, width=30)
addressEntry = ttk.Entry(pane_top, width=30)
semesterEntry = ttk.Entry(pane_top, width=30)

nameLabel.grid(row=1, column=0, padx=10, pady=5)
collegeLabel.grid(row=2, column=0, padx=10, pady=5)
phoneLabel.grid(row=3, column=0, padx=10, pady=5)
addressLabel.grid(row=4, column=0, padx=10, pady=5)
semesterLabel.grid(row=5, column=0, padx=10, pady=5)

nameEntry.grid(row=1, column=1, padx=10, pady=5)
collegeEntry.grid(row=2, column=1, padx=10, pady=5)
phoneEntry.grid(row=3, column=1, padx=10, pady=5)
addressEntry.grid(row=4, column=1, padx=10, pady=5)
semesterEntry.grid(row=5, column=1, padx=10, pady=5)

# Bottom pane: Academic information
pane_bottom.grid(sticky='ew')
academic_info_label = ttk.Label(pane_bottom, text="Academic Information", font=("Cambria", 12, "bold"))
academic_info_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

durationLabel = ttk.Label(pane_bottom, text="Enter your course duration:")
departmentLabel = ttk.Label(pane_bottom, text="Enter your department:")
projectLabel = ttk.Label(pane_bottom, text="Enter your project work:")
curriculumLabel = ttk.Label(pane_bottom, text="Enter your extra curriculum:")

durationEntry = ttk.Entry(pane_bottom, width=30)
departmentEntry = ttk.Entry(pane_bottom, width=30)
projectEntry = ttk.Entry(pane_bottom, width=30)
curriculumEntry = ttk.Entry(pane_bottom, width=30)

durationLabel.grid(row=1, column=0, padx=10, pady=5)
departmentLabel.grid(row=2, column=0, padx=10, pady=5)
projectLabel.grid(row=3, column=0, padx=10, pady=5)
curriculumLabel.grid(row=4, column=0, padx=10, pady=5)

durationEntry.grid(row=1, column=1, padx=10, pady=5)
departmentEntry.grid(row=2, column=1, padx=10, pady=5)
projectEntry.grid(row=3, column=1, padx=10, pady=5)
curriculumEntry.grid(row=4, column=1, padx=10, pady=5)

# Add a new label for image input
imageLabel = ttk.Label(root, text="Select an image", width=40, anchor='w', font=("Cambria", 10))
imageLabel.grid(row=2, column=0, padx=(30, 0), pady=(30, 0), columnspan=2)

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
imageButton = ttk.Button(root, text="Select Image", command=selectImage, style='Fancy.TButton')
imageButton.grid(row=2, column=1, pady=40)

def takeNameInput():
    # Your existing code for inserting data into MySQL goes here
    pass

def destroyRootWindow():
    # Your existing code for displaying results goes here
    pass

style = ttk.Style()
style.configure('Fancy.TButton', foreground='black', background='blue', font=('Helvetica', 12, 'bold'))    

button = ttk.Button(root, text="Take Input", command=lambda: takeNameInput(), style='Fancy.TButton')
button.grid(row=3, column=0, pady=40)

# Create the "Display Result" button
displayButton = ttk.Button(root, text="Display Result", command=lambda: destroyRootWindow(), style='Fancy.TButton')
displayButton.grid(row=3, column=1, pady=40)

root.mainloop()
