import csv
from collections import Counter

with open('popupdb.csv', newline='') as csvfile:
    scamreader = csv.DictReader(csvfile)
    country_counter = Counter()
    for scam in scamreader:
        p = scam["Number"]
        country = p[:p.find("-")]
        country_counter[country]+=1

print(country_counter.most_common(10))