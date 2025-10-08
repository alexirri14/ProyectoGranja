import sqlite3

conn = sqlite3.connect('granja_huevos.db')
cursor = conn.cursor()

print('=== ESTRUCTURA DE TABLAS ===')
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
tablas = cursor.fetchall()
print('Tablas disponibles:', [tabla[0] for tabla in tablas])

print('\n=== VENTAS DE JABAS ===')
cursor.execute('SELECT * FROM ventas_jabas ORDER BY id DESC')
ventas_jabas = cursor.fetchall()
print(f'Total ventas jabas: {len(ventas_jabas)}')
for venta in ventas_jabas:
    print(f'ID: {venta[0]}, Fecha: {venta[1]}, Tipo: {venta[2]}, Cantidad: {venta[3]}, Estado: {venta[4]}')

print('\n=== VENTAS GENERALES ===')
cursor.execute('SELECT * FROM ventas ORDER BY id DESC')
ventas_generales = cursor.fetchall()
print(f'Total ventas generales: {len(ventas_generales)}')
for venta in ventas_generales:
    print(f'ID: {venta[0]}, Fecha: {venta[1]}, Jabas Primera: {venta[2]}, Jabas Segunda: {venta[3]}, Peso: {venta[4]}, Precio/kg: {venta[5]}, Total: {venta[6]}')

print('\n=== LOTES ===')
cursor.execute('SELECT * FROM lotes ORDER BY id DESC')
lotes = cursor.fetchall()
print(f'Total lotes: {len(lotes)}')
for lote in lotes:
    print(f'Lote completo: {lote}')

conn.close()