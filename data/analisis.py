def analyze_data(eventos, ciudades):
    mapa_ciudades = {}

    for c in ciudades:
        mapa_ciudades[str(c["id"])] = c["ciudad"]

    resumen = {}

    for evento in eventos:
        id_c = evento.get("id_ciudad")

        ciudad = mapa_ciudades.get(id_c)

        if not ciudad:
            continue

        if ciudad in resumen:
            resumen[ciudad] += 1
        else:
            resumen[ciudad] = 1

    return resumen