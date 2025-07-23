# Importa CustomTkinter para crear interfaces modernas y personalizables
import customtkinter as ctk

# Importa los frames personalizados de la aplicación
from ui.inicio_frame import InicioFrame
from ui.resultados_frame import ResultadosFrame

# Establece el modo de apariencia (oscuro) y el tema de color (azul)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class BuscadorApp(ctk.CTk):
    """
    Clase principal de la aplicación de búsqueda de empleos.
    Administra la ventana principal y el cambio entre las vistas (inicio y resultados).
    Hereda de CTk, la versión personalizada de la ventana principal de Tkinter.
    """

    def __init__(self):
        """
        Inicializa la ventana principal de la aplicación y configura los frames.
        """
        super().__init__()

        # Configuración básica de la ventana
        self.title("Buscador de Empleos")
        self.geometry("800x600")
        #self.resizable(False, False)  # Desactiva el cambio de tamaño

        # Crea e inicializa los frames (vistas)
        self.frame_inicio = InicioFrame(self, self.cambiar_a_resultados)
        self.frame_resultados = ResultadosFrame(self)

        # Muestra inicialmente el frame de inicio
        self.frame_inicio.pack(fill="both", expand=True)

    def cambiar_a_resultados(self, resultados):
        """
        Cambia de la vista de inicio a la vista de resultados y muestra los datos.

        Args:
            resultados (list): Lista de ofertas de empleo a mostrar.
        """
        self.frame_inicio.pack_forget()  # Oculta el frame de inicio
        self.frame_resultados.mostrar_resultados(resultados)  # Carga los resultados en la otra vista
        self.frame_resultados.pack(fill="both", expand=True)  # Muestra el frame de resultados
