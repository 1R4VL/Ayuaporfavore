from model.personas_m import PacienteModel, MedicoModel

class InsumosModel:
    """Modelo de los Insumos Médicos."""
    def __init__(self, id, nombre, tipo, stock):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.stock = stock

class RecetasModel:
    """Modelo de las Recetas Médicas."""
    def __init__(self, id, paciente: PacienteModel, medico: MedicoModel, descripcion):
        self.id = id
        self.paciente = paciente
        self.medico = medico
        self.descripcion = descripcion

class ConsultasModel:
    """Modelo de las Consultas Médicas."""
    def __init__(self, id, paciente: PacienteModel, medico: MedicoModel, receta: RecetasModel, fecha, comentarios):
        self.id = id
        self.paciente = paciente
        self.medico = medico
        self.receta = receta
        self.fecha = fecha
        self.comentarios = comentarios

class AgendaModel:
    """Modelo de la Agenda Médica."""
    def __init__(self, id, paciente:PacienteModel, medico:MedicoModel, fecha_consulta, estado):
        self.id = id
        self.paciente = paciente
        self.medico = medico
        self.fecha_consulta = fecha_consulta
        self.estado = estado

