# STUDENT RESULT CHECKER PROGRAM
print("===================================")
print("      STUDENT RESULT CHECKER       ")
print("===================================")

# Collecting student details
student_name = input("Enter Student Name: ")
student_passcode = input("Enter passcode")

# Collecting student score
score = int(input("Enter Student Score (0 - 100): "))

# Checking if score is valid
if score < 0 or score > 100:
    print("Invalid score entered!")
    print("Score must be between 0 and 100.")

else:
    print("\n========= RESULT =========")

    # Determining grade and performance
    if score >= 70:
        grade = "A"
        remark = "Excellent"
        status = "PASS"

    elif score >= 60:
        grade = "B"
        remark = "Very Good"
        status = "PASS"

    elif score >= 50:
        grade = "C"
        remark = "Good"
        status = "PASS"

    elif score >= 45:
        grade = "D"
        remark = "Fair"
        status = "PASS"

    elif score >= 40:
        grade = "E"
        remark = "Poor"
        status = "PASS"

    else:
        grade = "F"
        remark = "Fail"
        status = "FAILED"
    # Displaying student result
    print(f"Student Name : {student_name}")
    print(f"Student passcode : {student_passcode}")
    print(f"Score        : {score}")
    print(f"Grade        : {grade}")
    print(f"Remark       : {remark}")
    print(f"Status       : {status}")

    print("============================")
    print(" Result Processing Complete ")
    print("============================")