import csv

partidos = []

# Si aparece Belgrano como local o visitante, lo guardo en la lista partidos
with open("liga_2023.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["local_team"] == "Belgrano" or row["visitor_team"] == "Belgrano":
            partidos.append(row)

print(f"Partidos encontrados: {len(partidos)}")

# Creo lista con equipos de primera actuales
equipos_primera_2026 = [
    "River Plate", "Boca Juniors", "Racing Club", "Independiente",
    "San Lorenzo", "Huracan", "Velez", "Newells", "Rosario Central",
    "Lanus", "Estudiantes (LP)", "Talleres (C)", "Atl Tucuman",
    "Argentinos", "Sarmiento (J)", "Instituto", "Barracas Central",
    "Def y Justicia", "Central Cba (SdE)", "Platense", "Tigre",
    "Union", "Banfield", "Gimnasia (LP)", "Gimnasia (M)",
    "Ind Rivadavia", "Aldosivi", "Riestra", "Estudiantes RC"
]

# Creo lista de partidos contra equipos de primera actual
partidos_primera = []

for partido in partidos:
    if partido["local_team"] == "Belgrano":
        rival = partido["visitor_team"]
    else:
        rival = partido["local_team"]
    
    if rival in equipos_primera_2026:
        partidos_primera.append(partido)

print(f"Partidos contra equipos de primera actual: {len(partidos_primera)}")

# Creo diccionario con historial contra cada rival

historial = {}

for rival in equipos_primera_2026:
    historial[rival] = {"Victorias":0,"Empates":0,"Derrotas":0}

# Recorro los partidos y genero los contadores

for partido in partidos_primera:
    if partido["local_team"] == "Belgrano":
        rival = partido["visitor_team"]
        resultado_belgrano = int(partido["local_result"])
        resultado_rival = int(partido["visitor_result"])
        if resultado_rival < resultado_belgrano:
            historial[rival]["Victorias"] +=1
        elif resultado_rival > resultado_belgrano:
            historial[rival]["Derrotas"] +=1
        else:
            historial[rival]["Empates"] +=1
    else:
        rival = partido["local_team"]
        resultado_belgrano = int(partido["visitor_result"])
        resultado_rival = int(partido["local_result"])
        if resultado_rival < resultado_belgrano:
            historial[rival]["Victorias"] +=1
        elif resultado_rival > resultado_belgrano:
            historial[rival]["Derrotas"] +=1
        else:
            historial[rival]["Empates"] +=1

print(historial["River Plate"])