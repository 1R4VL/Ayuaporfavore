import bcrypt

class UsuarioController:
    def __init__(self, db):
        self.db = db

    def crear_usuario(self, nombre_usuario, clave, nombre, apellido, fecha_nacimiento):
        clave_encriptada = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
        cursor = self.db.obtener_cursor()
        sql = """
            INSERT INTO rr_usuario (nombre_usuario, clave, nombre, apellido, fecha_nacimiento)
            VALUES (:nombre_usuario, :clave, :nombre, :apellido, :fecha_nacimiento)
        """
        cursor.execute(sql, {
            'nombre_usuario': nombre_usuario,
            'clave': clave_encriptada,
            'nombre': nombre,
            'apellido': apellido,
            'fecha_nacimiento': fecha_nacimiento
        })
        self.db.commit()
        cursor.close()