from tkinter import *
from auth import login_gui
from subject_topic import add_subject, add_topic, update_status, view_topics, search_topic
from reminders import add_reminder
from dashboard import dashboard_gui

# Run Login first
login_gui()

root = Tk()
root.title("Syllabus Progress Monitoring System")
root.geometry("400x550")
root.configure(bg="#f5f5dc")  # Beige background

Label(root, text="--- Syllabus Progress Monitoring ---", font=("Arial", 14, "bold"), bg="#2fc814").pack(pady=10)

Button(root, text="Add Subject", width=30, bg="#23f1ee", command=add_subject).pack(pady=5)
Button(root, text="Add Topic & Material", width=30, bg="#29ddf5", command=add_topic).pack(pady=5)
Button(root, text="Update Topic Status", width=30, bg="#47e6ff", command=update_status).pack(pady=5)
Button(root, text="View Pending Topics", width=30, bg="#fc403d", command=lambda: view_topics("Not Started")).pack(pady=5)
Button(root, text="View Completed Topics", width=30, bg="#84fa72", command=lambda: view_topics("Completed")).pack(pady=5)
Button(root, text="View In Progress Topics", width=30, bg="#7ad5e9", command=lambda: view_topics("In Progress")).pack(pady=5)
Button(root, text="Search Topic", width=30, bg="#5cbacd", command=search_topic).pack(pady=5)
Button(root, text="Add Reminder", width=30, bg="#4cfefb", command=add_reminder).pack(pady=5)
Button(root, text="Dashboard", width=30, bg="#3afcfc", command=dashboard_gui).pack(pady=5)
Button(root, text="Exit", width=30, bg="#33d6f6", fg="white", command=root.destroy).pack(pady=5)

root.mainloop()
#updated in feature-update branch

