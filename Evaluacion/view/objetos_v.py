from model.objetos_m import InsumosModel, RecetasModel, ConsultasModel, AgendaModel

class InsumosView:
    def mostrar_insumo(self, insumo: InsumosModel):
        print(f"ID Insumo: {insumo.id}")
        print(f"Nombre: {insumo.nombre}")
        print(f"Tipo: {insumo.tipo}")
        print(f"Stock: {insumo.stock}")
    
    def mostrar_insumos(self, insumos):
        for insumo in insumos:
            self.mostrar_insumo(insumo)

class RecetasView:
    def mostrar_receta(self, receta: RecetasModel):
        print(f"ID Receta: {receta.id}")
        print(f"Paciente ID: {receta.paciente.id}")
        print(f"Médico ID: {receta.medico.id}")
        print(f"Descripción: {receta.descripcion}")
    
    def mostrar_recetas(self, recetas):
        for receta in recetas:
            self.mostrar_receta(receta)

class ConsultasView:
    def mostrar_consulta(self, consulta: ConsultasModel):
        print(f"ID Consulta: {consulta.id}")
        print(f"Paciente ID: {consulta.paciente.id}")
        print(f"Médico ID: {consulta.medico.id}")
        print(f"Receta ID: {consulta.receta.id}")
        print(f"Fecha: {consulta.fecha}")
        print(f"Comentarios: {consulta.comentarios}")

    def mostrar_consultas(self, consultas):
        for consulta in consultas:
            self.mostrar_consulta(consulta)

class AgendaView:
    def mostrar_agenda(self, agenda: AgendaModel):
        print(f"ID Agenda: {agenda.id}")
        print(f"Paciente ID: {agenda.paciente.id}")
        print(f"Médico ID: {agenda.medico.id}")
        print(f"Fecha Consulta: {agenda.fecha_consulta}")
        print(f"Estado: {agenda.estado}")

    def mostrar_agendas(self, agendas):
        for agenda in agendas:
            self.mostrar_agenda(agenda)