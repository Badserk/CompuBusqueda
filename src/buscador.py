from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_empleos(url, driver):
    """
    Extrae las ofertas de empleo desde la URL dada usando Selenium.

    Returns:
        list[dict]: Lista de empleos con título, empresa, salario y ubicación.
    """
    driver.get(url)
    empleos = []

    try:
        WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article.box_offer"))
        )
    except Exception as e:
        print(f"⚠️ Las ofertas no cargaron correctamente: {e}")
        return []

    ofertas = driver.find_elements(By.CSS_SELECTOR, "article.box_offer")

    for oferta in ofertas:
        try:
            # Título
            titulo_elem = oferta.find_element(By.CSS_SELECTOR, "h2.fs18 a")
            titulo = titulo_elem.text.strip()

            # Empresa: puede estar en <a> o como texto plano
            empresa_elem = oferta.find_elements(By.CSS_SELECTOR, "a.fc_base.t_ellipsis")
            if empresa_elem:
                empresa = empresa_elem[0].text.strip()
            else:
                # Alternativa: empresa como texto directo
                empresa_fallback = oferta.find_elements(By.CSS_SELECTOR, "p.dFlex.vm_fx.fs16.fc_base.mt5")
                empresa = empresa_fallback[0].text.strip() if empresa_fallback else "Desconocida"


            # Salario
            spans_salario = oferta.find_elements(By.CSS_SELECTOR, "div.fs13.mt15 span.dIB")
            salario = "No especificado"
            for span in spans_salario:
                if "$" in span.text:
                    salario = span.text.strip()
                    break

            # Ubicación
            ubicacion_elem = oferta.find_elements(By.CSS_SELECTOR, "p.fs16.fc_base.mt5 span")
            ubicacion = ubicacion_elem[0].text.strip() if ubicacion_elem else "Ubicación no especificada"

            empleos.append({
                "titulo": titulo,
                "empresa": empresa,
                "salario": salario,
                "ubicacion": ubicacion,
            })

        except Exception as e:
            print("⚠️ Error al procesar una oferta:", e)
            continue

    return empleos
