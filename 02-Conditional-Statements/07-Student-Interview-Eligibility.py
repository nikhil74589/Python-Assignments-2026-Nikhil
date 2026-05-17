# Students interview eligibility checker.

academic_score = float(input("Enter Academic Score (%): "))
attendance = float(input("Enter Attendance Percentage (%): "))
activity = input("Participated in Extracurricular Activities? (Yes/No): ")

# Checking eligibility conditions.

if academic_score >= 60 and attendance >= 75 and activity.lower() == "yes":
    print("Eligible for Interview")
else:
    print("Not Eligible for Interview")