import csv
import random

partidos = []

# Si aparece Belgrano como local o visitante, lo guardo en la lista partidos
with open("liga_2023.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["local_team"] == "Belgrano" or row["visitor_team"] == "Belgrano":
            partidos.append(row)

# Creo lista con equipos de primera actuales
equipos_primera_2026 = [
    "River Plate", "Boca Juniors", "Racing Club", "Independiente",
    "San Lorenzo", "Huracan", "Velez", "Newells", "Rosario Central",
    "Lanus", "Estudiantes (LP)", "Talleres (C)", "Atl Tucuman",
    "Argentinos", "Sarmiento (J)", "Instituto", "Barracas Central",
    "Def y Justicia", "Central Cba (SdE)", "Platense", "Tigre",
    "Union", "Banfield", "Gimnasia (LP)", "Gimnasia (M)",
    "Ind Rivadavia", "Aldosivi", "Riestra", "Estudiantes (RC)"
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

# Creo diccionario con historial contra cada rival siendo local, visitante y total

historial = {}

for rival in equipos_primera_2026:
    historial[rival] = {"Local":{"Victorias":0,"Empates":0,"Derrotas":0},
                        "Visitante":{"Victorias":0,"Empates":0,"Derrotas":0},
                        "Total":{"Victorias":0,"Empates":0,"Derrotas":0}}

# Recorro los partidos y genero los contadores

for partido in partidos_primera:
    if partido["local_team"] == "Belgrano":
        rival = partido["visitor_team"]
        resultado_belgrano = int(partido["local_result"])
        resultado_rival = int(partido["visitor_result"])
        if resultado_rival < resultado_belgrano:
            historial[rival]["Local"]["Victorias"] +=1
            historial[rival]["Total"]["Victorias"] +=1
        elif resultado_rival > resultado_belgrano:
            historial[rival]["Local"]["Derrotas"] +=1
            historial[rival]["Total"]["Derrotas"] +=1
        else:
            historial[rival]["Local"]["Empates"] +=1
            historial[rival]["Total"]["Empates"] +=1
    else:
        rival = partido["local_team"]
        resultado_belgrano = int(partido["visitor_result"])
        resultado_rival = int(partido["local_result"])
        if resultado_rival < resultado_belgrano:
            historial[rival]["Visitante"]["Victorias"] +=1
            historial[rival]["Total"]["Victorias"] +=1
        elif resultado_rival > resultado_belgrano:
            historial[rival]["Visitante"]["Derrotas"] +=1
            historial[rival]["Total"]["Derrotas"] +=1
        else:
            historial[rival]["Visitante"]["Empates"] +=1
            historial[rival]["Total"]["Empates"] +=1

apertura_2026 = [{"numero":1,"rival":"Rosario Central","condicion":"Visitante"},
                {"numero":2,"rival":"Tigre","condicion":"Local"},
                {"numero":3,"rival":"Argentinos","condicion":"Visitante"},
                {"numero":4,"rival":"Banfield","condicion":"Local"},
                {"numero":5,"rival":"Ind Rivadavia","condicion":"Visitante"},
                {"numero":6,"rival":"Def y Justicia","condicion":"Visitante"},
                {"numero":7,"rival":"Atl Tucuman","condicion":"Local"},
                {"numero":8,"rival":"Huracan","condicion":"Visitante"},
                {"numero":9,"rival":"Sarmiento (J)","condicion":"Local"},
                {"numero":10,"rival":"Estudiantes (RC)","condicion":"Visitante"},
                {"numero":11,"rival":"Talleres (C)","condicion":"Local"},
                {"numero":12,"rival":"Racing Club","condicion":"Local"},
                {"numero":13,"rival":"River Plate","condicion":"Visitante"},
                {"numero":14,"rival":"Aldosivi","condicion":"Local"},
                {"numero":15,"rival":"Barracas Central","condicion":"Visitante"},
                {"numero":16,"rival":"Gimnasia (LP)","condicion":"Local"}]

clausura_2026 = [{"numero":1,"rival":"Rosario Central","condicion":"Local"},
                {"numero":2,"rival":"Tigre","condicion":"Visitante"},
                {"numero":3,"rival":"Argentinos","condicion":"Local"},
                {"numero":4,"rival":"Banfield","condicion":"Visitante"},
                {"numero":5,"rival":"Ind Rivadavia","condicion":"Local"},
                {"numero":6,"rival":"Def y Justicia","condicion":"Local"},
                {"numero":7,"rival":"Atl Tucuman","condicion":"Visitante"},
                {"numero":8,"rival":"Huracan","condicion":"Local"},
                {"numero":9,"rival":"Sarmiento (J)","condicion":"Visitante"},
                {"numero":10,"rival":"Estudiantes (RC)","condicion":"Local"},
                {"numero":11,"rival":"Talleres (C)","condicion":"Visitante"},
                {"numero":12,"rival":"Racing Club","condicion":"Visitante"},
                {"numero":13,"rival":"River Plate","condicion":"Local"},
                {"numero":14,"rival":"Aldosivi","condicion":"Visitante"},
                {"numero":15,"rival":"Barracas Central","condicion":"Local"},
                {"numero":16,"rival":"Gimnasia (LP)","condicion":"Visitante"}]

victorias_apertura = 0
derrotas_apertura = 0
empates_apertura = 0

modo = input("Queres ver el analisis fecha por fecha o ir directo al resultado del  apertura? (fecha/directo): ")

for fecha in apertura_2026:
    numero = fecha["numero"]
    estado_localia = fecha["condicion"]
    rival = fecha["rival"]
    
    if rival not in historial:
        if modo == "fecha":
            print(f"Fecha {numero}: Belgrano vs {rival} ({estado_localia}")
            print("Sin historial disponible contra este rival")
        prediccion = random.choice(["Victoria","Empate","Derrota"])
        if prediccion == "Victoria":
            victorias_apertura += 1
        elif prediccion == "Empate":
            empates_apertura += 1
        else:
            derrotas_apertura += 1
        continue

    ganados = historial[rival][estado_localia]["Victorias"]
    perdidos = historial[rival][estado_localia]["Derrotas"]
    empatados = historial[rival][estado_localia]["Empates"]
    ganados_total = historial[rival]["Total"]["Victorias"]
    perdidos_total = historial[rival]["Total"]["Derrotas"]
    empatados_total = historial[rival]["Total"]["Empates"]
    
    if modo == "fecha":
        print(f"Fecha {numero}: Belgrano vs {rival} ({estado_localia})")
        print(f"Historial como {estado_localia}: Victorias: {ganados} | Empates: {empatados} | Derrotas {perdidos}")
        print(f"Historial total: Victorias: {ganados_total} | Empates: {empatados_total} | Derrotas {perdidos_total}")
        respuesta = input("Queres ver la prediccion? (s/n): ")
    
    victorias_prediccion = ganados + ganados_total
    perdidos_prediccion = perdidos + perdidos_total
    empatados_prediccion = empatados + empatados_total
    opciones = ["Victoria"] * victorias_prediccion + ["Derrota"] * perdidos_prediccion + ["Empate"] * empatados_prediccion
    
    if not opciones:
        prediccion = random.choice(["Victoria","Empate","Derrota"])
    else:
        prediccion = random.choice(opciones)
    
    if prediccion == "Victoria":
        victorias_apertura += 1
    elif prediccion == "Empate":
        empates_apertura += 1
    else:
        derrotas_apertura += 1
    
    if modo == "fecha":
        if respuesta.lower() == "s":
            print(f"-> Prediccion: {prediccion}")
        print()

print(f"\n--- Resultado Apertura 2026 ---")
print(f"Victorias: {victorias_apertura} | Empates: {empates_apertura} | Derrotas: {derrotas_apertura}")
puntos_apertura = victorias_apertura * 3 + empates_apertura
print(f"Puntos proyectados: {puntos_apertura}")
