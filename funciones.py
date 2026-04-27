import pandas as pd

def cargar_csv(ruta):
    return pd.read_csv(ruta)

def limpiar_ciudades(df):
    df["ciudad"] = df["ciudad"].str.strip()
    df["region"] = df["region"].str.lower().str.strip()
    df["poblacion"] = df["poblacion"].fillna(0)
    return df

def limpiar_eventos(df):
    df["tipo"] = df["tipo"].str.lower().str.strip()
    df["estado"] = df["estado"].str.lower().str.strip()
    df["temperatura"] = df["temperatura"].fillna(0)
    return df

def filtrar_activos(df):
    return df[df["estado"] == "activo"]

def filtrar_temperatura(df):
    return df[df["temperatura"] <= 50]

def combinar(ciudades, eventos):
    return pd.merge(ciudades, eventos, left_on="id", right_on="id_ciudad")

def evento_mas_comun(df):
    return df["tipo"].value_counts().idxmax()

def promedio_temperatura(df):
    return df.groupby("tipo")["temperatura"].mean()

def contar_lluvias(df):
    return df[df["tipo"] == "lluvia"].shape[0]