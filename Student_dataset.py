
import csv

students = [
    {
        "Student ID": "CS001",
        "Department": "Computer Science",
        "Level": 100,
        "Attendance Percentage": 85,
        "Average Examination Score": 78
    },
    {
        "Student ID": "CS002",
        "Department": "Computer Science",
        "Level": 200,
        "Attendance Percentage": 90,
        "Average Examination Score": 82
    },
    {
        "Student ID": "CY003",
        "Department": "Cybersecurity",
        "Level": 300,
        "Attendance Percentage": 75,
        "Average Examination Score": 69
    },
    {
        "Student ID": "IT004",
        "Department": "Information Technology",
        "Level": 200,
        "Attendance Percentage": 88,
        "Average Examination Score": 91
    },
    {
        "Student ID": "CS005",
        "Department": "Computer Science",
        "Level": 300,
        "Attendance Percentage": 95,
        "Average Examination Score": 86
    },
    {
        "Student ID": "CY006",
        "Department": "Cybersecurity",
        "Level": 100,
        "Attendance Percentage": 80,
        "Average Examination Score": 74
    },
    {
        "Student ID": "IT007",
        "Department": "Information Technology",
        "Level": 300,
        "Attendance Percentage": 92,
        "Average Examination Score": 88
    },
    {
        "Student ID": "CS008",
        "Department": "Computer Science",
        "Level": 200,
        "Attendance Percentage": 70,
        "Average Examination Score": 65
    }
]

with open("student_dataset.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print("Student dataset created successfully!")
