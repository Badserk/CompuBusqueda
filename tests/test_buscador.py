import customtkinter as ctk

# Configuración global
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Ventana principal
app = ctk.CTk()
app.title("Buscador con Filtros")
app.geometry("600x500")
app.resizable(False, False)

# Tabview principal
tabview = ctk.CTkTabview(app)
tabview.pack(expand=True, fill="both", padx=20, pady=20)

# Pestaña de búsqueda
busqueda_tab = tabview.add("Buscar")

# 🔍 Campo de búsqueda
search_entry = ctk.CTkEntry(busqueda_tab, placeholder_text="Buscar...", width=300)
search_entry.grid(row=0, column=0, padx=10, pady=20, sticky="w")

search_button = ctk.CTkButton(busqueda_tab, text="Buscar")
search_button.grid(row=0, column=1, padx=10, pady=20, sticky="e")

# 🔽 Filtros
label_filtros = ctk.CTkLabel(busqueda_tab, text="Filtros", font=("Segoe UI", 18, "bold"))
label_filtros.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="w")

# Categoría
label_categoria = ctk.CTkLabel(busqueda_tab, text="Categoría:")
label_categoria.grid(row=2, column=0, padx=10, sticky="w")
combo_categoria = ctk.CTkOptionMenu(busqueda_tab, values=["Todos", "Tecnología", "Salud", "Educación"])
combo_categoria.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Rango de precios
label_precio = ctk.CTkLabel(busqueda_tab, text="Rango de precios:")
label_precio.grid(row=3, column=0, padx=10, sticky="w")

precio_min = ctk.CTkEntry(busqueda_tab, placeholder_text="Mínimo", width=120)
precio_min.grid(row=3, column=1, padx=5, pady=5, sticky="w")

precio_max = ctk.CTkEntry(busqueda_tab, placeholder_text="Máximo", width=120)
precio_max.grid(row=3, column=1, padx=5, pady=5, sticky="e")

# Ordenar por
label_ordenar = ctk.CTkLabel(busqueda_tab, text="Ordenar por:")
label_ordenar.grid(row=4, column=0, padx=10, sticky="w")
combo_ordenar = ctk.CTkOptionMenu(busqueda_tab, values=["Relevancia", "Más reciente", "Precio ↑", "Precio ↓"])
combo_ordenar.grid(row=4, column=1, padx=10, pady=5, sticky="e")

# Función para mostrar resultados
def mostrar_resultados():
    # Eliminar pestaña anterior de resultados si existe
    if "Resultados" in tabview._name_list:
        tabview.delete("Resultados")

    resultados_tab = tabview.add("Resultados")
    tabview.set("Resultados")

    # Datos de ejemplo
    resultados = [
        {"titulo": "Curso de Python", "categoria": "Tecnología", "precio": "$50"},
        {"titulo": "Clases de Yoga", "categoria": "Salud", "precio": "$30"},
        {"titulo": "Tutorías de Matemáticas", "categoria": "Educación", "precio": "$40"}
    ]

    for i, r in enumerate(resultados):
        card = ctk.CTkFrame(resultados_tab, corner_radius=10)
        card.pack(padx=10, pady=10, fill="x")

        label_titulo = ctk.CTkLabel(card, text=r["titulo"], font=("Segoe UI", 16, "bold"))
        label_titulo.pack(anchor="w", padx=10, pady=(5, 0))

        label_categoria = ctk.CTkLabel(card, text=f"Categoría: {r['categoria']}")
        label_categoria.pack(anchor="w", padx=10)

        label_precio = ctk.CTkLabel(card, text=f"Precio: {r['precio']}")
        label_precio.pack(anchor="w", padx=10, pady=(0, 5))

# Conectar botón
search_button.configure(command=mostrar_resultados)

# Ejecutar app
app.mainloop()
