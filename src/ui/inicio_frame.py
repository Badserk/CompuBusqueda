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

        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_ordenar = list(FILTROS["ordenar_por"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_ordenar_por = ctk.StringVar(value="Ordenar")        
        #* Botón 1
        self.menu_ordenar_por = ctk.CTkOptionMenu(contenedor_menus,values=opciones_ordenar,variable=self.var_ordenar_por)
        self.menu_ordenar_por.pack(side="left", padx=5)

        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_fecha = list(FILTROS["fecha"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_fecha = ctk.StringVar(value="Fecha")  
        #* Botón 2
        self.menu_fecha = ctk.CTkOptionMenu(contenedor_menus,values=opciones_fecha,variable=self.var_fecha)
        self.menu_fecha.pack(side="left", padx=5)

        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_categoria = list(FILTROS["fecha"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_categoria = ctk.StringVar(value="Categoría")
        #* Botón 3
        self.menu_categoria = ctk.CTkOptionMenu(contenedor_menus, values=opciones_categoria,variable=self.var_categoria)
        self.menu_categoria.pack(side="left", padx=5)


        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_lugar_de_trabajo = list(FILTROS["ciudad"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_lugar_de_trabajo = ctk.StringVar(value="Ciudad")
        #* Botón 4
        self.menu_categoria = ctk.CTkOptionMenu(contenedor_menus, values=opciones_lugar_de_trabajo,variable=self.var_lugar_de_trabajo)
        self.menu_categoria.pack(side="left", padx=5)

        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_experiencia = list(FILTROS["experiencia"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_opciones_experiencia = ctk.StringVar(value="Experiencia")
        #* Botón 5
        self.menu_experiencia = ctk.CTkOptionMenu(contenedor_menus, values=opciones_experiencia,variable=self.var_opciones_experiencia)
        self.menu_experiencia.pack(side="left", padx=5)


        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_salario= list(FILTROS["salario"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_opciones_salario = ctk.StringVar(value="Salario")
        #* Botón 6
        self.menu_salario = ctk.CTkOptionMenu(contenedor_menus, values=opciones_salario,variable=self.var_opciones_salario)
        self.menu_salario.pack(side="left", padx=5)

        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_jornada = list(FILTROS["jornada"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_opciones_jornada = ctk.StringVar(value="Jornada")
        #* Botón 7
        self.menu_jornada = ctk.CTkOptionMenu(contenedor_menus, values=opciones_jornada,variable=self.var_opciones_jornada)
        self.menu_jornada.pack(side="left", padx=5)
        
        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_contrato = list(FILTROS["contrato"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_opciones_contrato = ctk.StringVar(value="contrato")
        #* Botón 8
        self.menu_contrato = ctk.CTkOptionMenu(contenedor_menus, values=opciones_contrato,variable=self.var_opciones_contrato)
        self.menu_contrato.pack(side="left", padx=5)
        
        #? Obtener las opciones y agregar un placeholder al inicio
        opciones_discapacidad = list(FILTROS["discapacidad"].values())
        #! Crear una variable con el valor por defecto (placeholder)
        self.var_opciones_discapacidad = ctk.StringVar(value="Discapacidad")
        #* Botón 9
        self.menu_discapacidad = ctk.CTkOptionMenu(contenedor_menus, values=opciones_discapacidad,variable=self.var_opciones_discapacidad)
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
        contrato = self.obtener_key_por_valor(FILTROS["contrato"], self.menu_contrato.get())
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
