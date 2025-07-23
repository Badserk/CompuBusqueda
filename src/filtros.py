from urllib.parse import urlencode

FILTROS = {
    "experiencia": {
        4: "1 año",
        5: "2 años",
        6: "3-4 años",
        7: "5-10 años",
        8: "10+ año",
        None: None
    },
    "salario": {
        1: "<700k", 2: "700k", 3: "1M+", 4: "1.5M+", 5: "2M+",
        6: "2.5M+", 7: "3M+", 8: "3.5M+", 9: "4M+", 10: "4.5M+",
        11: "5.5M+", 12: "6M+", 13: "8M+", 14: "10M+",
        15: "12.5M+", 16: "15M+", 17: "18M+"
    },
    "contrato": {
        1: "ocasional", 2: "aprendizaje", 3: "prestacion",
        4: "obra_labor", 5: "indefinido", 6: "fijo"
    },
    "jornada": {
        "tiempo_completo": "tiempo-completo",
        "medio_tiempo": "medio-tiempo",
        "por_horas": "por-horas",
        "practicas": "beca-practicas"
    },
    "area": {
        1: "Ventas",
        2: "CallCenter / Telemercadeo",
        3: "Almacén / Logística / Transporte",
        4: "Producción / Operarios / Manufactura",
        5: "Otros",
        6: "Medicina / Salud",
        7: "Administración / Oficina",
        8: "Atención a clientes",
        9: "Mantenimiento y Reparaciones Técnicas",
        10: "Contabilidad / Finanzas",
        11: "Servicios Generales, Aseo y Seguridad",
        12: "Informática / Telecomunicaciones",
        13: "Construcción y obra",
        14: "Hostelería / Turismo",
        15: "Recursos Humanos",
        16: "Ingeniería",
        17: "Mercadotecnia / Publicidad / Comunicación",
        18: "Docencia",
        19: "Compras / Comercio Exterior",
        20: "Investigación y Calidad",
        21: "Diseño / Artes gráficas",
        22: "Legal / Asesoría",
        23: "Dirección / Gerencia"
    }
}

def construir_url(area: str, ciudad: str, salario=None, experiencia=None, contrato=None, jornada=None):
    area_slug = area.lower().replace("/", "").replace(" ", "-")
    ciudad_slug = ciudad.lower().replace(" ", "-")

    # Base de la URL
    if jornada in FILTROS["jornada"]:
        base = f"https://co.computrabajo.com/empleos-en-{ciudad_slug}-jornada-{FILTROS['jornada'][jornada]}"
    else:
        base = f"https://co.computrabajo.com/empleos-de-{area_slug}-en-{ciudad_slug}"

    params = {}

    # Ojo: usamos el ID directamente
    if isinstance(salario, int):
        params["sal"] = salario
    if isinstance(experiencia, int):
        params["iex"] = experiencia
    if isinstance(contrato, int):
        params["cont"] = contrato

    return base + "?" + urlencode(params) if params else base
