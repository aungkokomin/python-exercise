import csv
from pathlib import Path
rows = []

with Path('../data-list.csv').open(newline="",encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append({
            'id': row['id'],
            'name': row['name'],
            'age': row['age']
        })
    print(rows)
    nameolderthanequal28 = [row['name'] for row in rows if int(row['age']) >= 28]
    print(nameolderthanequal28)

# Better way to of above code with error handling:
# import csv
# from pathlib import Path

# csv_path = Path("../data-list.csv")
# names_ge_28 = []

# with csv_path.open(newline="", encoding="utf-8") as f:
#     for r in csv.DictReader(f):
#         try:
#             if int(r["age"]) >= 28:
#                 names_ge_28.append(r["name"].strip())
#         except (KeyError, ValueError):
#             pass  # skip bad rows

# print(",".join(names_ge_28))