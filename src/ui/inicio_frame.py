# Importa CustomTkinter para crear interfaces modernas
import customtkinter as ctk

# Importa la función que configura el navegador con Selenium
from utils.selenium_utils import configurar_driver

# Importa la lógica para buscar empleos en una URL
from logic.buscador import buscar_empleos

class InicioFrame(ctk.CTkFrame):
    """
    Frame inicial de la aplicación.
    Permite al usuario iniciar la búsqueda de empleos y muestra el estado del proceso.
    """

    def __init__(self, master, callback_resultados):
        """
        Constructor del frame de inicio.

        Args:
            master (widget): Contenedor padre, normalmente la ventana principal.
            callback_resultados (function): Función que será llamada al terminar la búsqueda
                                            para cambiar a la vista de resultados.
        """
        super().__init__(master)
        self.callback_resultados = callback_resultados

        # Título principal
        ctk.CTkLabel(self, text="Buscador de Empleos", font=("Arial", 24)).pack(pady=20)

        # Botón que inicia la búsqueda
        ctk.CTkButton(self, text="Buscar Ofertas", command=self.buscar).pack(pady=20)

        # Etiqueta para mostrar el estado de la búsqueda
        self.label_estado = ctk.CTkLabel(self, text="")
        self.label_estado.pack()

    def buscar(self):
        """
        Lógica que se ejecuta al presionar el botón "Buscar Ofertas".
        Inicia el navegador, realiza la búsqueda, y devuelve los resultados al frame principal.
        """
        # Indica al usuario que la búsqueda está en proceso
        self.label_estado.configure(text="Buscando, por favor espera...")
        self.update_idletasks()

        # Configura el navegador usando Selenium
        driver = configurar_driver()
        try:
            # URL objetivo de búsqueda de empleos
            url = "https://co.computrabajo.com/empleos-en-bogota-dc-jornada-tiempo-completo?sal=1&cont=5"
            
            # Ejecuta la búsqueda y obtiene los resultados
            resultados = buscar_empleos(url, driver)
        except Exception as e:
            resultados = []
            print("❌ Error en la búsqueda:", e)  # Log del error en consola
        finally:
            driver.quit()  # Cierra el navegador

        # Envía los resultados al frame de resultados mediante el callback
        self.callback_resultados(resultados)
