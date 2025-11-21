from model.personas_m import PacienteModel, MedicoModel , UsuarioModel

class UsuarioView:
    """Vista para mostrar información de usuarios."""
    def mostrar_usuario(self, usuario: UsuarioModel):
        print(f"ID Usuario: {usuario.id}")
        print(f"Nombre de Usuario: {usuario.nombre_usuario}")
        print(f"Nombre: {usuario.nombre} {usuario.apellido}")
        print(f"Fecha de Nacimiento: {usuario.fecha_nacimiento}")
    
    def mostrar_usuarios(self, usuarios):
        for usuario in usuarios:
            self.mostrar_usuario(usuario)

class PacienteView:
    """Vista para mostrar información de pacientes."""
    def mostrar_paciente(self, paciente: PacienteModel):
        print(f"ID Paciente: {paciente.id}")
        print(f"Nombre de Usuario: {paciente.nombre_usuario}")
        print(f"Nombre: {paciente.nombre} {paciente.apellido}")
        print(f"Fecha de Nacimiento: {paciente.fecha_nacimiento}")
        print(f"Comuna: {paciente.comuna}")
        print(f"Fecha de Primera Visita: {paciente.fecha_primera_visita}")
    
    def mostrar_pacientes(self, pacientes):
        for paciente in pacientes:
            self.mostrar_paciente(paciente)

class MedicoView:
    """Vista para mostrar información de médicos."""
    def mostrar_medico(self, medico: MedicoModel):
        print(f"ID Médico: {medico.id}")
        print(f"Nombre de Usuario: {medico.nombre_usuario}")
        print(f"Nombre: {medico.nombre} {medico.apellido}")
        print(f"Fecha de Nacimiento: {medico.fecha_nacimiento}")
        print(f"Especialidad: {medico.especialidad}")
        print(f"Horario de Atención: {medico.horario_atencion}")
        print(f"Fecha de Ingreso: {medico.fecha_ingreso}")
    
    def mostrar_medicos(self, medicos):
        for medico in medicos:
            self.mostrar_medico(medico)

