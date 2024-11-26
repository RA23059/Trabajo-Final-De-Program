import sqlite3

DATABASE = r"./personajes sql (1).db"

def get_universe_characters(universe_id):
    """Obtiene los personajes de un universo específico"""
    try:
        conexion = sqlite3.connect(DATABASE)
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT 
                nombre, 
                IFNULL(especie, 'Desconocido'), 
                IFNULL(rol, 'Desconocido'), 
                IFNULL(edad, 'Desconocido') 
            FROM personajes WHERE universo_id = ?
        """, (universe_id,))
        personajes = cursor.fetchall()
        conexion.close()
        return personajes
    except sqlite3.Error as e:
        print(f"Error al obtener personajes: {e}")
        return []