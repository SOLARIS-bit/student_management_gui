import tkinter as tk
from tkinter import ttk, messagebox
from database import Database

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        # Database instance
        self.database = Database()

        # Menu Bar Setup
        self.menubar = tk.Menu(root)
        self.root.config(menu=self.menubar)

        # Create the File Menu
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_data)
        file_menu.add_command(label="Load", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=file_menu)

        # Create the Help Menu
        help_menu = tk.Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        self.menubar.add_cascade(label="Help", menu=help_menu)
        
        # Data structure to manage promotions
        self.promotions = {"Promotion 1": {"students": [], "subjects": [], "grades": {}},
                           "Promotion 2": {"students": [], "subjects": [], "grades": {}},
                           "Promotion 3": {"students": [], "subjects": [], "grades": {}}}


        # Creating a main canvas to allow scrolling
        self.main_canvas = tk.Canvas(root, bg="#2C3E50")
        self.main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adding a scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.main_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold the UI elements
        self.main_frame = tk.Frame(self.main_canvas, bg="#2C3E50")
        self.main_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Function to update scroll region
        def update_scroll_region(event):
            self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

        self.main_frame.bind("<Configure>", update_scroll_region)

        # UI Elements
        title = tk.Label(self.main_frame, text="Control Panel", font=("Comic Sans MS", 18, "bold"), fg="yellow", bg="#2C3E50")
        title.pack(pady=10)

        # Promotion selection
        tk.Label(self.main_frame, text="Select Promotion:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.promotion_box = ttk.Combobox(self.main_frame, values=["Promotion 1", "Promotion 2", "Promotion 3"])
        self.promotion_box.pack(pady=5)

        # Student input
        tk.Label(self.main_frame, text="Enter Student Name:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.student_entry = tk.Entry(self.main_frame)
        self.student_entry.pack(pady=5)

        add_student_btn = tk.Button(self.main_frame, text="Add Student", bg="green", fg="white", font=("Arial", 12), command=self.add_student)
        add_student_btn.pack(pady=5)

        remove_student_btn = tk.Button(self.main_frame, text="Remove Student", bg="red", fg="white", font=("Arial", 12), command=self.remove_student)
        remove_student_btn.pack(pady=5)

        # Search for Student
        tk.Label(self.main_frame, text="Search for Student:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.search_entry = tk.Entry(self.main_frame)
        self.search_entry.pack(pady=5)

        search_student_btn = tk.Button(self.main_frame, text="Search", bg="orange", fg="white", font=("Arial", 12), command=self.search_student)
        search_student_btn.pack(pady=5)

        # Student List
        tk.Label(self.main_frame, text="Student List:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.student_listbox = tk.Listbox(self.main_frame, width=40, height=5)
        self.student_listbox.pack(pady=5)
        
        # Subject List
        tk.Label(self.main_frame, text="Subject List:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.subject_listbox = tk.Listbox(self.main_frame, width=40, height=5)
        self.subject_listbox.pack(pady=5)


        # Subject input
        tk.Label(self.main_frame, text="Enter Subject Name:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.subject_entry = tk.Entry(self.main_frame)
        self.subject_entry.pack(pady=5)

        add_subject_btn = tk.Button(self.main_frame, text="Add Subject", bg="purple", fg="white", font=("Arial", 12), command=self.add_subject)
        add_subject_btn.pack(pady=5)

        remove_subject_btn = tk.Button(self.main_frame, text="Remove Subject", bg="red", fg="white", font=("Arial", 12), command=self.remove_subject)
        remove_subject_btn.pack(pady=5)

        # Grade Management
        tk.Label(self.main_frame, text="Assign Grades:", font=("Arial", 12), fg="white", bg="#2C3E50").pack(pady=10)

        tk.Label(self.main_frame, text="Select Student for Grade:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.grade_student_menu = ttk.Combobox(self.main_frame, values=[])
        self.grade_student_menu.pack(pady=5)

        tk.Label(self.main_frame, text="Select Subject for Grade:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.grade_subject_menu = ttk.Combobox(self.main_frame, values=[])
        self.grade_subject_menu.pack(pady=5)

        tk.Label(self.main_frame, text="Enter Grade:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
        self.grade_entry = tk.Entry(self.main_frame)
        self.grade_entry.pack(pady=5)

        assign_grade_btn = tk.Button(self.main_frame, text="Assign Grade", bg="blue", fg="white", font=("Arial", 12), command=self.assign_grade)
        assign_grade_btn.pack(pady=5)

        # Treeview for displaying assigned grades
        self.grade_tree = ttk.Treeview(self.main_frame, columns=("Student", "Subject", "Grade"), show="headings")
        self.grade_tree.heading("Student", text="Student")
        self.grade_tree.heading("Subject", text="Subject")
        self.grade_tree.heading("Grade", text="Grade")
        self.grade_tree.pack(pady=10)

        # Back to Main Menu
        back_btn = tk.Button(self.main_frame, text="Back to Main Menu", bg="blue", fg="white", font=("Arial", 12))
        back_btn.pack(pady=20)

        # Lists to hold students and subjects
        self.students = []
        self.subjects = []
        
        # Dictionary to hold grades (nested dictionary)
        self.grades = {}  # {student_name: {subject: grade}}

    def save_data(self):
        self.database.save_data(self.students, self.subjects, self.grades)
        messagebox.showinfo("Save Data", "Data saved successfully!")

    def load_data(self):
        students, subjects, grades = self.database.load_data()
        self.students = students
        self.subjects = subjects
        self.grades = grades

        # Update the UI elements with loaded data
        self.student_listbox.delete(0, tk.END)
        for student in self.students:
            self.student_listbox.insert(tk.END, student)

        self.grade_student_menu['values'] = self.students
        self.grade_subject_menu['values'] = self.subjects
        self.update_grade_display()
        
        messagebox.showinfo("Load Data", "Data loaded successfully!")

    def update_scroll_region(self, event):
        self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))

    def add_student(self):
        student_name = self.student_entry.get()
        if student_name:
            if student_name not in self.students:
                self.students.append(student_name)
                self.student_listbox.insert(tk.END, student_name)
                self.grade_student_menu['values'] = self.students
                self.student_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Duplicate Student", "This student is already in the list.")
        else:
            messagebox.showwarning("Input Error", "Please enter a student name.")

    def remove_student(self):
        selected_student_index = self.student_listbox.curselection()
        if selected_student_index:
            student_name = self.student_listbox.get(selected_student_index)
            self.students.remove(student_name)
            self.student_listbox.delete(selected_student_index)
            self.grade_student_menu['values'] = self.students
            # Remove grades for the deleted student
            if student_name in self.grades:
                del self.grades[student_name]
                self.update_grade_display()
        else:
            messagebox.showwarning("Selection Error", "Please select a student to remove.")

    def search_student(self):
        search_term = self.search_entry.get().strip()
        if search_term:
            matching_students = [student for student in self.students if search_term.lower() in student.lower()]
            self.student_listbox.delete(0, tk.END)  # Clear the listbox
            if matching_students:
                for student in matching_students:
                    self.student_listbox.insert(tk.END, student)
            else:
                messagebox.showinfo("No Results", "No matching students found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a search term.")

    def add_subject(self):
        subject_name = self.subject_entry.get()
        if subject_name:
            if subject_name not in self.subjects:
                self.subjects.append(subject_name)
                self.subject_listbox.insert(tk.END, subject_name)
                self.grade_subject_menu['values'] = self.subjects
                self.subject_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Duplicate Subject", "This subject is already in the list.")
        else:
            messagebox.showwarning("Input Error", "Please enter a subject name.")

    def remove_subject(self):
        selected_subject_index = self.subject_listbox.curselection()
        if selected_subject_index:
            subject_name = self.subject_listbox.get(selected_subject_index)
            self.subjects.remove(subject_name)
            self.subject_listbox.delete(selected_subject_index)
            self.grade_subject_menu['values'] = self.subjects
        else:
            messagebox.showwarning("Selection Error", "Please select a subject to remove.")

    def assign_grade(self):
        student_name = self.grade_student_menu.get()
        subject_name = self.grade_subject_menu.get()
        grade = self.grade_entry.get()

        if not student_name or not subject_name or not grade:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        # Check if the student and subject exist
        if student_name not in self.students:
            messagebox.showwarning("Student Not Found", f"Student '{student_name}' does not exist.")
            return
        if subject_name not in self.subjects:
            messagebox.showwarning("Subject Not Found", f"Subject '{subject_name}' does not exist.")
            return

        # Check if the grade is a valid number
        try:
            grade = float(grade)  # Attempt to convert to float
            if grade < 0 or grade > 100:  # Check for reasonable grade range
                raise ValueError("Grade must be between 0 and 100.")
        except ValueError as ve:
            messagebox.showwarning("Invalid Grade", str(ve))
            return

        # Store grade in the dictionary
        if student_name not in self.grades:
            self.grades[student_name] = {}
        self.grades[student_name][subject_name] = grade

        self.update_grade_display()
        self.grade_entry.delete(0, tk.END)

    def update_grade_display(self):
        # Clear the current treeview
        for row in self.grade_tree.get_children():
            self.grade_tree.delete(row)

        # Populate the treeview with grades
        for student, subjects in self.grades.items():
            for subject, grade in subjects.items():
                self.grade_tree.insert("", "end", values=(student, subject, grade))

    def show_about(self):
        messagebox.showinfo("About", "Student Management System\nVersion 1.0\nDeveloped using Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()

