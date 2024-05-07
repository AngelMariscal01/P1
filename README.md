# Primer Proyecto de Data Science de "SoyHenry"
¡Hola!

Estoy emocionado de compartir con ustedes mi entrega final del primer proyecto individual de Data Science con "SoyHenry".

Este proyecto representa un hito importante en mi camino hacia convertirme en un profesional de la ciencia de datos. A lo largo de este tiempo, he explorado una amplia gama de conceptos, técnicas y herramientas que me han preparado para abordar desafíos reales en este apasionante campo.

En este repositorio, encontrarán todos los elementos necesarios para evaluar mi proyecto. He puesto mucho esfuerzo y dedicación en cada aspecto, y estoy ansioso por recibir sus comentarios y sugerencias.

# Carpeta API
En la carpeta API se encuentra todo el proceso ETL (Extracción, Transformación y Carga) necesario para implementar las siguientes funciones:

## Carpeta API

En la carpeta API se encuentra todo el proceso ETL (Extracción, Transformación y Carga) necesario para implementar las siguientes funciones en la api:

### Funciones Disponibles:

1. **PlayTimeGenre( genero : str )**
   - Descripción: Devuelve el año con más horas jugadas para un género específico.
   - Ejemplo de retorno: `{"Año de lanzamiento con más horas jugadas para Género X" : 2013}`

2. **UserForGenre( genero : str )**
   - Descripción: Devuelve el usuario que acumula más horas jugadas para un género dado, junto con una lista de la acumulación de horas jugadas por año.
   - Ejemplo de retorno: `{"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}`

3. **UsersRecommend( año : int )**
   - Descripción: Devuelve el top 3 de juegos más recomendados por usuarios para el año dado, basado en reseñas con comentarios positivos o neutrales.
   - Ejemplo de retorno: `[{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]`

4. **UsersNotRecommend( año : int )**
   - Descripción: Devuelve el top 3 de juegos menos recomendados por usuarios para el año dado, basado en reseñas con comentarios negativos.
   - Ejemplo de retorno: `[{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]`

5. **sentiment_analysis( año : int )**
   - Descripción: Devuelve la cantidad de registros de reseñas de usuarios categorizados con un análisis de sentimiento (Negativo, Neutral, Positivo) para un año de lanzamiento específico.
   - Ejemplo de retorno: `{Negative = 182, Neutral = 120, Positive = 278}`

## Carpeta data

En la carpeta "data" se encuentran los archivos iniciales necesarios para el proyecto, así como los dos dataframes utilizados para el modelo de Machine Learning.

### Archivos Disponibles:

- **ETL.parquet**: Archivo parquet que contiene los datos procesados luego del proceso de Extracción, Transformación y Carga (ETL).
- **NombresJuegos.parquet**: Archivo parquet que contiene los nombres de los juegos.
- **steam_games.json.gz**: Archivo comprimido en formato JSON que contiene datos sobre juegos de Steam.
- **user_reviews.json.gz**: Archivo comprimido en formato JSON que contiene reseñas de usuarios sobre juegos.
- **users_items.json.gz**: Archivo comprimido en formato JSON que contiene datos sobre usuarios y los elementos que poseen.

## Carpeta ETL-EDA

En la carpeta "ETL-EDA" se encuentran los siguientes archivos y notebooks relacionados con el proceso de Extracción, Transformación y Carga (ETL) y el Análisis Exploratorio de Datos (EDA), así como el entrenamiento del modelo de Machine Learning basado en similitud de coseno.

### Archivos y Notebooks Disponibles:

- **ETL.ipynb**: Notebook que contiene el proceso de Extracción, Transformación y Carga (ETL) de los datos.
- **EDA.ipynb**: Notebook que contiene el Análisis Exploratorio de Datos (EDA) realizado sobre los datos.
- **entrenamiento.ipynb**: Notebook que contiene el entrenamiento del modelo de Machine Learning basado en similitud de coseno.

## Archivo `.gitignore`

El archivo `.gitignore` se utiliza para especificar qué archivos y carpetas deben ser ignorados por Git. En este proyecto, se han definido las siguientes exclusiones:

## Archivo `main.py`

El archivo `main.py` es el archivo principal del proyecto, donde se utiliza FastAPI para el despliegue en Render.

## Archivo `requirements.txt`

El archivo `requirements.txt` contiene la lista de dependencias del proyecto que deben ser instaladas.

¡Gracias por la oportunidad de trabajar en este proyecto y por su continuo apoyo en mi viaje de aprendizaje en Data Science!

API: https://p1-3w6m.onrender.com/docs
Video: https://youtu.be/KaDgbmbpEuk
