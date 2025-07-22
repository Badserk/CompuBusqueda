def construir_url(area, ciudad, salario=None, experiencia=None, contrato=None):
    base = f"https://co.computrabajo.com/empleos-de-{area}-en-{ciudad}"
    params = []

    if salario:
        params.append(f"sal={salario}")
    if experiencia:
        params.append(f"iex={experiencia}")
    if contrato:
        params.append(f"cont={contrato}")

    if params:
        return f"{base}?" + "&".join(params)
    return base
