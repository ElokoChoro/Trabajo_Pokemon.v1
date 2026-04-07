#2

print(df[df["Tipo 1"]== "Fuego"])
print(df[["Nombre", "Tipo 1", "Ataque", "Velocidad"]])

#3

mayor_defensa = df[df["Defensa"] == df["Defensa"].max()]
print(mayor_defensa)
