# Python writing files (.txt, .json, .csv)

# --------- .txt ---------
txt_data = "I like pizza!"

file_path = "output.txt"

try:
   with open(file_path, 'w') as file:
      file.write(txt_data)
      print(f".txt file '{file_path}' has been created successfully")
except FileExistsError:
   print("That file already exists")

# --------- .json ---------

import json

employee = {
   "name": "Spongebob",
   "age": 30,
   "job": "Cook"
}

file_path = "output.json"

try:
    with open(file_path, 'w') as file:
        json.dump(employee, file, indent=4)

    print(f"JSON file '{file_path}' has been created successfully")
except FileExistsError:
    print("That file already exists!")

# --------- .csv---------
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")