from bs4 import BeautifulSoup

def buscar_empleos(url, driver):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    ofertas = []

    for box in soup.select("article.box_offer"):
        titulo = box.find("h2")
        empresa = box.find("a", class_="fs16")
        salario = box.find("li", class_="bV")

        ofertas.append({
            "titulo": titulo.text.strip() if titulo else "Sin título",
            "empresa": empresa.text.strip() if empresa else "No especificada",
            "salario": salario.text.strip() if salario else "No informado"
        })

    return ofertas
