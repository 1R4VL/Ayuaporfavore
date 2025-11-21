class UsuarioModel:
    """Modelo de usuario base."""
    def __init__(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

class PacienteModel(UsuarioModel):
    """Modelo de paciente, hereda de UsuarioModel."""
    def __init__(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, comuna, fecha_primera_visita):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento)
        self.comuna = comuna
        self.fecha_primera_visita = fecha_primera_visita


class MedicoModel(UsuarioModel):
    """Modelo de médico, hereda de UsuarioModel."""
    def __init__(self, id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento, especialidad, horario_atencion, fecha_ingreso):
        super().__init__(id, nombre_usuario, clave, nombre, apellido, fecha_nacimiento)
        self.especialidad = especialidad
        self.horario_atencion = horario_atencion
        self.fecha_ingreso = fecha_ingreso