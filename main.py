from data.clean.cleanData import clean_data
from data.analisis import analyze_data

ciudades = clean_data("data/raw/ciudades.csv")
eventos = clean_data("data/raw/eventos.csv")

resultado = analyze_data(eventos, ciudades)

print("EVENTOS POR CIUDAD:", resultado)