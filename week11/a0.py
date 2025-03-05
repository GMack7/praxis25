import csv
import json

infile = "week11/1960OCCT.csv"
outfile = "week11/1960black.json"

data = []
with open(infile, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        row["White"] = int(row["White"])
        row["Black"] = int(row["Black"])
        row["Other Races"] = int(row["Other Races"])
        data.append(row) 

sorted_population = sorted(data, key=lambda x: x["Black"], reverse=True)

with open(outfile, "w", encoding="utf-8") as json_file: 
    json.dump(sorted_population, json_file, indent=4)

outfile