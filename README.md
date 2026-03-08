# Belgrano Predictor 2026

Herramienta que analiza el historial histórico del fútbol argentino desde 1931 hasta 2026
para predecir los resultados de Belgrano en el torneo 2026, basándose en enfrentamientos previos contra cada rival.

## ¿Cómo funciona?

El programa lee un archivo CSV con partidos históricos de la liga argentina, filtra los partidos de Belgrano y construye un historial detallado contra cada equipo de Primera División actual, diferenciando resultados de local y visitante. Luego, utilizando el fixture 2026, genera una predicción para cada partido basada en la probabilidad histórica de cada resultado.

## ¿Cómo correrlo?

**Requisitos:** Python 3

**Ejecutar:**
```bash
python main.py
```