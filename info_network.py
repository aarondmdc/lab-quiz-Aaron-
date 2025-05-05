import datetime

name = "Aaron DM Dela Cruz"
student_id = "211-0962"
now = datetime.datetime.now()

print(f"Name: {name}")
print(f"Student ID: {student_id}")
print(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

issue = input("Describe a networking issue you are facing: ") 

with open("network_issues.txt", "w") as file: 
    file.write(f"Name: {name}\n")
    file.write(f"Student ID: {student_id}\n")
    file.write(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Issue: {issue}\n")

