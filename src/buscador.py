import requests
from bs4 import BeautifulSoup

def buscar_empleos(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    trabajos = []
    for oferta in soup.select('article.box_offer'):
        titulo = oferta.select_one('a').text.strip()
        empresa = oferta.select_one('span.nomEmp').text.strip() if oferta.select_one('span.nomEmp') else 'No disponible'
        ubicacion = oferta.select_one('p').text.strip()
        enlace = 'https://www.computrabajo.com.co' + oferta.select_one('a')['href']
        trabajos.append({
            'titulo': titulo,
            'empresa': empresa,
            'ubicacion': ubicacion,
            'enlace': enlace
        })
    return trabajos
