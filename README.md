# Student Performance Prediction System

## Overview

The Student Performance Prediction System is a simple Python-based project
that analyzes a student's academic information and gives a performance
score, risk level, and useful recommendations.

The system takes basic details such as attendance percentage, daily study
hours, and previous examination marks.

The project is designed using simple Python concepts such as functions,
conditions, loops, lists, input validation, and modules.

## Features

The project contains three main functional modules:

1. Performance Prediction System
2. Risk Analyzer
3. Recommendation System

Additional features include:

- Student name input
- Attendance validation between 0 and 100
- Study hours validation between 0 and 24
- Previous exam marks validation between 0 and 100
- Prevention of invalid text input
- Performance level calculation
- Academic risk identification
- Personalized recommendations

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

No external Python libraries are required.

## Project Structure

StudentPerformanceProject/

- main.py
- performance.py
- risk.py
- recommendation.py
- utils.py
- README.md
- statement.md

## Modules

### 1. main.py

This is the main file of the project.

It:

- Takes input from the user
- Validates the entered values
- Calls the other project modules
- Displays the final student report

### 2. performance.py

This module calculates the predicted performance score using:

- Attendance percentage
- Daily study hours
- Previous examination marks

### 3. risk.py

This module analyzes the student's academic risk.

The risk level can be:

- Low Risk
- Medium Risk
- High Risk

### 4. recommendation.py

This module gives recommendations based on the student's performance.

Examples:

- Improve attendance
- Increase study hours
- Revise weak topics
- Practice more questions
- Continue the current study routine

### 5. utils.py

This module converts the performance score into a performance level.

Possible performance levels are:

- Excellent
- Good
- Average
- Needs Improvement

## Input Details

The program accepts:

- Student Name
- Attendance Percentage: 0 to 100
- Daily Study Hours: 0 to 24
- Previous Exam Marks: 0 to 100

## Input Validation

The system validates all numerical inputs.

For example:

- Attendance cannot be below 0 or above 100.
- Daily study hours cannot be below 0 or above 24.
- Previous exam marks cannot be below 0 or above 100.
- If the user enters letters instead of numbers, the program asks for
  the input again instead of crashing.

## Output

The program displays:

- Student Name
- Predicted Performance Score
- Performance Level
- Risk Level
- Personalized Recommendations

## How to Run the Project

### Step 1

Open the project folder in Visual Studio Code.

### Step 2

Open the terminal.

### Step 3

Run:

python main.py

### Step 4

Enter the requested student details.

Example:

Student Name: Rahul

Attendance: 85

Daily Study Hours: 4

Previous Exam Marks: 75

The program will generate the student's performance report.

## Testing

The project can be tested using different input values.

### Test Case 1

Attendance: 90

Study Hours: 4

Previous Marks: 85

Expected Result:

- Good or Excellent performance
- Low academic risk

### Test Case 2

Attendance: 65

Study Hours: 2

Previous Marks: 55

Expected Result:

- Average performance
- Medium academic risk
- Improvement recommendations

### Test Case 3

Attendance: 45

Study Hours: 1

Previous Marks: 30

Expected Result:

- Low performance
- High academic risk
- Recommendations for improvement

### Invalid Input Testing

Study Hours: 30

The system should reject the value because study hours cannot be more
than 24.

Previous Marks: 120

The system should reject the value because marks cannot be more than 100.

Attendance: abc

The program should not crash and should ask the user to enter numbers only.

## Project Workflow

Student Input
        |
        v
Input Validation
        |
        v
Performance Prediction
        |
        v
Risk Analysis
        |
        v
Recommendation Generation
        |
        v
Final Student Report

## Future Enhancements

The project can be improved in the future by adding:

- Graphical User Interface
- Student login system
- Database storage
- Performance history
- Graphs and charts
- Multiple subject analysis
- Teacher dashboard
- Report generation

## Author

Student Project

## Conclusion

The Student Performance Prediction System demonstrates how basic Python
programming concepts can be used to solve a practical academic problem.

The project combines performance prediction, risk analysis, input
validation, and personalized recommendations in a simple modular system.