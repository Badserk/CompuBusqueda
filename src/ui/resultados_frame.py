import customtkinter as ctk

class ResultadosFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Resultados de Búsqueda", font=("Arial", 20)).pack(pady=10)
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=750, height=480)
        self.scrollable_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.resultados_label = ctk.CTkLabel(self, text="")
        self.resultados_label.pack()

        ctk.CTkButton(self, text="⏪ Volver", command=self.volver_inicio).pack(pady=10)

    def mostrar_resultados(self, resultados):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if resultados:
            self.resultados_label.configure(text=f"🔎 Se encontraron {len(resultados)} ofertas:")
            for r in resultados:
                self.crear_tarjeta(r)
        else:
            self.resultados_label.configure(text="❌ No se encontraron ofertas.")

    def crear_tarjeta(self, oferta):
        tarjeta = ctk.CTkFrame(self.scrollable_frame, fg_color="#1e1e1e", corner_radius=10)
        tarjeta.pack(fill="x", padx=10, pady=6)

        ctk.CTkLabel(tarjeta, text=f"📌 {oferta['titulo']}", font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=10, pady=(8, 2))
        empresa = oferta.get("empresa", "No especificada")
        salario = oferta.get("salario", "No informado")

        ctk.CTkLabel(
            tarjeta,
            text=f"🏢 {empresa}     💰 {salario}",
            font=("Segoe UI", 12)
        ).pack(anchor="w", padx=10, pady=(0, 10))

    def volver_inicio(self):
        self.pack_forget()
        self.master.frame_inicio.pack(fill="both", expand=True)
