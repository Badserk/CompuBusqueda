# Importa los módulos necesarios de Selenium para controlar el navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Importa la librería selenium_stealth para evitar la detección de automatización
from selenium_stealth import stealth

# Módulo para manipular rutas del sistema operativo
import os

def configurar_driver():
    """
    Configura e inicializa el driver de Chrome con opciones específicas
    para evitar la detección por parte de los sitios web y ejecutarlo en modo headless.

    Returns:
        driver (webdriver.Chrome): Instancia del navegador Chrome configurado.
    """
    # Opciones personalizadas para el navegador Chrome
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Evita detección de automatización
    options.add_argument("--headless=new")  # Ejecuta el navegador en modo sin cabeza (sin interfaz gráfica)
    options.add_argument("--start-maximized")  # Inicia el navegador maximizado

    # Ruta del ejecutable de ChromeDriver dentro de la carpeta 'drivers'
    chromedriver_path = os.path.join("drivers", "chromedriver.exe")
    
    # Crea un servicio de ChromeDriver con la ruta especificada
    service = Service(chromedriver_path)

    # Inicializa el navegador Chrome con el servicio y las opciones configuradas
    driver = webdriver.Chrome(service=service, options=options)

    # Aplica configuraciones de stealth para simular comportamiento humano
    stealth(driver,
        languages=["es-ES", "es"],             # Idiomas preferidos del navegador
        vendor="Google Inc.",                  # Vendor para emular un navegador real
        platform="Win32",                      # Plataforma del sistema operativo
        webgl_vendor="Intel Inc.",             # Vendor WebGL simulado
        renderer="Intel Iris OpenGL Engine",   # Renderizador WebGL simulado
        fix_hairline=True                      # Corrige errores visuales de línea fina
    )

    return driver  # Retorna el navegador listo para ser utilizado
