import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------
# 1. CARGA Y LIMPIEZA
# ----------------------
df = pd.read_csv('pokemon_primera_gen.csv')
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df['Tipo 2'] = df['Tipo 2'].fillna('Ninguno')

# ----------------------
# 2. FILTRADO Y SELECCIÓN
# ----------------------
print(df[df["Tipo 1"]== "Fuego"])
print(df[["Nombre", "Tipo 1", "Ataque", "Velocidad"]])

# ----------------------
# 3. ESTADÍSTICA DESCRIPTIVA
# ----------------------
print("promedio de ataque de todos los pokemones")
print(df["Ataque"].mean())
print("Mediana de ataque de todos los pokemons")
print(df["Ataque"].median())
print("Moda de ataque de todos los pokemones")
print(df["Ataque"].mode())

#cual es el pokemons con mayor defensa? y el de menor velocidad?
print("El pokemon con mayor defensa es:")
print(df.loc[df["Defensa"].idxmax()])
print("El pokemon con menor velocidad es:")
print(df.loc[df["Velocidad"].idxmin()])

#¿Cuantos pokemons tienen 2 tipos?
print("El numero de pokemons con 2 tipos es:")
print(df[df["Tipo 2"] != NINGUNO].shape[0])

#rango de los PS
print("El rango de los PS es:")
print(df["PS"].max() - df["PS"].min())

#desviacion estandar de los PS
print("La desviacion estandar de los PS es:")
print(df["PS"].std())

# ----------------------
# 4. VISUALIZACIONES
# ----------------------

#histograma de los valores de ataque
plt.figure()
plt.hist(df["Ataque"], bins=15)
plt.title("Histograma de Ataque")
plt.show()

#grafico de dispersion entre ataque y velocidad

plt.figure()
plt.scatter(df["Ataque"], df["Velocidad"])
plt.xlabel("Ataque")
plt.ylabel("Velocidad")
plt.title("Grafico de dispersion entre Ataque y Velocidad")
plt.show()

#boxplot de los PS por tipo principal (TIPO 1)

plt.figure()
sns.boxplot(x="Tipo 1", y="PS", data=df)
plt.xticks(rotation=45)
plt.show()

#distribucion de la defensa usando diagrama de violin

plt.figure()
sns.violinplot(y=df["Defensa"])
plt.show()

# ----------------------
# 5. MANIPULACIÓN
# ----------------------
df['Poder Total'] = df['Ataque'] + df['Defensa'] + df['Velocidad'] + df['PS']
# Se sumara los stats base del pokemones para ver quién es el más fuerte de la 1ra gen
top_pokemones_con_mas_poder= df.sort_values(by='Poder Total', ascending=False)

# ----------------------
# 6. AGRUPAMIENTO Y ANALISIS POR GRUPO 
# ----------------------
# Usamos std para ver si los tipos son consistentes o tienen mucha diferencia de stats entre los pokemones 
resumen_de_ataque_por_tipo = df.groupby('Tipo 1')['Ataque'].agg(['mean', 'median', 'std'])
tipo_veloz = df.groupby('Tipo 1')['Velocidad'].mean().idxmax()
#al terminar el code agregen este print para los dos item (5,6):
# print("--- Los 5 Pokemones más fuertes ---")
#print(df_ranking.head())
#print(f"\nEl tipo de Pokémon mas veloz en promedio es: {tipo_veloz}") 

