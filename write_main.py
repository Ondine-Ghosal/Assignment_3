# Assignment 3 - Students Marks Processing

'''
How I am going to make this(a dictionary with the total marks obtained by each student)?
    1. Download the sample file, import librarys
    2. Save the data as [student]
    3. read the csv file
    4. see each students highest scores
    5. print them out in a dictionary.  '''
# First I am going to download the sample file, import the librarys and save the data as student.csv.
'''
THIS IS WHAT I AM GOING WITH:
import csv

filename = 'student.csv'''

# Next i am going to read the csv file
'''Iteration1: 
import csv

filename = 'student.csv'
with open('student.csv', 'r') as file:
    filename = file.read()'''

'''
THIS IS WHAT I AM GOING WITH:
import csv

filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)'''

# Now i am going to find each peoples scores and print it out
'''
THIS IS WHAT IM GOING WITH:
import csv

filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)'''

# Next I am going to find the highest scores for each student
'''
Iteration1:
import csv

filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        name = [0]
        scores = map(int, row[1]) # map function is used as a iterator to give a result after applying to something iteratable(tuples, list, etc)
        highest_score = max(score)
        print(f"{name}'s highest score is {highest_score}")'''
        
'''
Iteration2:
import csv  # To read CSV files.

filename = 'student.csv'  
with open(filename, 'r') as file:
    reader = csv.reader(file)  
    next(reader)  # Skip the header.

    scores = {}  # Store highest scores.

    for row in reader:
        name, mark = row[1], int(row[3])
        scores[name] = max(scores(name, mark), mark)  # Keep highest score.

for name, high_score in scores.items():
    print(f"{name}'s highest score is {high_score}")'''

'''
THIS IS WHAT I AM GOING TO USE
import csv  # To read CSV files.

filename = 'student.csv'  
with open(filename, 'r') as file:
    reader = csv.reader(file)  
    next(reader)  # Skip the header.

    scores = {}  # Store highest scores.

    for row in reader:
        name, mark = row[1], int(row[3])
        scores[name] = max(scores.get(name, mark), mark)  # Keep highest score.

for name, high_score in scores.items():
    print(f"{name}'s highest score is {high_score}")'''

# Now i am going to print them in a dictonary

'''
FOR THE FIRST ONE:
import csv  # To read CSV files.

filename = 'student.csv'  
with open(filename, 'r') as file:
    reader = csv.reader(file)  
    next(reader)  # Skip the header.

    scores = {}  # Store highest scores.

    for row in reader:
        name, mark = row[1], int(row[3])

print("Highest marks(for each student) are: ", scores)'''

'''How to calculate each students marks?
    1. read the file
    2. calculate the scores
    3. print them out in dict
    4. combine the 2 together'''

# First read the file
'''
GOING WITH THIS
with open(filename, 'r') as file:
    reader = csv.reader(file)'''

# Then calculate the scores then print it
'''
Iteration1:
import csv

students = {}
filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        name = row[1]  # get the student's name
        marks = int(row[3])  # get the marks
        
        students[name].append(marks)  # Add the marks to the list

for name, marks in students.items():
    total = sum(marks)
    print(f"{name}- Total of marks: {total}")'''

'''
Iteration2:
import csv

students = {}
filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header

    for row in reader:
        name = row[1]  # get the student's name
        marks = int(row[3])  # get the marks
        
        students[name].append(marks)  # Add the marks to the list

for name, marks in students.items():
    total = sum(marks)
    print(f"{name}- Total of marks: {total}")'''
'''
GOING WITH THIS:
import csv

students = {}
filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header

    for row in reader:
        name = row[1]  # get the student's name
        marks = int(row[3])  # get the marks

        if name not in students:
            students[name] = []  # Create a list for the student
        
        students[name].append(marks)  # Add the marks to the list

for name, marks in students.items():
    total = sum(marks)
    print(f"{name}- Total of marks: {total}")'''

# Next print them out in dictonary 
'''
THIS IS WHAT I AM USING:
import csv

students = {}
filename = 'student.csv'
with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header

    for row in reader:
        name = row[1]  # get the student's name
        marks = int(row[3])  # get the marks

        if name not in students:
            students[name] = []  # Create a list for the student
        
        students[name].append(marks)  # Add the marks to the list

# Print the dictionary with total marks for each student
for name, marks in students.items():
    total = sum(marks)
    print(f"Total of marks - {name}: {total}")'''

# Combine the two to get final result
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