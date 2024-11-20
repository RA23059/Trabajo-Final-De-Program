import sqlite3

def init_db():
    # Crear conexión a la base de datos
    conn = sqlite3.connect('personajes.db')
    c = conn.cursor()
    
    # Crear tabla para los personajes si no existe
    c.execute('''
        CREATE TABLE IF NOT EXISTS personajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            universo INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            url_imagen TEXT NOT NULL
        )
    ''')
    
    # Datos de ejemplo para los personajes
    personajes = [
        # Universo 11
        (11, 'Jiren', '/static/images/jiren.jpg'),
        (11, 'Toppo', '/static/images/toppo.jpg'),
        (11, 'Dyspo', '/static/images/dyspo.jpg'),
        
        # Universo 7
        (7, 'Goku', '/static/images/goku.jpg'),
        (7, 'Vegeta', '/static/images/vegeta.jpg'),
        (7, 'Gohan', '/static/images/gohan.jpg'),
        
        # Universo 6
        (6, 'Hit', '/static/images/hit.jpg'),
        (6, 'Caulifla', '/static/images/caulifla.jpg'),
        (6, 'Kale', '/static/images/kale.jpg'),
        
        # Universo 2
        (2, 'Ribrianne', '/static/images/ribrianne.jpg'),
        (2, 'Kakunsa', '/static/images/kakunsa.jpg'),
        (2, 'Rozie', '/static/images/rozie.jpg')
    ]
    
    # Limpiar datos existentes antes de insertar
    c.execute('DELETE FROM personajes')
    
    # Insertar los nuevos datos
    c.executemany('INSERT INTO personajes (universo, nombre, url_imagen) VALUES (?, ?, ?)', personajes)
    
    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()

def get_universe_characters(numero_universo):
    # Obtener personajes de un universo específico
    conn = sqlite3.connect('personajes.db')
    c = conn.cursor()
    c.execute('SELECT nombre, url_imagen FROM personajes WHERE universo = ?', (numero_universo,))
    personajes = c.fetchall()
    conn.close()
    return personajes