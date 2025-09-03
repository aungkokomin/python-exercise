import csv,random, names

#save data
with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No','Name','Age'])
    randomCount = random.randint(1,10)
    for i in range(randomCount): # Write random number of rows
        writer.writerow([i+1,names.get_full_name(),random.randint(20,40)])
#Load Data
with open('people.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)