from urllib.parse import urlencode

FILTROS = {
    "ciudad":{
    "bogota": "bogota-dc"
        },
        #by
    "ordenar_por":{
    "relevance": "relevancia",
    "publicationtime": "fecha",
    "salary": "salario"
        },
        #pubdate
        "fecha":{
        99: "urgente",
        1: "Hoy",
        3: "Últimos 3 días",
        7: "Última Semana",
        15: "Últimos 15 días",
        30: "útimo Mes",
        },
        "categoria": {
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
        },
        "lugar_de_trabajo":{
        "en-remoto": "remoto",
        "hibrido": "hibrido"  
        },
        "experiencia": {
        4: "1 año",
        5: "2 años",
        6: "3-4 años",
        7: "5-10 años",
        8: "10+ año"
        },
        "salario": {
        1: "<700k", 2: "700k", 3: "1M+", 4: "1.5M+", 5: "2M+",
        6: "2.5M+", 7: "3M+", 8: "3.5M+", 9: "4M+", 10: "4.5M+",
        11: "5.5M+", 12: "6M+", 13: "8M+", 14: "10M+",
        15: "12.5M+", 16: "15M+", 17: "18M+"
        },
        "jornada": {
        "jornada-tiempo-completo": "tiempo-completo",
        "jornada-medio-tiempo": "medio tiempo",
        "jornada-por-horas": "por horas",
        "jornada-beca-practicas": "beca practicas"
        },
        
        "contrato": {
        4: "obra_labor",
        5: "indefinido",
        6: "fijo",
        2: "aprendizaje",
        3: "prestacion",
        1: "ocasional"
        },
        "discapacidad":{
        0: "no",
        1: "si"

        }

    }

def construir_url(ordenar_por: str, fecha: str, categoria: str, ciudad: str, experiencia=None, salario=None, jornada=None, contrato=None, discapacidad=None):
    categoria_slug = FILTROS["categoria"].get(categoria, "").lower().replace("/", "").replace(" ", "-")
    ciudad_slug = ciudad.lower().replace(" ", "-")

    # Base de la URL
    if jornada in FILTROS["jornada"]:
        base = f"https://co.computrabajo.com/empleos-en-{ciudad_slug}-jornada-{FILTROS['jornada'][jornada]}"
    else:
        base = f"https://co.computrabajo.com/empleos-de-{categoria_slug}-en-{ciudad_slug}"

    params = {}

    # Ojo: usamos el ID directamente
    if isinstance(ordenar_por, str):
        params["by"] = ordenar_por
        
    if isinstance(fecha, int):
        params["pubdate"] = fecha
        
    #if isinstance(categoria, int):
    #    params[""]
    
    if isinstance(experiencia, int):
        params["iex"] = experiencia
        
    if isinstance(salario, int):
        params["sal"] = salario
        
    #if isinstance(jornada,str):
    #    params[""] = jornada

    if isinstance(contrato, int):
        params["cont"] = contrato

    if isinstance(discapacidad, int):
        params["dis"] = discapacidad
        

        



    return base + "?" + urlencode(params) if params else base
