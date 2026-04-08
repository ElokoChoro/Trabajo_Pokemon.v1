Trabajo Práctico - Análisis de Datos Pokémon 1ra Generación
Hola, este es nuestro trabajo práctico de análisis de datos usando Python. La tarea consistía en cargar un dataset con los Pokémon de la primera generación y usar la librería Pandas para limpiar los datos, calcular estadísticas y finalmente usar Matplotlib y Seaborn para crear distintos gráficos.

A continuación, explicamos lo que hicimos en cada parte del código:

1 y 2. Carga, Limpieza y Filtrado
En esta primera parte cargamos el archivo CSV original. Le hicimos una limpieza básica eliminando los datos duplicados y rellenando los espacios vacíos del "Tipo 2" con la palabra 'Ninguno'. Además, aplicamos un filtro muy importante para eliminar cualquier Pokémon que tuviera el tipo 'Hada' (ya que ese tipo no existía en la primera generación). Después hicimos algunas pruebas de filtrado, como mostrar en pantalla solo a los Pokémon de tipo Fuego.

3. Estadística Descriptiva
Aquí usamos funciones de Pandas para calcular estadísticas básicas sobre la columna de Ataque, sacando el promedio, la mediana y la moda. También buscamos casos específicos, como encontrar al Pokémon con mayor Defensa y al que tiene la menor Velocidad. Finalmente, contamos cuántos Pokémon tienen doble tipo y calculamos el rango y la desviación estándar de los Puntos de Salud (PS).

4. Visualizaciones
En esta sección generamos 4 gráficos diferentes para visualizar la distribución de los datos:

Un histograma para ver cómo se agrupan los valores de Ataque.

Un gráfico de dispersión (scatter) para comparar el Ataque contra la Velocidad.

Un diagrama de caja (boxplot) para ver los PS separados por el Tipo principal del Pokémon.

Un diagrama de violín para observar la distribución general de la Defensa.

5 y 6. Manipulación y Agrupamiento
Para esta parte, creamos una nueva columna llamada "Poder Total" que suma todas las estadísticas base (Ataque, Defensa, Velocidad y PS) de cada Pokémon. Esto nos permitió ordenar la lista y sacar un Top 5 de los Pokémon más fuertes. Después usamos la función .groupby para agrupar a los Pokémon por su tipo y calcular el promedio, mediana y desviación estándar de sus ataques, además de buscar cuál es el tipo de Pokémon más veloz en promedio.

7. Análisis Exploratorio (EDA)
En esta última sección profundizamos un poco más en los datos. Buscamos qué tipos de Pokémon tienden a tener el mayor ataque y defensa promedio. También calculamos el coeficiente de correlación entre el ataque y la velocidad para ver si están relacionados. Ordenamos los tipos de Pokémon según qué tan dispersos están sus PS y, para terminar, generamos un par de diagramas de caja adicionales para identificar visualmente si existen "valores atípicos" (outliers) en las estadísticas de Ataque y PS.

Eso es todo lo que pide la tarea. Esperamos que esté bien estructurado y que los gráficos ayuden a entender mejor cómo se distribuyen las estadísticas en la primera generación.
