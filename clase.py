class Eventos():
    def __init__(self, identificacion, titulo, descripcion, costo_produccion, tipo_evento, segmento_diario):
        self.identificacion = identificacion
        self.titulo = titulo
        self.descripcion = descripcion
        self.costo_produccion = costo_produccion
        self.tipo_evento = tipo_evento
        self.segmento_diario = segmento_diario

    def __str__(self):
        return "-Identificacion: " + f"{str(self.identificacion):10}" + " " + \
            "-Titulo: " + f"{str(self.titulo):9}" + " " + \
            "-Costo de produccion: " + f"{str(self.costo_produccion):8}" + " " + \
            "-Tipo de evento: " + f"{str(self.tipo_evento):2}" + " " + \
            "-Segmento diario: " + f"{str(self.segmento_diario):2}" + " " + \
            "-Descripcion: " + str(self.descripcion)
