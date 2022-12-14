import json
import csv

with open('dane_json.json', 'r') as f:
    data = json.load(f)

members = data['members']

data_file = open('data_file.csv', 'w')

csv_writer = csv.writer(data_file)

count=0
for m in members:
    if count==0:
        header=m.keys()
        csv_writer.writerow(header)
        count+=1
    csv_writer.writerow(m.values())
data_file.close()
