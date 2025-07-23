from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
from buscador import buscar_empleos

def configurar_driver():
    """
    #!Configura y retorna una instancia de WebDriver con opciones de evasión de detección.
    
    """
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled") #? desactiva la detección del 'bot'
    options.add_argument("--headless=new") #? abre el navegador sin ventana

    servicio = Service("drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=servicio, options=options)

    # Aplicar técnicas de evasión de detección automatizada
    stealth(driver,
            languages=["es-ES", "es"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
    )

    return driver

def mostrar_resultados(resultados):
    """
    Imprime los resultados de búsqueda en consola.
    """
    if resultados:
        print(f"\n🔎 Se encontraron {len(resultados)} ofertas:\n")
        for r in resultados:
            print(f"📌 {r['titulo']} | 🏢 {r['empresa']} | 💰 {r['salario']}")
    else:
        print("❌ No se encontraron ofertas.")

if __name__ == "__main__":
    url = "https://co.computrabajo.com/empleos-en-bogota-dc-jornada-tiempo-completo?sal=1&cont=5"
    driver = configurar_driver()

    try:
        resultados = buscar_empleos(url, driver)
        mostrar_resultados(resultados)
    finally:
        driver.quit()
