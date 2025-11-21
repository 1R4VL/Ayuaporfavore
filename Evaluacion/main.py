import bcrypt
from config.db_config import ConexionOracle
from config.db_config import validar_tablas

def conectarBD():
    """
        Realiza conexión a BD utilizando función predefinida.
    """
    db = ConexionOracle("SYSTEM", "Jeloum3n12", "localhost:1521/XEPDB1")
    db.conectar()
    validar_tablas(db)
    return db

def main():
    db = conectarBD()

    print("Inicio de sesión, ingrese sus credenciales\n")
    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))
    clave = bytes(clave, encoding="utf-8")

    salt = bcrypt.gensalt()
    clave_encriptada = bcrypt.hashpw(clave, salt)
    clave_encriptada = clave_encriptada.decode(encoding="utf-8")

    cursor = db.obtener_cursor()

    consulta = "insert into rr_usuario (nombre_usuario, clave) values (:1, :2)"
    cursor.execute(consulta, (usuario, clave_encriptada,))
    db.connection.commit()

    usuario = str(input("Ingrese su nombre de usuario: "))
    clave = str(input("Ingrese su clave: "))

    consulta = "select clave from rr_usuario where nombre_usuario = :1"
    cursor.execute(consulta, (usuario,))
    clave_bd = cursor.fetchone()
    clave_bytes = bytes(clave, encoding="utf-8")
    clave_test = bytes(clave_bd[0], encoding="utf-8",)

    validacion_clave = bcrypt.checkpw(clave_bytes, clave_test)

    if validacion_clave:
        print("Ingreso correcto")
    else:
        print("Credenciales incorrectas")

    db.desconectar()

if __name__ == "__main__":
    main()