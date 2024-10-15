import tkinter as tk
from tkinter import messagebox

# Sample attendance data
attendance_data = {
    'student1': [30, 40],
    'student2': [25, 35],
    'student3': [20, 30],
    # Add more students as needed
}

# Function to calculate attendance percentage
def calculate_percentage(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100

# Function to calculate additional lectures needed
def lectures_needed(attended, total, target=75):
    required = (target / 100) * (total + 1) - attended
    return max(0, int(required) + 1)

# Login function
def login():
    student_id = entry_id.get()
    if student_id in attendance_data:
        attended, total = attendance_data[student_id]
        percentage = calculate_percentage(attended, total)
        lbl_percentage.config(text=f"Attendance: {percentage:.2f}%")
        
        if percentage < 75:
            warning_label.config(text="Warning: Attendance below 75%!", fg="red")
            needed = lectures_needed(attended, total)
            lbl_needed.config(text=f"You need to attend {needed} more lectures to reach 75%.")
        else:
            warning_label.config(text="")
            lbl_needed.config(text="")

    else:
        messagebox.showerror("Error", "Student ID not found.")

# Setting up the main window
root = tk.Tk()
root.title("Automated Attendance System")

# Student ID Label and Entry
lbl_id = tk.Label(root, text="Enter Student ID:")
lbl_id.grid(row=0, column=0, padx=10, pady=10)

entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=10)

# Login Button
btn_login = tk.Button(root, text="Login", command=login)
btn_login.grid(row=0, column=2, padx=10, pady=10)

# Attendance Percentage Label
lbl_percentage = tk.Label(root, text="Attendance: ")
lbl_percentage.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Warning Label
warning_label = tk.Label(root, text="", font=("Helvetica", 12))
warning_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Lectures Needed Label
lbl_needed = tk.Label(root, text="", font=("Helvetica", 12))
lbl_needed.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Run the application
root.mainloop()
