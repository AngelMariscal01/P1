from fastapi import FastAPI
import pandas as pd
from joblib import load
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from joblib import dump, load

app = FastAPI()

dfPlayTimeGenre = pd.read_parquet('./API/PlayTimeGenreParquet.parquet')

dfUserForGenre = pd.read_parquet('./API/UserForGenreParquet.parquet')

dfUserRecommend = pd.read_parquet('./API/UsersRecommendParquet.parquet')

df = pd.read_parquet('./data/ETL.parquet')

nombres = pd.read_parquet('./data/NombresJuegos.parquet')

df = pd.read_parquet('./data/ETL.parquet')
nombres = pd.read_parquet('./data/NombresJuegos.parquet')
features = df.drop(columns=['ItemId', 'Precio', 'TiempoJugado'])
scaler = MinMaxScaler()
df_normalized = scaler.fit_transform(features)
similarities = cosine_similarity(df_normalized)

def PlayTime(genero: str, df):
    # Filtrar el DataFrame para obtener solo las filas que corresponden al género proporcionado
    filtered_df = df[df['Generos'] == genero].copy()  # Crear una copia explícita
    
    # Extraer el año de la columna 'Fecha_Lanzamiento' (sin importar el formato)
    filtered_df['Año_Lanzamiento'] = pd.to_datetime(filtered_df['Fecha_Lanzamiento'], errors='coerce').dt.year
    
    # Eliminar filas con años no válidos
    filtered_df = filtered_df.dropna(subset=['Año_Lanzamiento'])
    
    # Agrupar por año y sumar las horas jugadas para cada año
    horas_jugadas_por_año = filtered_df.groupby('Año_Lanzamiento')['Tiempo_Jugado'].sum()
    
    if horas_jugadas_por_año.empty:
        return None  # Retorna None si no hay datos para el género dado
    
    # Encontrar el año con la suma más alta de horas jugadas
    año_con_mas_horas = horas_jugadas_por_año.idxmax()
    
    return año_con_mas_horas

@app.get("/PlayTimeGenre/{Genre}")
async def PlayTimeGenre(Genre: str):
    año = PlayTime(Genre, dfPlayTimeGenre)
    return  {"Año de lanzamiento con más horas jugadas para el Género ", Genre, " : ", año}

@app.get("/UserForGenre/{Genre}")
async def UserForGenre(Genre: str):
    df_genero = dfUserForGenre[dfUserForGenre['Generos'] == Genre].copy()
    
    # Obtenemos el usuario con más horas jugadas para el género
    usuario_max_horas = df_genero.groupby('IdUsuario')['Tiempo_Jugado'].sum().idxmax()
    
    # Filtramos el DataFrame para obtener solo las filas del usuario con más horas
    df_usuario_max_horas = df_genero[df_genero['IdUsuario'] == usuario_max_horas]
    
    # No necesitamos convertir la columna 'Fecha_Lanzamiento' a tipo datetime
    
    # Eliminamos filas con valores NaN en la columna 'Año_Lanzamiento'
    df_usuario_max_horas = df_usuario_max_horas.dropna(subset=['Año_Lanzamiento'])

    # Agrupamos por 'Año_Lanzamiento' y sumamos las horas jugadas
    horas_por_año = df_usuario_max_horas.groupby('Año_Lanzamiento')['Tiempo_Jugado'].sum()
    
    # Creamos la lista de horas jugadas por año
    lista_horas_por_año = [{"Año": int(año), "Horas": horas} for año, horas in horas_por_año.items()]
    
    return {"Usuario con más horas jugadas para Género " + Genre: usuario_max_horas, "Horas jugadas": lista_horas_por_año}

@app.get("/UsersRecommend/{year}")
def UsersRecommend(year: int):
    # Filtrar los datos según el año dado
    datos_año = dfUserRecommend[dfUserRecommend['year'].astype(int) == year]
    
    # Seleccionar solo las filas donde recommend sea True y sentiment_analysis sea 2 o 1
    recomendados = datos_año[(datos_año['recommend'] == True) & (datos_año['sentiment_analysis'].isin([1, 2]))]
    
    # Contar el número de recomendaciones para cada juego
    conteo_recomendaciones = recomendados['name'].value_counts()

    # Convertir el objeto zip en una lista y luego ordenar los juegos según el número de recomendaciones en orden descendente
    juegos_ordenados = list(conteo_recomendaciones.items())
    
    # Seleccionar los tres primeros juegos
    top_3 = [{"Puesto {}".format(i+1): juego[0]} for i, juego in enumerate(juegos_ordenados[:3])]
    
    return top_3

@app.get("/UsersNotRecommend/{year}")
def UsersNotRecommend(year: int):
    # Filtrar los datos según el año dado
    datos_año = dfUserRecommend[dfUserRecommend['year'].astype(int) == year]
    
    # Seleccionar solo las filas donde recommend sea True y sentiment_analysis sea 2 o 1
    recomendados = datos_año[(datos_año['recommend'] == False) & (datos_año['sentiment_analysis'].isin([0]))]

    # Contar el número de recomendaciones para cada juego
    conteo_recomendaciones = recomendados['name'].value_counts()
    
    # Convertir el objeto zip en una lista y luego ordenar los juegos según el número de recomendaciones en orden descendente
    juegos_ordenados = list(conteo_recomendaciones.items())
    
    # Seleccionar los tres primeros juegos
    top_3 = [{"Puesto {}".format(i+1): juego[0]} for i, juego in enumerate(juegos_ordenados[:3])]
    
    return top_3

@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year: int):
    # Filtrar el DataFrame por el año proporcionado
    df_filtered = dfUserRecommend[dfUserRecommend['year'] == year]
    print(df_filtered.count())
    # Contar la cantidad de registros por cada categoría de análisis de sentimiento
    sentiment_counts = df_filtered['sentiment_analysis'].value_counts()
    
    # Mapear los valores numéricos de la categoría de análisis de sentimiento a sus respectivos nombres
    sentiment_mapping = {2: 'Positive', 1: 'Neutral', 0: 'Negative'}
    
    # Crear el diccionario de retorno con los valores mapeados
    return {sentiment_mapping[key]: value for key, value in sentiment_counts.items()}

@app.get("/recomendacion_juego/{ItemId}")
async def recomendacion_juego(ItemId: int):
    df['ItemId'] = df['ItemId'].astype(str)
    df_resultado = pd.merge(df, nombres, on='ItemId')
    # Seleccionar solo las columnas 'ItemId' y 'Nombre'
    df_resultado = df_resultado[['ItemId', 'Titulo']]
    # Convertir el DataFrame a un formato JSON compatible
    json_resultado = df_resultado.to_dict(orient='records')
    return json_resultado