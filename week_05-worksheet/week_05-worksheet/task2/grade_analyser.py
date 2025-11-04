'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be achieved by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
import os
print("Current working directory:", os.getcwd())
print("Files here:", os.listdir())

import csv

# Ask user for the input file name
input_filename = input("Enter the student data filename: ")

with open(input_filename, 'r') as infile:
    reader = csv.reader(infile)
    output_rows = []

    next(reader)  # Skip the header row

    for row in reader:
        student_id = row[0]
        # Extract valid (non-empty) grades and convert them to floats
        grades = [float(x) for x in row[1:] if x.strip() != '']

        # Calculate average
        if len(grades) > 0:
            average = sum(grades) / len(grades)
        else:
            average = 0.0

        # Determine classification
        if average >= 70:
            classification = "1"
        elif average >= 60:
            classification = "2:1"
        elif average >= 50:
            classification = "2:2"
        elif average >= 40:
            classification = "3"
        else:
            classification = "F"

        # Add result to output list
        output_rows.append([student_id, f"{average:.2f}", classification])

        # Add result to output list
        output_rows.append([student_id, f"{average:.2f}", classification])

# Create output file name
output_filename = input_filename + "_out.csv"

# Write results to new CSV file
with open(output_filename, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(output_rows)

print(f"Results written to {output_filename}")
