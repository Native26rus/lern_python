from collections import Counter
import csv, json

counter, summator = Counter(), 0
ls_files = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']

for name_file in ls_files:
    with open(name_file, encoding='utf8') as file:
       data = csv.reader(file)
       head = next(data)

       for line in data:
           prod, summ = line[0], sum(map(int,line[1:]))
           counter.update({prod:summ})

with open('prices.json', encoding='utf8') as file:
    data = json.load(file)
    for k in counter:
        summator += counter[k] * data[k]

print(summator)
