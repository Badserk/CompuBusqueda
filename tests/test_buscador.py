from src.buscador import buscar_empleos

def test_busqueda():
    url = "https://co.computrabajo.com/empleos-de-informatica-y-telecom-en-bogota-dc?sal=4&iex=4&cont=5"
    resultados = buscar_empleos(url)
    assert isinstance(resultados, list)
    assert all('titulo' in r for r in resultados)
