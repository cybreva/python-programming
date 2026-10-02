import csv

with open("newfile.txt","r") as f:
    logs = f.readlines()

    with open("newfile.csv","r") as f:
        reader = csv.DictReader(f)
        for row in reader :
            print(row["Timestamp"] ,row["Event_ID"])
