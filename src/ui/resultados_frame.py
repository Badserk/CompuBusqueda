# Importa CustomTkinter, una extensión de Tkinter con soporte para temas oscuros y personalización moderna
import customtkinter as ctk

class ResultadosFrame(ctk.CTkFrame):
    """
    Frame que muestra los resultados de búsqueda en la aplicación.
    Contiene un título, un área desplazable con tarjetas de resultados
    y un botón para volver a la pantalla de inicio.
    """

    def __init__(self, master):
        """
        Constructor del frame de resultados.

        Args:
            master (widget): El contenedor padre, normalmente la ventana principal.
        """
        super().__init__(master)

        # Título de la sección de resultados
        ctk.CTkLabel(self, text="Resultados de Búsqueda", font=("Arial", 20)).pack(pady=10)

        # Frame desplazable donde se mostrarán las tarjetas de resultados
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=750, height=480)
        self.scrollable_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Etiqueta para mostrar el número de resultados o mensajes de estado
        self.resultados_label = ctk.CTkLabel(self, text="")
        self.resultados_label.pack()

        # Botón para volver a la pantalla de inicio
        ctk.CTkButton(self, text="⏪ Volver", command=self.volver_inicio).pack(pady=10)

    def mostrar_resultados(self, resultados):
        """
        Muestra la lista de resultados en el frame desplazable.
        Si no hay resultados, se muestra un mensaje correspondiente.

        Args:
            resultados (list): Lista de diccionarios con información de ofertas de empleo.
        """
        # Limpia resultados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if resultados:
            self.resultados_label.configure(text=f"🔎 Se encontraron {len(resultados)} ofertas:")
            for r in resultados:
                self.crear_tarjeta(r)  # Crea una tarjeta por cada resultado
        else:
            self.resultados_label.configure(text="❌ No se encontraron ofertas.")

    def crear_tarjeta(self, oferta):
        """
        Crea una tarjeta visual con los datos de una oferta de trabajo.

        Args:
            oferta (dict): Diccionario que contiene al menos 'titulo', y opcionalmente 'empresa' y 'salario'.
        """
        # Tarjeta contenedora con estilo personalizado
        tarjeta = ctk.CTkFrame(self.scrollable_frame, fg_color="#1e1e1e", corner_radius=10)
        tarjeta.pack(fill="x", padx=10, pady=6)

        # Título del puesto
        ctk.CTkLabel(
            tarjeta,
            text=f"📌 {oferta['titulo']}",
            font=("Segoe UI", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(8, 2))

        # Empresa y salario (si no están disponibles, se muestran valores por defecto)
        empresa = oferta.get("empresa", "No especificada")
        salario = oferta.get("salario", "No informado")

        ctk.CTkLabel(
            tarjeta,
            text=f"🏢 {empresa}     💰 {salario}",
            font=("Segoe UI", 12)
        ).pack(anchor="w", padx=10, pady=(0, 10))

    def volver_inicio(self):
        """
        Oculta el frame actual y muestra el frame de inicio de la aplicación.
        """
        self.pack_forget()  # Oculta este frame
        self.master.frame_inicio.pack(fill="both", expand=True)  # Muestra el frame de inicio
