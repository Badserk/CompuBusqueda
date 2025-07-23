import customtkinter as ctk
from utils.selenium_utils import configurar_driver
from logic.buscador import buscar_empleos
from logic.filtros import FILTROS, construir_url


class InicioFrame(ctk.CTkFrame):
    def __init__(self, master, callback_resultados):
        super().__init__(master)
        self.callback_resultados = callback_resultados

        ctk.CTkLabel(self, text="Buscador de Empleos", font=("Arial", 24)).pack(pady=(20, 10))

        # Entrada de búsqueda
        self.entry_busqueda = ctk.CTkEntry(self, placeholder_text="Ingresa palabras clave", width=400)
        self.entry_busqueda.pack(pady=(0, 10), anchor="center")

        # Contenedor de menús desplegables
        contenedor_menus = ctk.CTkFrame(self)
        contenedor_menus.pack(pady=(0, 10))

        # Menús desplegables (filtros)
        self.menu_ordenar_por = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["ordenar_por"].values()))
        self.menu_ordenar_por.pack(side="left", padx=5)

        self.menu_fecha = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["fecha"].values()))
        self.menu_fecha.pack(side="left", padx=5)

        self.menu_categoria = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["categoria"].values()))
        self.menu_categoria.pack(side="left", padx=5)

        self.menu_lugar_de_trabajo = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["lugar_de_trabajo"].values()))
        self.menu_lugar_de_trabajo.pack(side="left", padx=5)

        self.menu_experiencia = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["experiencia"].values()))
        self.menu_experiencia.pack(side="left", padx=5)

        self.menu_salario = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["salario"].values()))
        self.menu_salario.pack(side="left", padx=5)

        self.menu_jornada = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["jornada"].values()))
        self.menu_jornada.pack(side="left", padx=5)

        self.menu_contratoa = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["contrato"].values()))
        self.menu_contratoa.pack(side="left", padx=5)

        self.menu_discapacidad = ctk.CTkOptionMenu(contenedor_menus, values=list(FILTROS["discapacidad"].values()))
        self.menu_discapacidad.pack(side="left", padx=5)

        # Botón de búsqueda
        ctk.CTkButton(self, text="Buscar Ofertas", command=self.buscar).pack(pady=10)

        # Etiqueta de estado
        self.label_estado = ctk.CTkLabel(self, text="")
        self.label_estado.pack()

    def obtener_key_por_valor(self, diccionario, valor_buscado):
        for clave, valor in diccionario.items():
            if valor == valor_buscado:
                return clave
        return None

    def buscar(self):
        self.label_estado.configure(text="Buscando, por favor espera...")
        self.update_idletasks()

        # Obtener filtros seleccionados
        ciudad = "bogota-dc"  # puedes volverlo dinámico si lo deseas

        ordenar_por = self.obtener_key_por_valor(FILTROS["ordenar_por"], self.menu_ordenar_por.get())
        fecha = self.obtener_key_por_valor(FILTROS["fecha"],self.menu_fecha.get())
        categoria = self.obtener_key_por_valor(FILTROS["categoria"], self.menu_categoria.get())
        salario = self.obtener_key_por_valor(FILTROS["salario"], self.menu_salario.get())
        experiencia = self.obtener_key_por_valor(FILTROS["experiencia"], self.menu_experiencia.get())
        contrato = self.obtener_key_por_valor(FILTROS["contrato"], self.menu_contratoa.get())
        jornada = self.obtener_key_por_valor(FILTROS["jornada"], self.menu_jornada.get())
        discapacidad = self.obtener_key_por_valor(FILTROS["discapacidad"], self.menu_discapacidad.get())

        # Construir la URL con los filtros seleccionados
        url = construir_url(
            ciudad=ciudad,
            ordenar_por=ordenar_por,
            fecha=fecha,
            categoria=categoria,
            experiencia=experiencia,
            salario=salario,
            jornada=jornada,
            contrato=contrato,
            discapacidad=discapacidad
        )

        print("🔍 URL generada:", url)  # Para depuración

        # Ejecutar búsqueda
        driver = configurar_driver()
        try:
            resultados = buscar_empleos(url, driver)
        except Exception as e:
            resultados = []
            print("❌ Error en la búsqueda:", e)
        finally:
            driver.quit()

        self.callback_resultados(resultados)
