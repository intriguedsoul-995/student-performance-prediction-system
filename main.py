from performance import calculate_performance
from risk import check_risk
from recommendation import give_recommendation
from utils import get_grade


print("****************************")
print('\n')
print("STUDENT PERFORMANCE SYSTEM")
print('\n')
print("*****************************")

name = input("Enter student name: ")

# Attendance 
while True:
    try:
        attendance = float(input("Enter attendance percentage (0-100):"))

        if 0 <= attendance <= 100:
            break
        else:
            print("Please enter a number between 0 and 100")

    except ValueError:
        print("Please enter numbers only")


# Study hours 
while True:
    try:
        study_hours = float(input("Enter daily study hours (0-24): "))

        if 0 <= study_hours <= 24:
            break
        else:
            print("Please enter study hours between 0 and 24")

    except ValueError:
        print("Please enter numbers only")



# Previous marks 
while True:
    try:
        marks = float(input("Enter previous exam marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Please enter marks between 0 and 100")

    except ValueError:
        print("Please enter numbers only")


performance_score = calculate_performance(
    attendance,
    study_hours,
    marks
)

risk_level = check_risk(
    attendance,
    marks
)

grade = get_grade(performance_score)

recommendations = give_recommendation(
    attendance,
    study_hours,
    marks
)


print("\n-##############################")
print("STUDENT REPORT")
print("##############################")

print("Student Name:", name)
print("Predicted Performance Score:", round(performance_score, 2))
print("Performance Level:", grade)
print("Risk Level:", risk_level)

print("\nRecommendations:")

for recommendation in recommendations:
    print("-", recommendation)

