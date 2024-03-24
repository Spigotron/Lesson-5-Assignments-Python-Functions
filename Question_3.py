import math

grades = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for grade in grades:
    grade = int(grade)

def average(grades):
    return sum(grades) / len(grades)

def highest(grades):
    return max(grades)

def lowest(grades):
    return min(grades)

print(average(grades))
print(highest(grades))
print(lowest(grades))

def categorize(grades):
    for grade in grades:
        if grade >= 90:
            print(f" Your grade is {grade}, which is an A.")
        elif 80 <= grade <= 89:
            print(f" Your grade is {grade}, which is a B.")
        elif 70 <= grade <= 79:
            print(f" Your grade is {grade}, which is a C.")
        elif 60 <= grade <= 69:
            print(f" Your grade is {grade}, which is a D.")
        elif grade <= 59:
            print(f" Your grade is {grade}, which is an F.")

categorize(grades)