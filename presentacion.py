CURSO = "Programación 3 - 2° Cuatrimestre"
integrantes = ["Juan Manuel", "Esteban"]

print(f"Equipo de {CURSO}:")
for numero, nombre in enumerate(integrantes, start=1):
    print(f"{numero}. {nombre}")
