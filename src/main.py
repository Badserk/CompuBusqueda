# Importa la clase principal de la interfaz gráfica desde el módulo ui.main_window
from ui.main_window import BuscadorApp

# Punto de entrada del programa
if __name__ == "__main__":
    # Crea una instancia de la aplicación principal (ventana raíz)
    app = BuscadorApp()
    
    # Inicia el bucle principal de la interfaz gráfica
    # Esto mantiene la ventana abierta y espera eventos del usuario
    app.mainloop()
