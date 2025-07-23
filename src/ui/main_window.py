import customtkinter as ctk
from ui.inicio_frame import InicioFrame
from ui.resultados_frame import ResultadosFrame

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class BuscadorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Buscador de Empleos")
        self.geometry("800x600")
        self.resizable(False, False)

        self.frame_inicio = InicioFrame(self, self.cambiar_a_resultados)
        self.frame_resultados = ResultadosFrame(self)

        self.frame_inicio.pack(fill="both", expand=True)

    def cambiar_a_resultados(self, resultados):
        self.frame_inicio.pack_forget()
        self.frame_resultados.mostrar_resultados(resultados)
        self.frame_resultados.pack(fill="both", expand=True)
