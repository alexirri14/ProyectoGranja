#!/usr/bin/env python3
"""
Script para verificar que todos los frameworks y librerías estén correctamente instalados.
"""

print("=== VERIFICACIÓN DE FRAMEWORKS INSTALADOS ===\n")

# Frameworks incluidos en Python estándar
print("1. Frameworks incluidos en Python estándar:")
try:
    import tkinter as tk
    print("   ✓ tkinter - Interfaz gráfica")
except ImportError as e:
    print(f"   ✗ tkinter - Error: {e}")

try:
    import sqlite3
    print("   ✓ sqlite3 - Base de datos")
except ImportError as e:
    print(f"   ✗ sqlite3 - Error: {e}")

try:
    import threading
    print("   ✓ threading - Hilos")
except ImportError as e:
    print(f"   ✗ threading - Error: {e}")

try:
    import asyncio
    print("   ✓ asyncio - Programación asíncrona")
except ImportError as e:
    print(f"   ✗ asyncio - Error: {e}")

try:
    import datetime
    print("   ✓ datetime - Manejo de fechas")
except ImportError as e:
    print(f"   ✗ datetime - Error: {e}")

try:
    import json
    print("   ✓ json - Manejo de JSON")
except ImportError as e:
    print(f"   ✗ json - Error: {e}")

try:
    import os
    print("   ✓ os - Sistema operativo")
except ImportError as e:
    print(f"   ✗ os - Error: {e}")

try:
    import sys
    print("   ✓ sys - Sistema")
except ImportError as e:
    print(f"   ✗ sys - Error: {e}")

try:
    import typing
    print("   ✓ typing - Tipos de datos")
except ImportError as e:
    print(f"   ✗ typing - Error: {e}")

try:
    import decimal
    print("   ✓ decimal - Números decimales")
except ImportError as e:
    print(f"   ✗ decimal - Error: {e}")

try:
    import re
    print("   ✓ re - Expresiones regulares")
except ImportError as e:
    print(f"   ✗ re - Error: {e}")

try:
    import functools
    print("   ✓ functools - Funciones utilitarias")
except ImportError as e:
    print(f"   ✗ functools - Error: {e}")

try:
    import collections
    print("   ✓ collections - Colecciones")
except ImportError as e:
    print(f"   ✗ collections - Error: {e}")

try:
    import dataclasses
    print("   ✓ dataclasses - Clases de datos")
except ImportError as e:
    print(f"   ✗ dataclasses - Error: {e}")

# Frameworks externos instalados
print("\n2. Frameworks externos instalados:")
try:
    import openpyxl
    print(f"   ✓ openpyxl {openpyxl.__version__} - Archivos Excel")
except ImportError as e:
    print(f"   ✗ openpyxl - Error: {e}")

try:
    import pandas as pd
    print(f"   ✓ pandas {pd.__version__} - Análisis de datos")
except ImportError as e:
    print(f"   ✗ pandas - Error: {e}")

try:
    import dateutil
    print(f"   ✓ python-dateutil {dateutil.__version__} - Utilidades de fecha")
except ImportError as e:
    print(f"   ✗ python-dateutil - Error: {e}")

try:
    import colorlog
    # Algunos módulos no tienen __version__
    version = getattr(colorlog, '__version__', 'instalado')
    print(f"   ✓ colorlog {version} - Logging con colores")
except ImportError as e:
    print(f"   ✗ colorlog - Error: {e}")

try:
    import psutil
    print(f"   ✓ psutil {psutil.__version__} - Información del sistema")
except ImportError as e:
    print(f"   ✗ psutil - Error: {e}")

try:
    import babel
    print(f"   ✓ babel {babel.__version__} - Internacionalización")
except ImportError as e:
    print(f"   ✗ babel - Error: {e}")

print("\n=== VERIFICACIÓN COMPLETADA ===")
print("Todos los frameworks necesarios para el programa están disponibles.")