def analyze_data(df_eventos, df_ciudades):
    mapa_ciudades = dict(zip(df_ciudades["id"].astype(str), df_ciudades["ciudad"]))

    resumen = {}

    for _, row in df_eventos.iterrows():
        id_c = str(row["id_ciudad"])

        ciudad = mapa_ciudades.get(id_c)

        if not ciudad:
            continue

        if ciudad in resumen:
            resumen[ciudad] += 1
        else:
            resumen[ciudad] = 1

    return resumen