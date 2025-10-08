# Sistema de Gestión de Huevos Comerciales

Sistema para gestionar el inventario y ventas de huevos comerciales, desarrollado con Python y Tkinter.

## Descripción

Esta aplicación permite gestionar el proceso completo de inventario y venta de huevos comerciales, desde el ingreso de lotes, pesaje de paquetes, registro de ventas y generación de reportes.

## Características Principales

- **Gestión de Inventario**: Registro y seguimiento de lotes de huevos.
- **Sistema de Pesaje**: Registro del peso de cada paquete de huevos.
- **Registro de Ventas**: Proceso de venta con cálculo automático de totales.
- **Historial y Reportes**: Consulta de ventas históricas y exportación a Excel.
- **Interfaz Gráfica**: Interfaz amigable desarrollada con Tkinter.

## Requisitos

- Python 3.6 o superior
- Bibliotecas requeridas:
  - tkinter (incluido en la mayoría de instalaciones de Python)
  - openpyxl (para exportación a Excel)

## Instalación

1. Clone o descargue este repositorio.
2. Instale las dependencias:

```bash
pip install openpyxl
```

3. Ejecute la aplicación:

```bash
python main.py
```

## Estructura del Proyecto

```
ProyectoGranja/
├── controllers/       # Controladores (lógica de negocio)
├── dao/               # Objetos de acceso a datos
├── models/            # Modelos de datos
├── utils/             # Utilidades (exportación a Excel, validaciones)
├── views/             # Interfaces gráficas
└── main.py            # Punto de entrada de la aplicación
```

## Guía de Uso

### 1. Inventario

En esta pestaña puede:
- Ver el inventario actual de lotes
- Registrar nuevos lotes
- Consultar totales de jabas, paquetes y kilos disponibles

Para registrar un nuevo lote:
1. Haga clic en "Registrar Lote"
2. Complete la información requerida (fecha, cantidad de jabas, precio por kg)
3. Haga clic en "Guardar"

### 2. Pesaje

En esta pestaña puede:
- Seleccionar un lote para pesaje
- Registrar el peso de cada paquete
- Ver el peso promedio y total del lote
- Marcar un lote como completamente pesado

Para registrar el peso de un paquete:
1. Seleccione un lote del desplegable
2. Haga clic en un paquete de la lista
3. Ingrese el peso en kilogramos
4. Haga clic en "Registrar Peso"

### 3. Ventas

En esta pestaña puede:
- Seleccionar un lote para vender
- Especificar la cantidad de jabas a vender
- Simular la venta para ver los detalles
- Confirmar y registrar la venta

Para realizar una venta:
1. Seleccione un lote del desplegable
2. Ingrese la fecha de venta y cantidad de jabas
3. Haga clic en "Simular Venta" para ver los detalles
4. Haga clic en "Confirmar Venta" para registrarla

### 4. Historial

En esta pestaña puede:
- Ver el historial de ventas
- Filtrar por fechas o por lote específico
- Ver resúmenes de ventas (totales de jabas, paquetes, kilos y montos)
- Exportar los resultados a Excel

Para exportar a Excel:
1. Aplique los filtros deseados
2. Haga clic en "Exportar a Excel"
3. Seleccione la ubicación donde guardar el archivo

## Base de Datos

La aplicación utiliza SQLite para almacenar los datos, creando automáticamente la base de datos en la primera ejecución. No se requiere configuración adicional.

## Consideraciones Técnicas

- Cada jaba contiene 2 paquetes de huevos
- Los paquetes deben ser pesados antes de poder ser vendidos
- El sistema calcula automáticamente los totales de venta basados en el peso y precio por kilogramo

## Solución de Problemas

Si encuentra algún error:
1. Verifique que todas las dependencias estén instaladas correctamente
2. Asegúrese de tener permisos de escritura en la carpeta de la aplicación
3. Revise los mensajes de error para identificar el problema específico

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.