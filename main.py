import csv

partidos = []

with open("liga_2023.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["local_team"] == "Belgrano" or row["visitor_team"] == "Belgrano":
            partidos.append(row)

print(f"Partidos encontrados: {len(partidos)}")
print(partidos[0])