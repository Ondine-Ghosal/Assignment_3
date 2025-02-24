import csv

scores = {}
students = {}
filename = 'student.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file) # reads the file
    next(reader)  # skip the header
    for row in reader:
        name, marks = row[1], int(row[3])
        scores[name] = max(scores.get(name, marks), marks)  # Keeps highest score.
        if name not in students:
            students[name] = []  # Create a list for the student
        
        students[name].append(marks)  # Add the marks to the list

print("Highest marks(for each student) are ", scores)   # prints highest marks 
for name, marks in students.items():
    total = sum(marks) # calculates
    print(f"\nTotal of marks - {name}: {total}") # prints out the total marks