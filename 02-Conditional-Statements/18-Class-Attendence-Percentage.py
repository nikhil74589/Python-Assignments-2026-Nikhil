# Input total classes and attended classes :

total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

# Calculate attendance percentage :
attendance_percentage = (attended_classes / total_classes) * 100

# Show attendance percentage ;
print("Attendance Percentage =", attendance_percentage, "%")

# Check eligibility :
if attendance_percentage >= 75:
    print("Eligible to sit in the exam.")
else:
    print("Not eligible to sit in the exam.")