import sqlite3

conn = sqlite3.connect('granja_huevos.db')
cursor = conn.cursor()

print('=== PAQUETES ===')
cursor.execute('SELECT * FROM paquetes ORDER BY id DESC')
paquetes = cursor.fetchall()
print(f'Total paquetes: {len(paquetes)}')

if paquetes:
    print('\nPrimeros 10 paquetes:')
    for paquete in paquetes[:10]:
        print(f'ID: {paquete[0]}, Lote: {paquete[1]}, Peso: {paquete[2]}, Vendido: {paquete[3]}, ID_Venta: {paquete[4]}, Orden: {paquete[5]}')
else:
    print('No hay paquetes en la base de datos')

print('\n=== PAQUETES POR LOTE ===')
cursor.execute('SELECT id_lote, COUNT(*) as total, SUM(CASE WHEN peso_kg IS NOT NULL AND peso_kg > 0 THEN 1 ELSE 0 END) as pesados, SUM(CASE WHEN vendido = 1 THEN 1 ELSE 0 END) as vendidos FROM paquetes GROUP BY id_lote')
paquetes_por_lote = cursor.fetchall()
for lote_info in paquetes_por_lote:
    print(f'Lote {lote_info[0]}: Total={lote_info[1]}, Pesados={lote_info[2]}, Vendidos={lote_info[3]}')

print('\n=== LOTES ===')
cursor.execute('SELECT * FROM lotes ORDER BY id DESC')
lotes = cursor.fetchall()
for lote in lotes:
    print(f'Lote {lote[0]}: Jabas={lote[2]}, Tipo={lote[3]}, Estado={lote[4]}, Observaciones={lote[5]}')

conn.close()