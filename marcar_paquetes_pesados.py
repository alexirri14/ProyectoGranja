import sqlite3

conn = sqlite3.connect('granja_huevos.db')
cursor = conn.cursor()

# Marcar los paquetes del lote 43 como pesados con un peso de ejemplo
lote_id = 43
peso_ejemplo = 1.5  # 1.5 kg por paquete

print(f'Marcando paquetes del lote {lote_id} como pesados...')

# Obtener los paquetes del lote 43 que no están pesados
cursor.execute('SELECT id FROM paquetes WHERE id_lote = ? AND (peso_kg IS NULL OR peso_kg = 0)', (lote_id,))
paquetes_sin_pesar = cursor.fetchall()

print(f'Paquetes sin pesar encontrados: {len(paquetes_sin_pesar)}')

# Marcar cada paquete como pesado
for i, (paquete_id,) in enumerate(paquetes_sin_pesar):
    # Asignar un peso ligeramente variable para simular pesaje real
    peso = peso_ejemplo + (i * 0.1)  # Variación de 0.1 kg por paquete
    cursor.execute('UPDATE paquetes SET peso_kg = ? WHERE id = ?', (peso, paquete_id))
    print(f'Paquete {paquete_id}: peso asignado = {peso} kg')

conn.commit()

# Verificar los cambios
cursor.execute('SELECT COUNT(*) FROM paquetes WHERE id_lote = ? AND peso_kg IS NOT NULL AND peso_kg > 0', (lote_id,))
paquetes_pesados = cursor.fetchone()[0]

print(f'\nPaquetes del lote {lote_id} ahora pesados: {paquetes_pesados}')

conn.close()
print('Proceso completado.')