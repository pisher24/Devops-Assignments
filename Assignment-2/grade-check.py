# Program to calculate grade based on score

# Take input from user
score = int(input("Enter your score: "))

# Check grade using if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print result
print("Your grade is:", grade)


