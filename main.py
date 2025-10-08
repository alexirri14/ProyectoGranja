"""
Aplicación de gestión de inventario y ventas de huevos comerciales.
"""
import tkinter as tk
from tkinter import messagebox
import os
import sys
from views.main_window import MainWindow
from dao.db_manager import DBManager


def main():
    """Función principal para iniciar la aplicación."""
    try:
        # Inicializar la base de datos
        DBManager.create_tables()
        
        # Crear la ventana principal
        root = tk.Tk()
        app = MainWindow(root)
        
        # Iniciar el bucle principal
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()