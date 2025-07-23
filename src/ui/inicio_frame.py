import customtkinter as ctk
from utils.selenium_utils import configurar_driver
from logic.buscador import buscar_empleos

class InicioFrame(ctk.CTkFrame):
    def __init__(self, master, callback_resultados):
        super().__init__(master)
        self.callback_resultados = callback_resultados

        ctk.CTkLabel(self, text="Buscador de Empleos", font=("Arial", 24)).pack(pady=20)
        ctk.CTkButton(self, text="Buscar Ofertas", command=self.buscar).pack(pady=20)
        self.label_estado = ctk.CTkLabel(self, text="")
        self.label_estado.pack()

    def buscar(self):
        self.label_estado.configure(text="Buscando, por favor espera...")
        self.update_idletasks()

        driver = configurar_driver()
        try:
            url = "https://co.computrabajo.com/empleos-en-bogota-dc-jornada-tiempo-completo?sal=1&cont=5"
            resultados = buscar_empleos(url, driver)
        except Exception as e:
            resultados = []
            print("❌ Error en la búsqueda:", e)
        finally:
            driver.quit()

        self.callback_resultados(resultados)
