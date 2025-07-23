from logic.filtros import FILTROS
# Importa CustomTkinter para crear interfaces modernas
import customtkinter as ctk

# Importa la función que configura el navegador con Selenium
from utils.selenium_utils import configurar_driver

# Importa la lógica para buscar empleos en una URL
from logic.buscador import buscar_empleos

class InicioFrame(ctk.CTkFrame):
    def __init__(self, master, callback_resultados):
        """
        Constructor del frame de inicio.
        """
        super().__init__(master)
        self.callback_resultados = callback_resultados

        # Título principal
        ctk.CTkLabel(self, text="Buscador de Empleos", font=("Arial", 24)).pack(pady=(20, 10))

        # Campo de entrada (barra de búsqueda)
        self.entry_busqueda = ctk.CTkEntry(self, placeholder_text="Ingresa palabras clave", width=400)
        self.entry_busqueda.pack(pady=(0, 10), anchor="center")


        # ======= Fila horizontal de menús desplegables centrados =======
        contenedor_menus = ctk.CTkFrame(self)
        contenedor_menus.pack(pady=(0, 10))
        
        #! boton filtro 1
        # Obtener los valores para mostrar en el menú
        opciones_orden = list(FILTROS["ordenar_por"].values())
        # Crear el OptionMenu con esos valores
        self.menu_ordenar_por = ctk.CTkOptionMenu(contenedor_menus, values=opciones_orden)
        self.menu_ordenar_por.pack(side="left", padx=5)

        #! boton filtro 2
        # Obtener los valores para mostrar en el menú
        opciones_fecha = list(FILTROS["fecha"].values())
        # Crear el OptionMenu con esos valores
        self.menu_fecha = ctk.CTkOptionMenu(contenedor_menus, values=opciones_fecha)
        self.menu_fecha.pack(side="left", padx=5)

        #! boton filtro 3
        # obtener los valores para mostrar en el menú
        opciones_categoria = list(FILTROS["categoria"].values())
        # Crear el OptionMenu con esos valores
        self.menu_categoria = ctk.CTkOptionMenu(contenedor_menus, values=opciones_categoria)
        self.menu_categoria.pack(side="left", padx=5)

        #! boton filtro 4
        # obtener los valores para mostrar en el menú
        opciones_lugar_de_trabajo = list(FILTROS["lugar_de_trabajo"].values())
        # Crear el OptionMenu con esos valores
        self.menu_lugar_de_trabajo = ctk.CTkOptionMenu(contenedor_menus, values=opciones_lugar_de_trabajo)
        self.menu_lugar_de_trabajo.pack(side="left", padx=5)

        #! boton filtro 5
        # obtener los valores para mostrar en el menú
        opciones_experiencia = list(FILTROS["experiencia"].values())
        # Crear el OptionMenu con esos valores
        self.menu_experiencia = ctk.CTkOptionMenu(contenedor_menus, values=opciones_experiencia)
        self.menu_experiencia.pack(side="left", padx=5)

        #! boton filtro 6
        # obtener los valores para mostrar en el menú
        opciones_salario = list(FILTROS["salario"].values())
        # Crear el OptionMenu con esos valores
        self.menu_salario = ctk.CTkOptionMenu(contenedor_menus, values=opciones_salario)
        self.menu_salario.pack(side="left", padx=5)
        
        #! boton filtro 7
        # obtener los valores para mostrar en el menú
        opciones_jornada = list(FILTROS["jornada"].values())
        # Crear el OptionMenu con esos valores
        self.menu_jornada = ctk.CTkOptionMenu(contenedor_menus, values=opciones_jornada)
        self.menu_jornada.pack(side="left", padx=5)
        
        #! boton filtro 8
        # obtener los valores para mostrar en el menú
        opciones_contrato = list(FILTROS["contrato"].values())
        # Crear el OptionMenu con esos valores
        self.menu_contratoa = ctk.CTkOptionMenu(contenedor_menus, values=opciones_contrato)
        self.menu_contratoa.pack(side="left", padx=5)
        
        #! boton filtro 9
        # obtener los valores para mostrar en el menú
        opciones_discapacidad = list(FILTROS["discapacidad"].values())
        # Crear el OptionMenu con esos valores
        self.menu_discapacidad = ctk.CTkOptionMenu(contenedor_menus, values=opciones_discapacidad)
        self.menu_discapacidad.pack(side="left", padx=5)
        # ================================================================

        #! Botón que inicia la búsqueda
        ctk.CTkButton(self, text="Buscar Ofertas", command=self.buscar).pack(pady=10)

        #? Etiqueta para mostrar el estado de la búsqueda
        self.label_estado = ctk.CTkLabel(self, text="")
        self.label_estado.pack()

    def buscar(self):
        """
        Lógica que se ejecuta al presionar el botón "Buscar Ofertas".
        """
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
